"""
task: find the difference of 17 and user input, if the input is greater, return double the abs difference 
"""


userInput = float(input("Enter a number: "))

if userInput > 17:
  diff = userInput*2
  print("Doubled value is {}".format(abs(diff)))
else:
  diff = userInput - 17 
  print("Difference between {} and 17 is {}".format(userInput, abs(diff)))