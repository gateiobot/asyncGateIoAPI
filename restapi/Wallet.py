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

from typing import Dict, Any

from .BaseClient import GateIoBaseClient
from restapi.constants import *


class WalletClient(GateIoBaseClient):

    def __init__(self, apikey='', apisecret='',
                 use_server_time=False, domain=API_URL, proxy=None):
        GateIoBaseClient.__init__(self, apikey, apisecret, use_server_time,  domain, proxy)

    async def get_personal_fee(self, currency_pair: str = None, settle: str = None):
        url = "/wallet/fee"
        params = {}
        if currency_pair is not None:
            params["currency_pair"] = currency_pair
        if settle is not None:
            params["settle"] = settle

        success, error =await self._request("GET", url, params=params, is_auth_required=True)
        return success, error