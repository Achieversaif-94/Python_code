freq = {}
with open('romeo.txt') as f:
    for line in f:
        for word in line.split():
            freq[word] = freq.get(word, 0) + 1

for word in sorted(freq):
    print(word, freq[word])