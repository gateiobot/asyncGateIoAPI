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