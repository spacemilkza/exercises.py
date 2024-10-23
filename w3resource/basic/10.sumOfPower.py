"""
task: compute the user integer input as n+ n^2 + n^3 
"""

userInt = int(input("Integer: "))

userIntComputed = userInt + userInt**2 + userInt**3 

print("Sum of the repeatation of {} is {}".format(userInt, userIntComputed))