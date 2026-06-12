import urllib.request
import json

city = "Hyderabad"
lat = 17.385
lon = 78.4867

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read())

weather = data['current_weather']
print(f"City       : {city}")
print(f"Temperature: {weather['temperature']} °C")
print(f"Wind Speed : {weather['windspeed']} km/h")
print(f"Weather Code: {weather['weathercode']}")