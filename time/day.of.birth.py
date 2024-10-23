#program to get the day you were born

import datetime

date_of_birth = input("Date of birth(YYYY-MM-DD): ")

year = int(date_of_birth[0:4])
month = int(date_of_birth[5:7])
day = int(date_of_birth[-2:])

dob = datetime.datetime(year, month, day)
print(dob.strftime("You were born on a %A"))
