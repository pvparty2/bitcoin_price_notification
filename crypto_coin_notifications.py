import time
import ifttt
from coin import Coin


BITCOIN_PRICE_THRESHOLD = 50000
ifttt_emergency_event = 'bitcoin_price_emergency'
ifttt_update_event = 'bitcoin_price_update'


def main(): 
    coin = Coin() # Bitcoin's id is 1 according to CoinMarketCap's API documentation.

    while True:
        coin_price = coin.get_price()

        # Send an emergency notification
        if coin_price > BITCOIN_PRICE_THRESHOLD:
            ifttt.webhook_notify(ifttt_emergency_event, coin_price)
        else:
            ifttt.webhook_notify(ifttt_update_event, coin_price)

        # Sleep for 5 minutes before sending another coin price update.
        time.sleep(5 * 60)


if __name__ == '__main__':
    main()
