def first_non_repeating(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for ch in s:
        if count[ch] == 1:
            return ch
    return None

print(first_non_repeating("aabbcde"))
print(first_non_repeating("aabb"))