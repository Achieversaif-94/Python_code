import urllib.request

urls = [
    "https://example.com",
    "https://google.com",
    "https://github.com",
    "https://this-site-does-not-exist-xyz.com",
]

for url in urls:
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            print(f"UP   [{response.status}]  {url}")
    except Exception as e:
        print(f"DOWN          {url}  ({type(e).__name__})")