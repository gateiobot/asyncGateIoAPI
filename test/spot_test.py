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
from restapi import SpotClient
from utils.config import config

account_name = '优质稳健交易员'
apikey = config['accounts'][account_name]["key"]
apiSecret = config['accounts'][account_name]["secret"]
async def main():
    spot_client = SpotClient(apikey=apikey, apisecret=apiSecret)
    # Get list of currencies
    # currencies ,error= await spot_client.get_currencies()
    # print("Currencies:", currencies)



    # Get list of currency pairs
    # currency_pairs ,error= await spot_client.get_currency_pairs()
    # print("Currency Pairs:", currency_pairs)
    # Add more method calls as needed

    accounts, error = await spot_client.get_spot_accounts(currency='BTC')
    print("accounts:", accounts)

    # open_orders, error = await spot_client.get_open_orders()
    # print("open_orders:", open_orders)




asyncio.run(main())