import httpx

from httpx import AsyncClient
import logging
import time
from utils import config, tools
import asyncio
from restapi import SpotClient, logger
from utils.config import config


class StartUpCoinMonitor:
    BASE_URL = "https://api.gateio.ws/"

    def __init__(self):
        self._proxy = config["proxy"]
        self.new_coins_queue = asyncio.Queue()
        self.subscribers = []

    async def get_currency_pairs(self):
        url = self.BASE_URL + "api/v4/spot/currency_pairs"

        proxies = {"https://": self._proxy, "http://": self._proxy}
        async with AsyncClient(http2=True, proxies=proxies) as client:
            try:
                res = await client.get(url)
                res.raise_for_status()
                return res.json()

            except httpx.RequestError as e:
                logger.error(f"Request failed: {e}")
                return None

    def subscribe(self, startUpCoinTrader):
        self.subscribers.append(startUpCoinTrader)

    async def notify_subscribers(self, coin):
        for trader in self.subscribers:
            if coin not in trader.new_coins_queue._queue:
                await trader.new_coins_queue.put(coin)

    async def monitor_new_coins(self):
        while True:
            coins = await self.get_currency_pairs()
            if coins is None:
                continue
            current_time = int(time.time())
            new_coins = []
            for coin in coins:

                if coin.get('trade_status') == 'sellable' and coin.get('buy_start', 0) - current_time > 0:
                    await self.notify_subscribers(coin)
                    new_coins.append(coin.get('id'))
            logger.info('-------------------------------------')
            logger.info(f'待交易新币:{new_coins}')
            logger.info('-------------------------------------')
            await asyncio.sleep(1)


class StartUpCoinTradeBot:
    def __init__(self, account_name: str):
        self.account_name = account_name
        self.new_coins_queue = asyncio.Queue()
        self._api_key = config['accounts'][account_name]["key"]
        self._api_secret = config['accounts'][account_name]["secret"]
        self.spot = SpotClient(apikey=self._api_key, apisecret=self._api_secret)


    async def sell_new_coins(self):
        while True:
            try:
                coin = await self.new_coins_queue.get()
                if coin:
                    start_trade_time = coin.get("buy_start")
                    if (start_trade_time - time.time()) <= 0:
                        base_currency = coin.get('base')
                        currency_pair = coin.get('id')
                        base_currency_amount_info, error = await self.spot.get_spot_accounts(currency=base_currency)
                        if base_currency_amount_info:
                            sell_amount = base_currency_amount_info[0]['available']
                            order = {
                                "currency_pair": currency_pair,
                                "type": "market",
                                "side": "sell",
                                "amount": sell_amount,
                            }
                            created_order, error = self.spot.create_order(order)
                            if created_order:
                                while True:
                                    order_status, error = self.spot.get_order_details(created_order.id,currency_pair)
                                    if order_status.status == 'closed':
                                        logger.info(
                                            f"订单全部成交： 交易对 {created_order.currency_pair}, 状态： {order_status.status}")
                                        break
                                    elif order_status.status == 'cancelled':
                                        logger.info(f"订单被取消，重新下单")
                                        created_order, error = self.spot.create_order(order)
                                    await asyncio.sleep(1)  # 检查订单状态的间隔
                self.new_coins_queue.task_done()
            except Exception as e:
                logger.error(f"处理新币时发生错误: {e}")
            await asyncio.sleep(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    account_names = ["优质稳健交易员", "大牛哥哥"]


    async def run_tasks():
        monitor = StartUpCoinMonitor()
        traders = [StartUpCoinTradeBot(account_name) for account_name in account_names]
        tasks = [
            asyncio.create_task(monitor.monitor_new_coins())
        ]
        for trader in traders:
            monitor.subscribe(trader)
            tasks.append(
                asyncio.create_task(trader.sell_new_coins())
            )

        await asyncio.gather(*tasks)


    asyncio.run(run_tasks())
