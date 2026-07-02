import urllib.request
import json
import html

url = "https://opentdb.com/api.php?amount=1&type=multiple"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read())

q = data['results'][0]
question = html.unescape(q['question'])
correct = html.unescape(q['correct_answer'])
options = [html.unescape(o) for o in q['incorrect_answers']] + [correct]
options.sort()

print(f"Category  : {q['category']}")
print(f"Difficulty: {q['difficulty'].title()}")
print(f"\nQuestion: {question}")
print("\nOptions:")
for i, option in enumerate(options, 1):
    print(f"  {i}. {option}")
print(f"\nAnswer: {correct}")