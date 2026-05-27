counts = {}
with open('mbox-short.txt') as f:
    for line in f:
        if not line.startswith('From '):
            continue
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1
max_email = None
max_count = 0
for email, count in counts.items():
    if count > max_count:
        max_count = count
        max_email = email
print(max_email, max_count)