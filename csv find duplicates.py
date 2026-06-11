import csv

seen = {}
duplicates = []

with open('users.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        email = row['email'].strip().lower()
        if email in seen:
            duplicates.append(email)
        else:
            seen[email] = True

if duplicates:
    print("Duplicate emails found:")
    for d in duplicates:
        print(" ", d)
else:
    print("No duplicates found.")