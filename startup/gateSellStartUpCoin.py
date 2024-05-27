"""
通过以下邀请链接注册，将享受高额的手续费返佣
1. 芝麻开门交易所（gateio）
注册芝麻开门交易所，您将获得60%以上的手续费返佣
点击此链接注册芝麻开门交易所：https://www.gateex.cc/signup/UgBHUV8M/30?ref_type?=103
备用网址（科学上网）：https://www.gate.io/signup/UgBHUV8M/30?ref_type?=103

2. 币安交易所（binance）
注册币安交易所，您将获得40%以上的手续费返佣
点击此链接币安交易所：https://accounts.suitechsui.io/register?ref=L9VRCUHB
备用网址（科学上网）：https://www.binance.com/register?ref=L9VRCUHB

3. 欧易交易所（okx）
注册欧易交易所，您将获得40%以上的手续费返佣
点击此链接欧易交易所,领取50USDT数字货币盲盒：https://www.cnouyi.info/join/4390294
备用网址（科学上网）：https://www.okx.com/join/4390294

4. bitget交易所（bitget）
注册bitget交易所，您将获得60%以上的手续费返佣
点击此链接bitget交易所：https://partner.bitget.fit/bg/Y32LHU
备用网址（科学上网）：https://partner.bitget.com/bg/Y32LHU

qq:2926888267
qq群: 649390535
微信：daniugege6
电报：https://t.me/benbenniu666
电报群：https://t.me/daniuzhandui
推特：https://twitter.com/daniugelaile
"""

import asyncio
import logging
import time
import httpx
from httpx import AsyncClient
from restapi import SpotClient, logger
from utils import config
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
                            # 获取当前市场价格
                            market_info, error = await self.spot.get_tickers(currency_pair)
                            if market_info:
                                current_price = float(market_info['last'])
                                # 计算交易金额是否满足最小限制
                                if current_price * sell_amount < 1:
                                    logger.info(f"交易金额不满足最小限制1 USDT，跳过交易：{currency_pair}")
                                    continue
                                order = {
                                    "currency_pair": currency_pair,
                                    "type": "market",
                                    "side": "sell",
                                    "amount": sell_amount,
                                }
                                created_order, error = await self.spot.create_order(order)
                                if created_order:
                                    while True:
                                        order_status, error = await self.spot.get_order_details(created_order.id,currency_pair)
                                        if order_status.status == 'closed':
                                            logger.info(
                                                f"订单全部成交： 交易对 {created_order.currency_pair}, 状态： {order_status.status}")
                                            break
                                        elif order_status.status == 'cancelled':
                                            logger.info(f"订单被取消，重新下单")
                                            created_order, error = await self.spot.create_order(order)
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
