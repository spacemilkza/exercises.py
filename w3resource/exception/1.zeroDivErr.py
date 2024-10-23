"""
challenge: write a program to handle a ZeroDivisionError
when dividing by zero.
coder: malesela@spacemilk
"""

try:
  input_1 = int(input("Enter number: "))
  input_2 = int(input("Enter another number: "))
  result = round(input_1 / input_2, 2)
  print("Result: ", result)  
except ZeroDivisionError as obj:
  print("Error:", obj)


