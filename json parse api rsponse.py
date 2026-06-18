import urllib.request
import json

url = "https://jsonplaceholder.typicode.com/posts"

with urllib.request.urlopen(url) as response:
    posts = json.loads(response.read())

print(f"Total posts fetched: {len(posts)}")
print()
for post in posts[:5]:
    print(f"ID    : {post['id']}")
    print(f"User  : {post['userId']}")
    print(f"Title : {post['title']}")
    print()