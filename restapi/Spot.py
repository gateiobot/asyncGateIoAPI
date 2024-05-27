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
from typing import Optional, Dict, Any, List
from .BaseClient import GateIoBaseClient
from .constants import *


class SpotClient(GateIoBaseClient):

    def __init__(self, apikey='', apisecret='',
                 use_server_time=False, domain=API_URL, proxy=None):
        GateIoBaseClient.__init__(self, apikey, apisecret, use_server_time,  domain, proxy)


    async def get_currencies(self):
        url = f'/spot/currencies'
        params = {}

        success,error = await self._request("GET", url,params=params, is_auth_required=False)
        return success,error


    async def get_currency(self, currency: str):
        url = f'/spot/currencies'
        params = {
            'currency':currency
        }

        success, error = await self._request("GET", url, params=params, is_auth_required=False)
        return success, error

    async def get_currency_pairs(self):
        url = f'/spot/currency_pairs'
        params = {}
        success,error = await self._request("GET", url,params=params, is_auth_required=False)
        return success,error

    async def get_currency_pair(self, currency_pair: str):
        url = f'/spot/currency_pairs'
        params = {
            'currency_pair':currency_pair
        }
        success, error = await self._request("GET", url, params=params, is_auth_required=False)
        return success, error
    # Get Tickers
    async def get_tickers(self, currency_pair: str = None, timezone: str = None):
        url = f'/spot/tickers'
        params = {}
        if currency_pair is not None:
            params["currency_pair"] = currency_pair
        if timezone is not None:
            params["timezone"] = timezone

        success, error = await self._request("GET", url, params=params, is_auth_required=False)
        return success, error

    # Get Order Book
    async def get_order_book(self, currency_pair: str, interval: str = None, limit: int = None, with_id: bool = False):
        url = f'/spot/tickers'
        params = {"currency_pair": currency_pair}
        if interval is not None:
            params["interval"] = interval
        if limit is not None:
            params["limit"] = limit
        if with_id:
            params["with_id"] = with_id

        success, error = await self._request("GET", url, params=params, is_auth_required=False)
        return success, error

    async def get_trades(self, currency_pair: str, limit: int = None, last_id: str = None,
                   reverse: bool = False, from_time: int = None, to_time: int = None,
                   page: int = None):
        url = "/spot/trades"
        params = {"currency_pair": currency_pair}
        if limit is not None:
            params["limit"] = limit
        if last_id is not None:
            params["last_id"] = last_id
        if reverse is not None:
            params["reverse"] = reverse
        if from_time is not None:
            params["from"] = from_time
        if to_time is not None:
            params["to"] = to_time
        if page is not None:
            params["page"] = page

        success, error = await self._request("GET", url, params=params, is_auth_required=False)
        return success, error

    async def get_candlesticks(self, currency_pair: str, limit: int = None, from_time: int = None,
                         to_time: int = None, interval: str = None):
        url = '/spot/candlesticks'
        params = {"currency_pair": currency_pair}
        if limit is not None:
            params["limit"] = limit
        if from_time is not None:
            params["from"] = from_time
        if to_time is not None:
            params["to"] = to_time
        if interval is not None:
            params["interval"] = interval

        success, error = await self._request("GET", url, params=params, is_auth_required=False)
        return success, error

    async def get_batch_fee(self, currency_pairs: List[str]):
        url = '/spot/fee'
        params = {
            "currency_pairs": currency_pairs
        }

        success, error = await self._request("GET", url, params=params,  is_auth_required=True)
        return success, error

    async def get_spot_accounts(self, currency: str = None):
        url = "/spot/accounts"
        params = {}
        if currency is not None:
            params["currency"] = currency

        success, error = await self._request("GET", url, params=params, is_auth_required=True)
        return success, error

    async def get_spot_account_book(self, currency: str = None, from_time: int = None, to_time: int = None,
                              page: int = None, limit: int = None, type: str = None) :
        url = "/spot/account_book"
        params = {}
        if currency is not None:
            params["currency"] = currency
        if from_time is not None:
            params["from"] = from_time
        if to_time is not None:
            params["to"] = to_time
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if type is not None:
            params["type"] = type

        success, error = await self._request("GET", url, params=params, is_auth_required=True)
        return success, error

    async def place_batch_orders(self, orders: List[Dict[str, Any]]):
        url = "/spot/batch_orders"
        success, error = await self._request("POST", url, data=orders, is_auth_required=True)
        return success, error


    async def get_open_orders(self, page: int = None, limit: int = None, account: str = None):
        url = '/spot/open_orders'
        params = {}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if account is not None:
            params["account"] = account

        success, error = await self._request("GET", url, params=params, is_auth_required=True)
        return success, error
    
    async def create_order(self, order: Dict[str, Any]):
        url = "/spot/orders"
        success, error = await self._request("POST", url, data=order, is_auth_required=True)
        return success, error
    
    async def get_orders(self, currency_pair: str, status: str, page: int = None, limit: int = None, account: str = None, from_time: int = None, to_time: int = None, side: str = None):
        url = '/spot/orders'
        params = {"currency_pair": currency_pair, "status": status}
        if page is not None:
            params["page"] = page
        if limit is not None:
            params["limit"] = limit
        if account is not None:
            params["account"] = account
        if from_time is not None:
            params["from"] = from_time
        if to_time is not None:
            params["to"] = to_time
        if side is not None:
            params["side"] = side

        success, error = await self._request("GET", url, params=params, is_auth_required=True)
        return success, error
    
    async def cancel_open_orders(self, currency_pair: str, side: str = None, account: str = None, action_mode: str = None):
        url = '/spot/orders'
        params = {"currency_pair": currency_pair}
        if side is not None:
            params["side"] = side
        if account is not None:
            params["account"] = account
        if action_mode is not None:
            params["action_mode"] = action_mode

        success, error = await self._request("DELETE", url, params=params, is_auth_required=True)
        return success, error
    
    async def cancel_batch_orders(self, CancelBatchOrder: List[Dict[str, Any]]):
        url = "/spot/cancel_batch_orders"
        success, error = await self._request("POST", url, data=CancelBatchOrder, is_auth_required=True)
        return success, error
    
    async def get_order_details(self, order_id: str, currency_pair: str, account: str = None):
        url = f'/spot/orders/{order_id}'
        params = {"currency_pair": currency_pair}
        if account is not None:
            params["account"] = account

        success, error = await self._request("GET", url, params=params, is_auth_required=True)
        return success, error
    
    async def modify_order(self, order_id: str, currency_pair: str, body: Dict[str, Any], account: str = None):
        url = f'/spot/orders/{order_id}'
        params = {"currency_pair": currency_pair}
        if account is not None:
            params["account"] = account

        success, error = await self._request("PATCH", url, data=body, params=params, is_auth_required=True)
        return success, error
    
    async def cancel_order(self, order_id: str, currency_pair: str, account: str = None, action_mode: str = None):
        url = f'/spot/orders/{order_id}'
        params = {"currency_pair": currency_pair}
        if account is not None:
            params["account"] = account
        if action_mode is not None:
            params["action_mode"] = action_mode

        success, error = await self._request("DELETE", url, params=params, is_auth_required=True)
        return success, error
    
    async def get_my_trades(self, currency_pair: str = None, limit: int = None, page: int = None, order_id: str = None, account: str = None, from_time: int = None, to_time: int = None):
        url = '/spot/my_trades'
        params = {}
        if currency_pair is not None:
            params["currency_pair"] = currency_pair
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if order_id is not None:
            params["order_id"] = order_id
        if account is not None:
            params["account"] = account
        if from_time is not None:
            params["from"] = from_time
        if to_time is not None:
            params["to"] = to_time

        success, error = await self._request("GET", url, params=params, is_auth_required=True)
        return success, error
    
    async def get_server_time(self):
        url = '/spot/time'
        
        success, error = await self._request("GET", url, is_auth_required=False)
        return success, error

    async def countdown_cancel_all(self, timeout: int, currency_pair: str = None):
        url = '/spot/countdown_cancel_all'
        body = {"timeout": timeout}
        if currency_pair is not None:
            body["currency_pair"] = currency_pair

        success, error = await self._request("POST", url, data=body, is_auth_required=True)
        return success, error
    
    async def amend_batch_orders(self, orders: List[Dict[str, Any]]):
        url = "/spot/amend_batch_orders"
        success, error = await self._request("POST", url, data=orders, is_auth_required=True)
        return success, error

    async def create_price_triggered_order(self, trigger_price: str, rule: str, expiration: int,
                                     order_type: str, side: str, price: str, amount: str,
                                     account: str, market: str, time_in_force: str, text: str):
        url = "/spot/price_orders"
        body = {
            "trigger": {
                "price": trigger_price,
                "rule": rule,
                "expiration": expiration
            },
            "put": {
                "type": order_type,
                "side": side,
                "price": price,
                "amount": amount,
                "account": account,
                "market": market,
                "time_in_force": time_in_force,
                "text": text
            }
        }
        success, error = await self._request("POST", url, data=body, is_auth_required=True)
        return success, error
    
    async def get_price_triggered_orders(self, status: str, market: str = None, account: str = None,
                               limit: int = None, offset: int = None):
        url = "/spot/price_orders"
        params = {
            "status": status
        }
        if market:
            params["market"] = market
        if account:
            params["account"] = account
        if limit:
            params["limit"] = limit
        if offset:
            params["offset"] = offset
        success, error = await self._request("GET", url, params=params, is_auth_required=True)
        return success, error  

    async def cancel_batch_price_orders(self, settle: str, contract: str):
        url = "/spot/price_orders"
        params = {"contract": contract}
        success, error = await self._request("DELETE", url, params=params, is_auth_required=True)
        return success, error
    
    async def get_single_price_order_details(self, settle: str, order_id: str):
        url = f"/futures/{settle}/price_orders/{order_id}"
        success, error = await self._request("GET", url, is_auth_required=True)
        return success, error
    
    async def cancel_single_price_order(self, settle: str, order_id: str):
        url = f"/futures/{settle}/price_orders/{order_id}"
        success, error = await self._request("DELETE", url, is_auth_required=True)
        return success, error



