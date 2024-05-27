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
# Url
API_URL = 'https://api.gateio.ws/api/v4'


# Methods
GET = "GET"
POST = "POST"

# Headers
ACCEPT = 'Accept'
CONTENT_TYPE = 'Content-Type'
APPLICATION_JSON = 'application/json'

# Headers
GATEIO_ACCESS_KEY = 'KEY'
GATEIO_ACCESS_SIGN = 'SIGN'
GATEIO_ACCESS_TIMESTAMP = 'Timestamp'


# Broker Id
BROKER_ID = ''

# System Endpoints
SPOT_CURRENCIES = '/api/v4/spot/currencies'
SPOT_CURRENCY = '/api/v4/spot/{currency}'
SPOT_CURRENCY_PAIRS = '/spot/currency_pairs'
SPOT_CURRENCY_PAIR = '/spot/currency_pairs'

SPOT_SYSTEM_TIME = '/api/v4/spot/time'
SPOT_TICKERS = '/api/v4/spot/tickers'
SPOT_ORDER_BOOKS = '/api/v4/spot/order_book'
SPOT_TRADES = '/spot/trades'
SPOT_CANDLESTICKS = '/spot/candlesticks'
SPOT_BATCH_FEE = '/spot/batch_fee'