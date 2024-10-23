"""
task: find words that have less than N length
"""

myList = ["calvin", "mas", "south africa", "cape town"]
N = 4

myListLess = [x for x in myList if len(x) <= N]

print(myListLess)
