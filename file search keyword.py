import os

folder  = "notes"
keyword = "python"

matches = []

for filename in os.listdir(folder):
    if filename.endswith('.txt'):
        filepath = os.path.join(folder, filename)
        with open(filepath) as f:
            for line_num, line in enumerate(f, 1):
                if keyword.lower() in line.lower():
                    matches.append((filename, line_num, line.strip()))

print(f"Keyword '{keyword}' found in {len(matches)} line(s):\n")
for filename, line_num, line in matches:
    print(f"{filename} | Line {line_num}: {line}")