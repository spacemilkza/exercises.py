#program to determine the lowest age you can date.

def min_age(your_age):
  """Determine the minimum age a girl can date"""
  min_age_to_date = your_age/2 + 7

  return min_age_to_date


def max_age(your_age):
  """Determine the guy's maximum age a girl can date"""
  max_age_to_date = 2*your_age - 14

  return max_age_to_date


your_age = int(input("Your age: "))
    
choice = int(input("""Choose (1 or 2):
\n1. minimum age to date
\n2. maximum age to date
\nChoice: """))

match choice:
    case 1:
      print(f"The lowest you can date is {min_age(your_age)}")
    case 2:
      print(f"The highest you can date is {max_age(your_age)}")
    
