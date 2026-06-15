import urllib.request

url = "https://example.com"

with urllib.request.urlopen(url) as response:
    html = response.read().decode('utf-8')

print("Status :", response.status)
print("Length :", len(html), "characters")
print()
print("First 500 characters:")
print(html[:500])