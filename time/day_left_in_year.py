# A program to count how long you've lived in realtime.
# test data: {name: karabo mathole, d.o.b: 2002-09-11 at 09:00}

import datetime
from isLeapYear import isLeapYear

x = datetime.datetime.now()
isLeapYear = isLeapYear(2024)

print(x.strftime(f"%j of {366 if isLeapYear else 365} days left"))
