import requests

def get_coin_data(id) -> dict:
    '''
        Returns a dictionary of a cryptocurrency coin's data.
        
        Function accepts one argument: id. The id is the identification # of a coin
        according to CoinMarketCap's API documentation.
        Ex. Bitcoin's id is 1.
    '''

    api_key = '4d1be5e3-3485-4db1-9666-220771d10f86' # This is my personal key.
    api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    headers = {'CMC_PRO_API_KEY': api_key, 'id': id}

    response = requests.get(api_url, headers)
    
    coin_data = response.json()['data'][str(id)] # Dictionary regarding information about the coin's data
    response.close()
    
    return coin_data
    

