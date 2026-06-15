import urllib.request

url = "https://example.com"

with urllib.request.urlopen(url) as response:
    headers = response.headers

print("HTTP Headers for:", url)
print()
for key, value in headers.items():
    print(f"{key}: {value}")