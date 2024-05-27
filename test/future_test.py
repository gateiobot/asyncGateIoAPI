import asyncio
from restapi import FutureClient

async def main():
    future_client = FutureClient(apikey='XXXXXX', apisecret='XXXXX')


    # accounts,error = await future_client.get_accounts(settle='usdt')
    # print("accounts:", accounts)

    fee ,error = await future_client.get_fee(settle='usdt', contract="BTC_USDT")
    print("fee:", fee)
asyncio.run(main())