counts = {}
with open('mbox-short.txt') as f:
    for line in f:
        if not line.startswith('From '):
            continue
        words = line.split()
        email = words[1]
        domain = email.split('@')[1]
        counts[domain] = counts.get(domain, 0) + 1

max_domain = None
max_count = 0
for domain, count in counts.items():
    if count > max_count:
        max_count = count
        max_domain = domain

print(max_domain, max_count)