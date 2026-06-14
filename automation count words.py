import string

with open('article.txt') as f:
    text = f.read().lower()

text = text.translate(str.maketrans('', '', string.punctuation))
words = text.split()

total = len(words)
unique = len(set(words))

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

most_common = max(freq, key=freq.get)

print("Total words  :", total)
print("Unique words :", unique)
print("Most common  :", most_common, f"({freq[most_common]} times)")