counts = dict()
with open('mbox-short.txt') as f:
    for line in f:
        if not line.startswith('From '):
            continue
        parts = line.split()
        time = parts[5]           # e.g. '09:14:16'
        hour = time.split(':')[0]  # e.g. '09'
        counts[hour] = counts.get(hour, 0) + 1
for hour in sorted(counts):
    print(hour, counts[hour])