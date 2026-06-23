data = [
    "Alice - 88",
    "Bob   - 95",
    "Charlie - 76",
    "Diana - 91",
]

with open('results.txt', 'w') as f:
    for line in data:
        f.write(line + '\n')

print("Written to results.txt")
print()

with open('results.txt', 'r') as f:
    contents = f.read()

print("Reading back:")
print(contents)