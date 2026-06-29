counts = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}

with open('app.log') as f:
    for line in f:
        for level in counts:
            if level in line:
                counts[level] += 1
                break

print("Log Summary")
print("-----------")
for level, count in counts.items():
    print(f"{level}: {count}")

total = sum(counts.values())
print(f"\nTotal log entries: {total}")