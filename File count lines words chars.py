filename = "article.txt"

lines = 0
words = 0
chars = 0

with open(filename) as f:
    for line in f:
        lines += 1
        words += len(line.split())
        chars += len(line)

print(f"File     : {filename}")
print(f"Lines    : {lines}")
print(f"Words    : {words}")
print(f"Characters: {chars}")