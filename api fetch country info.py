import urllib.request
import json

country = "india"
url = f"https://restcountries.com/v3.1/name/{country}"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read())

info = data[0]
print("Name      :", info['name']['common'])
print("Capital   :", info['capital'][0])
print("Population:", info['population'])
print("Region    :", info['region'])
print("Currency  :", list(info['currencies'].keys())[0])