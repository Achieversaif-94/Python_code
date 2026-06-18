import json

with open('data.json') as f:
    data = json.load(f)

for item in data:
    name = item.get('name', 'N/A')
    age  = item.get('age', 'N/A')
    city = item.get('city', 'N/A')
    print(f"{name} | Age: {age} | City: {city}")
    