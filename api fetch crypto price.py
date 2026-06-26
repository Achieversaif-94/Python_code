import urllib.request
import json

coin = "bitcoin"
currency = "usd"
url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}&include_24hr_change=true"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read())

price  = data[coin][currency]
change = data[coin][f"{currency}_24h_change"]

print(f"Coin    : {coin.title()}")
print(f"Price   : ${price}")
print(f"24h Change: {round(change, 2)}%")