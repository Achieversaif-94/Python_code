from datetime import date

event_name = "New Year"
event_date = date(2027, 1, 1)
today = date.today()

days_left = (event_date - today).days

if days_left > 0:
    print(f"{days_left} days left until {event_name} ({event_date})")
elif days_left == 0:
    print(f"{event_name} is today!")
else:
    print(f"{event_name} was {abs(days_left)} days ago")