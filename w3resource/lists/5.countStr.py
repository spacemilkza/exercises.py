"""
task: counts strings of length >= 2 and the first and last character are the same

"""

myList = ["apple", "ease", "love", "America"]

print(len([x for x in myList if len(x) >= 2 and x[0] == x[-1]]))
