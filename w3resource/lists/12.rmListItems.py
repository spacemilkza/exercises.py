"""
task: remove items at index 0, 4, and 5 from a list
notes: you could also methods like remove or index but these ones are simpler
"""

myList = ["red", "green", "white", "black", "pink", "yellow"]

#solution 1
print([x for x in myList if myList.index(x) not in [0, 4, 5]])


#solution 2
"""
del myList[0]
del myList[4]
del myList[5]
"""

#solution 3
myList = myList[1:4]


