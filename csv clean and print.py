import csv

rows = []
with open('students.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row['name'].strip().title()
        score = row['score'].strip()
        if score == '' or name == '':
            continue
        rows.append({'name': name, 'score': int(score)})

rows.sort(key=lambda x: x['score'], reverse=True)
for r in rows:
    print(f"{r['name']}: {r['score']}")