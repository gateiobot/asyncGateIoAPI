import ast
import hashlib
import hmac
import json
import time
from typing import Any, Dict
from httpx import AsyncClient
from httpx._urlparse import urlparse

from . import logger
from .constants import *


class GateIoBaseClient(AsyncClient):

    def __init__(self, apikey='', apisecret='', use_server_time=False, base_api=API_URL, proxy=None):
        super().__init__(base_url=base_api, http2=True, proxy=proxy)
        self.API_KEY = apikey
        self.API_SECRET_KEY = apisecret
        self.use_server_time = use_server_time
        self.domain = base_api

    async def _request(self, method: str, url: str, params: Dict[str, Any] = None, data: Any = None,
                       headers: Dict[str, str] = None, is_auth_required: bool = False):

        try:
            if is_auth_required:
                headers = self._get_auth_headers(method, url, params, data)
            method = method.upper()
            if method == "GET":
                response = await self.get(url, params=params, headers=headers)
            elif method == "POST":
                response = await self.post(url, params=params, data=data, headers=headers)
            elif method == "PUT":
                response = await self.put(url, params=params, data=data, headers=headers)
            elif method == "DELETE":
                response = await self.delete(url, params=params, headers=headers)

            elif method == "PATCH":  # Simulate PATCH request using request method
                    response = await self.request("PATCH", url, params=params, data=data, headers=headers)
            else:
                error = "http method error!"
                return None, error
        except Exception as e:
            logger.error("method:", method, "url:", url, "headers:", headers, "params:", params, "body:", data,
                         "data:", data, "Error:", e)
            return None, e
        code = response.status_code

        if code not in (200, 201, 202, 203, 204, 205, 206):

            text = response.text


            logger.error("method:", method, "url:", url, "headers:", headers, "params:", params, "body:", data,
                             "data:", data, "code:", code, "result:", text)
            return None, text
        try:
            result = response.json()
        except:
            result = response.text

            logger.debug("response data is not json format!", "method:", method, "url:", url, "headers:", headers,
                         "params:", params, "data:", data, "data:", data, "code:", code, "result:", result)
        logger.debug("method:", method, "url:", url, "headers:", headers, "params:", params, "body:", data,
                     "data:", data, "code:", code, "result:", json.dumps(result))
        return result, None

    def _get_auth_headers(self, method: str, url: str, params: Dict[str, Any], data: Any) -> Dict[str, Any]:
        sign, ts = self._sign_payload(method, url, params, data)
        headers = {
            "KEY": f"{self.API_KEY}",
            "SIGN": f"{sign}",
            "Timestamp": f"{ts}",
            "Accept": 'application/json',
            "Content-Type": "application/json",
            "X-Gate-Channel-Id": 'daniugege',
        }
        return headers

    def _sign_payload(self, method: str, url: str, params: Dict[str, Any], data: Any) -> (str, int):
        query_string = ""
        body = data

        ts = time.time()
        m = hashlib.sha512()
        path = '/api/v4'+urlparse(url).path

        if body is not None:
            if not isinstance(data, str):
                body = json.dumps(data)
            m.update(body.encode('utf-8'))
        body_hash = m.hexdigest()

        if params:
            qs = []
            for k, v in params.items():
                qs.append(f"{k}={v}")
            query_string = "&".join(qs)

        s = f'{method}\n{path}\n{query_string}\n{body_hash}\n{ts}'
        return self._sign(s), ts

    def _sign(self, payload) -> str:
        return hmac.new(
            self.API_SECRET_KEY.encode('utf-8'),
            payload.encode('utf-8'),
            hashlib.sha512).hexdigest()
