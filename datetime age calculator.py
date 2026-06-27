from datetime import date

dob_str = "2005-08-15"
year, month, day = map(int, dob_str.split('-'))
dob = date(year, month, day)
today = date.today()

years = today.year - dob.year
months = today.month - dob.month
days = today.day - dob.day

if days < 0:
    months -= 1
    days += 30
if months < 0:
    years -= 1
    months += 12

print(f"Date of Birth: {dob}")
print(f"Today        : {today}")
print(f"Age          : {years} years, {months} months, {days} days")