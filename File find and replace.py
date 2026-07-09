filename = "document.txt"
find_word = "python"
replace_word = "Python"

with open(filename, 'r') as f:
    content = f.read()

count = content.lower().count(find_word.lower())
updated = content.replace(find_word, replace_word)

with open(filename, 'w') as f:
    f.write(updated)

print(f"Replaced '{find_word}' with '{replace_word}' — {count} time(s).")