import urllib.request
import re

url = "https://example.com"

with urllib.request.urlopen(url) as response:
    html = response.read().decode('utf-8')

links = re.findall(r'href=["\'](https?://[^"\']+)["\']', html)

print(f"Found {len(links)} links on {url}")
print()
for link in links:
    print(link)