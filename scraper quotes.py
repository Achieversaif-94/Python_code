import urllib.request
import re

url = "http://quotes.toscrape.com"

with urllib.request.urlopen(url) as response:
    html = response.read().decode('utf-8')

quotes  = re.findall(r'class="text">(.*?)</span>', html)
authors = re.findall(r'class="author">(.*?)</small>', html)

for quote, author in zip(quotes, authors):
    print(f'"{quote}"')
    print(f"  — {author}")
    print()