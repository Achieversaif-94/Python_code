import urllib.request
import json

url = "https://ipapi.co/json/"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read())

print(f"IP       : {data['ip']}")
print(f"City     : {data['city']}")
print(f"Region   : {data['region']}")
print(f"Country  : {data['country_name']}")
print(f"ISP      : {data['org']}")
print(f"Timezone : {data['timezone']}")