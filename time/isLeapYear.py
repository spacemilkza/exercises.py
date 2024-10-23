def isLeapYear(year):
  
  if year < 1582:
          print("Not within the Gregorian calendar period")
  else:
      if year % 4 != 0:
          return False
      elif year % 100 != 0:
          return True
      elif year % 400 != 0:
          return False
      else:
          return True

print(isLeapYear(2024))
