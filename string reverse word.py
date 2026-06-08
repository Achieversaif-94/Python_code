def reverse_words(s):
    return ' '.join(s.strip().split()[::-1])

print(reverse_words("  hello world  "))
print(reverse_words("the sky is blue"))