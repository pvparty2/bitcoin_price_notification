'''Represent a cryptocurrency coin.'''
import requests

class Coin:
    '''A class to represent a cryptocurrency coin.'''
    def __init__(self, id_=1) -> None: 
        '''
            Create an instance of the Coin class using an id
            as described in the CoinMarketCap documentation.
            The default is 1 - Bitcoin's id.
        '''
        self.id_ = id_


    def get_price(self) -> float:
        '''
            Return the most recent coin price from CoinMarketCap.
            The price is updated every time this function is called.
        '''
        coin_price = self.get_data()['quote']['USD']['price']
        return round(coin_price, 2)

    
    def get_date(self) -> str:
        '''Return the date of the latest price.'''
        coin_date = self.get_data()['last_updated'][:10] # Parse last_updated string to the date only. 
        return coin_date


    def get_data(self) -> dict:
        '''
            Returns a dictionary of a cryptocurrency coin's data.

            Function accepts one argument: id. The id is the identification # of a coin
            according to CoinMarketCap's API documentation.
            Ex. Bitcoin's id is 1.

            Data is updated by CoinMarketCap once every 5 minutes.
        '''

        api_key = '4d1be5e3-3485-4db1-9666-220771d10f86' # This is my personal key.
        api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

        headers = {'CMC_PRO_API_KEY': api_key, 'id': self.id_}

        response = requests.get(api_url, headers)

        coin_data = response.json()['data'][str(self.id_)] # Dictionary regarding information about the coin's data
        response.close()

        return coin_data


