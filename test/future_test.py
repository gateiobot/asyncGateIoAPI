import asyncio
from restapi import FutureClient

async def main():
    future_client = FutureClient(apikey='79235c0dcfbf88d63e5ddc15071fa888', apisecret='dc852df651aa5ee8b03c0efdbea9889b6ded7d6facf80653ebd10b118fb17def')


    # accounts,error = await future_client.get_accounts(settle='usdt')
    # print("accounts:", accounts)

    fee ,error = await future_client.get_fee(settle='usdt', contract="BTC_USDT")
    print("fee:", fee)
asyncio.run(main())