import csv

students = {}
with open('students.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        students[row['id']] = {'name': row['name'].strip()}

with open('marks.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        sid = row['id']
        if sid in students:
            students[sid]['marks'] = row['marks'].strip()

for sid, info in students.items():
    print(f"ID: {sid} | Name: {info['name']} | Marks: {info.get('marks', 'N/A')}")