"""
task: remove duplicates in list
"""

myList = [12, 34, 12, 54, 34, 54, 23, 67, 34,56, 346]

#solution 1: using pre-def func
print(list(set(myList)))


#solution 2: user-def method
setList = []

for x in myList:
    if x not in setList:
        setList.append(x)

print(setList)
