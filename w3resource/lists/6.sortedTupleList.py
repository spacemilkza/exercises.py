"""
Task: sort the list in an ascending order by the last item of the tuple items
"""

myList = [(2, 5), (1, 2), (4, 4), (2, 3), (2,1)]

def tupleListSorter(x):
    return x[-1] - 1

myList.sort(key=tupleListSorter)

print(myList)
