import asyncio
from restapi import SpotClient

async def main():
    spot_client = SpotClient(apikey='XXXXXXX', apisecret='XXXXXX')
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