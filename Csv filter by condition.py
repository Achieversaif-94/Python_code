import csv

with open('employees.csv', newline='') as f:
    reader = csv.DictReader(f)
    high_earners = [row for row in reader if row['salary'].strip() and float(row['salary']) > 50000]

print(f"Employees earning above 50000: {len(high_earners)}")
print()
for row in high_earners:
    print(f"{row['name'].strip()} - {row['salary'].strip()}")