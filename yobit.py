import requests

def get_bit():
	url = 'https://yobit.net/api/2/btc_usd/ticker'
	r = requests.get(url).json()
	price = r['ticker']['last']
	return str(price) + ' USD'