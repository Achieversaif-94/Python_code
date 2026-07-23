import csv

with open('raw_data.csv', newline='') as infile:
    reader = csv.DictReader(infile)
    rows = []
    for row in reader:
        cleaned = {k: v.strip().title() for k, v in row.items()}
        if all(cleaned.values()):
            rows.append(cleaned)

with open('cleaned_data.csv', 'w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Cleaned {len(rows)} rows written to cleaned_data.csv")