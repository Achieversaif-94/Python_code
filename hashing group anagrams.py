def group_anagrams(words):
    groups = {}
    for word in words:
        key = tuple(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
for group in group_anagrams(words):
    print(group)