import urllib.request
import re

url = "https://example.com"
target_word = "example"

with urllib.request.urlopen(url) as response:
    html = response.read().decode('utf-8')

clean_text = re.sub(r'<.*?>', ' ', html).lower()
words = clean_text.split()
count = words.count(target_word.lower())

print(f"URL        : {url}")
print(f"Word       : '{target_word}'")
print(f"Occurrences: {count}")