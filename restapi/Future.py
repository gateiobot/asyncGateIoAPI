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
import json
from typing import Optional, Dict, Any, List
from .BaseClient import GateIoBaseClient
from restapi.constants import *


class FutureClient(GateIoBaseClient):

    def __init__(self, apikey='', apisecret='',
                 use_server_time=False, domain=API_URL, proxy=None):
        GateIoBaseClient.__init__(self, apikey, apisecret, use_server_time, domain, proxy)

    async def get_contracts(self, settle: str, limit: int = None, offset: int = None):

        params = {}
        url = f"/futures/{settle}/contracts"
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        success, error = await self._request("GET", url, params=params, is_auth_required=False)
        return success, error

    async def get_contract(self, settle: str, contract: str):
        url = f"/futures/{settle}/contracts/{contract}"
        success, error = await self._request("GET", url, is_auth_required=False)
        return success, error

    async def get_order_book(self, settle: str, contract: str, interval: str = "0", limit: int = 10,
                             with_id: bool = False):
        params = {
            "contract": contract,
            "interval": interval,
            "limit": limit,
            "with_id": with_id
        }
        url = f"/futures/{settle}/order_book"
        success, error = await self._request("GET", url, params=params, is_auth_required=False)
        return success, error

    async def get_trades(self, settle: str, contract: str, limit: int = 20, offset: int = 0,
                         from_time: int = 0, to_time: int = 0):
        params = {
            "contract": contract,
            "offset": offset
        }
        if limit != 0:
            params['limit'] = limit
        if from_time != 0:
            params['from'] = from_time
        if to_time != 0:
            params['to'] = to_time

        url = f"/futures/{settle}/trades"
        success, error = await self._request("GET", url, params=params, is_auth_required=False)
        return success, error

    async def get_candlesticks(self, settle: str, contract: str, from_time: int = None, to_time: int = None,
                               limit: int = None, interval: str = None):
        params = {
            "contract": contract
        }

        if from_time is not None:
            params["from"] = from_time

        if to_time is not None:
            params["to"] = to_time

        if limit is not None:
            params["limit"] = limit

        if interval is not None:
            params["interval"] = interval

        url = f"/futures/{settle}/candlesticks"
        success, error = await self._request("GET", url, params=params)
        return success, error

    async def get_premium_index_candlesticks(self, settle: str, contract: str, from_time: int = None,
                                             to_time: int = None,
                                             limit: int = None, interval: str = None):
        params = {
            "contract": contract
        }

        if from_time is not None:
            params["from"] = from_time

        if to_time is not None:
            params["to"] = to_time

        if limit is not None:
            params["limit"] = limit

        if interval is not None:
            params["interval"] = interval

        url = f"/futures/{settle}/premium_index"
        success, error = await self._request("GET", url, params=params)
        return success, error

    async def get_tickers(self, settle: str, contract: str = ""):
        params = {}
        if contract:
            params["contract"] = contract
        url = f"/futures/{settle}/tickers"
        success, error = await self._request("GET", url, params=params)
        return success, error

    async def get_funding_rate(self, settle: str, contract: str, limit: int = None):
        params = {'contract': contract}
        if limit is not None:
            params["limit"] = limit

        url = f"/futures/{settle}/funding_rate"
        success, error = await self._request("GET", url, params=params, is_auth_required=False)
        return success, error

    async def get_insurance_history(self, settle: str, limit: int = None):
        params = {}
        if limit is not None:
            params["limit"] = limit
        url = f"/futures/{settle}/insurance"
        success, error = await self._request("GET", url, params=params, is_auth_required=False)
        return success, error

    # 合约统计信息
    async def get_contract_stats(self, settle: str, contract: str, from_time: int = None, interval: str = None,
                                 limit: int = None):
        params = {"contract": contract}
        if from_time is not None:
            params["from"] = from_time

        if limit is not None:
            params["limit"] = limit

        if interval is not None:
            params["interval"] = interval

        url = f"/futures/{settle}/contract_stats"
        success, error = await self._request("GET", url, params=params, is_auth_required=False)
        return success, error

    # 查询指数来源
    async def get_index_constituents(self, settle: str, index: str):
        url = f"/futures/{settle}/index_constituents/{index}"
        success, error = await self._request("GET", url, is_auth_required=False)
        return success, error

    # 查询强平委托历史
    async def get_liquidation_orders(self, settle: str, contract: str = None, from_time: int = None,
                                     to_time: int = None,
                                     limit: int = None):
        params = {"contract": contract}
        if from_time is not None:
            params["from"] = from_time

        if to_time is not None:
            params["to"] = to_time

        if limit is not None:
            params["limit"] = limit

        url = f"/futures/{settle}/liq_orders"
        success, error = await self._request("GET", url, params=params, is_auth_required=False)
        return success, error

    # 查询风险限额等级
    async def get_risk_limit_tiers(self, settle: str, contract: str):
        url = f"/futures/{settle}/risk_limit_tiers"
        params = {"contract": contract}
        success, error = await self._request("GET", url, params=params, is_auth_required=False)
        return success, error

    # 获取合约账号
    async def get_accounts(self, settle: str):
        url = f"/futures/{settle}/accounts"
        success, error = await self._request("GET", url, is_auth_required=True)
        return success, error

    # 查询合约账户变更历史
    async def get_account_book(self, settle: str, contract: str, limit: int = None, offset: int = None,
                               from_time: int = None, to_time: int = None, change_type: str = None):
        params = {"contract": contract}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        if from_time is not None:
            params['from'] = from_time
        if to_time is not None:
            params['to'] = to_time
        if change_type is not None:
            params['type'] = change_type

        url = f"/futures/{settle}/account_book"
        success, error = await self._request("GET", url, params=params, is_auth_required=True)
        return success, error

    # 获取用户仓位列表
    async def get_positions(self, settle: str, holding: bool = None, limit: int = None, offset: int = None):
        params = {}
        if holding is not None:
            params['holding'] = holding
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset

        url = f"/futures/{settle}/positions"
        success, error = await self._request("GET", url, params=params, is_auth_required=True)
        return success, error

    # 获取单个仓位信息
    async def get_position(self, settle: str, contract: str):
        url = f"/futures/{settle}/positions/{contract}"
        success, error = await self._request("GET", url, is_auth_required=True)
        return success, error

    # 更新仓位保证金
    async def update_position_margin(self, settle: str, contract: str, change: str):
        url = f"/futures/{settle}/positions/{contract}/margin"
        params = {"change": change}
        success, error = await self._request("POST", url, params=params, is_auth_required=True)
        return success, error

    # 更新仓位杠杆
    async def update_position_leverage(self, settle: str, contract: str, leverage: str,
                                       cross_leverage_limit: str = None):
        url = f"/futures/{settle}/positions/{contract}/leverage"
        params = {"leverage": leverage}
        if cross_leverage_limit is not None:
            params['cross_leverage_limit'] = cross_leverage_limit
            params['leverage'] = '0'

        success, error = await self._request("POST", url, params=params, is_auth_required=True)
        return success, error

    # 更新仓位风险限额
    async def update_position_risk_limit(self, settle: str, contract: str, risk_limit: str = None):
        url = f"/futures/{settle}/positions/{contract}/risk_limit"
        params = {}
        if risk_limit is not None:
            params['risk_limit'] = risk_limit
        success, error = await self._request("POST", url, params=params, is_auth_required=True)
        return success, error

    # 设置持仓模式
    async def set_due_mode(self, settle: str, dual_mode: bool = False):
        url = f"/futures/{settle}/dual_mode"
        params = {"dual_mode": str(dual_mode).lower()}
        success, error = await self._request("POST", url, params=params, is_auth_required=True)
        return success, error

    # 获取双仓模式下的持仓信息
    async def get_dual_positions(self, settle: str, contract: str):
        url = f"/futures/{settle}/dual_comp/positions/{contract}"
        params = {}
        success, error = await self._request("GET", url, params=params, is_auth_required=True)
        return success, error

    # 更新双仓模式下的保证金
    async def update_dual_position_margin(self, settle: str, contract: str, change: str, dual_side: str):
        url = f"/futures/{settle}/dual_comp/positions/{contract}/margin"
        params = {"change": change, "dual_side": dual_side}
        success, error = await self._request("POST", url, params=params, is_auth_required=True)
        return success, error

    # 更新双仓模式下的杠杆
    async def update_dual_position_leverage(self, settle: str, contract: str, leverage: str,
                                            cross_leverage_limit: str = None):
        url = f"/futures/{settle}/dual_comp/positions/{contract}/leverage"

        params = {"leverage": leverage}
        if cross_leverage_limit is not None:
            params['cross_leverage_limit'] = cross_leverage_limit
            params['leverage'] = '0'

        success, error = await self._request("POST", url, params=params, is_auth_required=True)
        return success, error

    # 更新双仓模式下的风险限额
    async def update_dual_position_risk_limit(self, settle: str, contract: str, risk_limit: str):
        url = f"/futures/{settle}/dual_comp/positions/{contract}/risk_limit"
        params = {"risk_limit": risk_limit}
        success, error = await self._request("POST", url, params=params, is_auth_required=True)
        return success, error

    async def place_order(self, settle: str, futuresorder: Dict[str, Any]):
        url = f"/futures/{settle}/orders"
        data = json.dumps(futuresorder)
        success, error = await self._request("POST", url, data=data, is_auth_required=True)
        return success, error

    async def get_futures_orders(self, settle: str, status: str, contract: str = None, limit: int = None,
                                 offset: int = None, last_id: str = None):
        url = f"/futures/{settle}/orders"
        params = {
            "status": status,
        }
        if contract is not None:
            params['contract'] = contract
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        if last_id is not None:
            params['last_id'] = last_id

        success, error = await self._request("GET", url, params=params, is_auth_required=True)
        return success, error

    # 批量取消状态为 open 的订单
    async def cancel_open_orders(self, settle: str, contract: str, side: str = None):
        url = f"/futures/{settle}/orders"
        params = {"contract": contract}
        if side is not None:
            params['side'] = side
        success, error = await self._request("DELETE", url, params=params, is_auth_required=True)
        return success, error

    # 查询合约订单列表(时间区间)
    async def get_orders_in_time_range(self, settle: str, contract: str = None, from_timestamp: int = None,
                                       to_timestamp: int = None,
                                       limit: int = None, offset: int = None):
        url = f"/futures/{settle}/orders_timerange"
        params = {}
        if contract is not None:
            params['contract'] = contract
        if from_timestamp is not None:
            params['from'] = from_timestamp
        if to_timestamp is not None:
            params['to'] = to_timestamp
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset

        success, error = await self._request("GET", url, params=params, is_auth_required=True)
        return success, error

    # 合约交易批量下单
    async def place_batch_orders(self, settle: str, futuresorders: List[Dict[str, Any]]):
        url = f"/futures/{settle}/batch_orders"
        data = json.dumps(futuresorders)
        success, error = await self._request("POST", url, data=data, is_auth_required=True)
        return success, error

    # 查询单个订单详情
    async def get_order(self, settle: str, order_id: str):
        url = f"/futures/{settle}/orders/{order_id}"
        success, error = await self._request("GET", url, is_auth_required=True)
        return success, error

    # 撤销单个订单
    async def cancel_order(self, settle: str, order_id: str):
        url = f"/futures/{settle}/orders/{order_id}"
        success, error = await self._request("DELETE", url, is_auth_required=True)
        return success, error

    async def modify_order(self, settle: str, order_id: str, size: Optional[int] = None, price: Optional[str] = None,
                           amend_text: Optional[str] = None):
        url = f"/futures/{settle}/orders/{order_id}"
        body = {}
        if size is not None:
            body['size'] = size
        if price is not None:
            body['price'] = price
        if amend_text is not None:
            body['amend_text'] = amend_text
        success, error = await self._request("PUT", url, data=body, is_auth_required=True)
        return success, error

    # 查询个人成交记录
    async def get_personal_trades(self, settle: str, contract: Optional[str] = None, order: Optional[int] = None,
                                  limit: Optional[int] = None, offset: Optional[int] = None,
                                  last_id: Optional[str] = None):
        url = f"/futures/{settle}/my_trades"
        params = {}
        if contract is not None:
            params['contract'] = contract
        if order is not None:
            params['order'] = order
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        if last_id is not None:
            params['last_id'] = last_id
        success, error = await self._request("GET", url, params=params, is_auth_required=True)
        return success, error

    # 查询个人成交记录(时间区间)
    async def get_personal_trades_timerange(self, settle: str, from_time: Optional[int] = None,
                                            to_time: Optional[int] = None,
                                            contract: Optional[str] = None, limit: Optional[int] = None,
                                            offset: Optional[int] = None, role: Optional[str] = None):
        url = f"/futures/{settle}/my_trades_timerange"
        params = {}
        if from_time is not None:
            params['from'] = from_time
        if to_time is not None:
            params['to'] = to_time
        if contract is not None:
            params['contract'] = contract
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        if role is not None:
            params['role'] = role
        success, error = await self._request("GET", url, params=params, is_auth_required=True)
        return success, error

    # 查询平仓历史
    async def get_position_close_history(self, settle: str, contract: Optional[str] = None, limit: Optional[int] = None,
                                         offset: Optional[int] = None, from_time: Optional[int] = None,
                                         to_time: Optional[int] = None, side: Optional[str] = None,
                                         pnl: Optional[str] = None):
        url = f"/futures/{settle}/position_close"
        params = {}
        if contract is not None:
            params['contract'] = contract
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        if from_time is not None:
            params['from'] = from_time
        if to_time is not None:
            params['to'] = to_time
        if side is not None:
            params['side'] = side
        if pnl is not None:
            params['pnl'] = pnl
        success, error = await self._request("GET", url, params=params, is_auth_required=True)
        return success, error

    # 查询强制平仓历史
    async def get_liquidation_history(self, settle: str, contract: Optional[str] = None, limit: Optional[int] = None,
                                      at: Optional[int] = None):
        url = f"/futures/{settle}/liquidates"
        params = {}
        if contract is not None:
            params['contract'] = contract
        if limit is not None:
            params['limit'] = limit
        if at is not None:
            params['at'] = at
        success, error = await self._request("GET", url, params=params, is_auth_required=True)
        return success, error

    # 查询ADL自动减仓订单信息
    async def get_auto_deleverage_orders(self, settle: str, contract: Optional[str] = None, limit: Optional[int] = None,
                                         at: Optional[int] = None):
        url = f"/futures/{settle}/auto_deleverages"
        params = {}
        if contract is not None:
            params['contract'] = contract
        if limit is not None:
            params['limit'] = limit
        if at is not None:
            params['at'] = at
        success, error = await self._request("GET", url, params=params, is_auth_required=True)
        return success, error

    # 倒计时取消订单
    async def set_countdown_cancel_all(self, settle: str, timeout: int, contract: Optional[str] = None):
        url = f"/futures/{settle}/countdown_cancel_all"
        data = {"timeout": timeout}
        if contract is not None:
            data["contract"] = contract
        data = json.dumps(data)
        success, error = await self._request("POST", url, data=data, is_auth_required=True)
        return success, error

    # 查询合约市场交易费率
    async def get_fee(self, settle: str, contract: Optional[str] = None):
        url = f"/futures/{settle}/fee"
        params = {}
        if contract is not None:
            params["contract"] = contract
        success, error = await self._request("GET", url, params=params, is_auth_required=True)
        return success, error

    # 批量撤销指定ID的订单列表
    async def batch_cancel_orders(self, settle: str, order_ids: List[str]):
        url = f"/futures/{settle}/batch_cancel_orders"
        data = order_ids
        success, error = await self._request("POST", url, data=data, is_auth_required=True)
        return success, error

    # 创建价格触发订单
    async def create_price_trigger_order(self, settle: str, FuturesPriceTriggeredOrder: Dict[str, Any]):
        url = f"/futures/{settle}/price_orders"
        data = FuturesPriceTriggeredOrder
        success, error = await self._request("POST", url, data=data, is_auth_required=True)
        return success, error

    # 查询自动订单列表
    async def get_price_trigger_orders(self, settle: str, status: str, contract: str = None, limit: int = None,
                                       offset: int = None):
        url = f"/futures/{settle}/price_orders"
        params = {"status": status}
        if contract:
            params["contract"] = contract
        if limit:
            params["limit"] = limit
        if offset:
            params["offset"] = offset
        success, error = await self._request("GET", url, params=params, is_auth_required=True)
        return success, error

    # 批量取消自动订单
    async def cancel_batch_price_orders(self, settle: str, contract: str):
        url = f"/futures/{settle}/price_orders"
        params = {"contract": contract}
        success, error = await self._request("DELETE", url, params=params, is_auth_required=True)
        return success, error

    # 查询单个自动订单详情
    async def get_single_price_order_details(self, settle: str, order_id: str):
        url = f"/futures/{settle}/price_orders/{order_id}"
        success, error = await self._request("GET", url, is_auth_required=True)
        return success, error

    # 撤销单个自动订单
    async def cancel_single_price_order(self, settle: str, order_id: str):
        url = f"/futures/{settle}/price_orders/{order_id}"
        success, error = await self._request("DELETE", url, is_auth_required=True)
        return success, error
