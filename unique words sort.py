words = []
with open('romeo.txt') as f:
    for line in f:
        for word in line.split():
            if word not in words:
                words.append(word)
words.sort()
print(words)