from datetime import datetime

now = datetime.now()

print("Current Date & Time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)

print(now.strftime("%d-%m-%Y"))
print(now.strftime("%I:%M %p"))