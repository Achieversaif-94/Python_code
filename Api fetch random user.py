import urllib.request
import json

url = "https://randomuser.me/api/"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read())

user = data['results'][0]
name = f"{user['name']['first']} {user['name']['last']}"
email = user['email']
country = user['location']['country']
age = user['dob']['age']
phone = user['phone']

print(f"Name   : {name}")
print(f"Email  : {email}")
print(f"Country: {country}")
print(f"Age    : {age}")
print(f"Phone  : {phone}")