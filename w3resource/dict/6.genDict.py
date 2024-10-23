"""
task: generate and print a dictionary that contains a number ranging from 1 to n
"""

n = 5
myDict = {x:x*x for x in range(1, n+1)}

print(myDict)
