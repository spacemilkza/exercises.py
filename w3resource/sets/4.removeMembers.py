"""
task: remove member(s) from a set
"""

mySet = set(("apple", "microsoft", "google", "facebook", "amazon"))


#solution 1
if "banana" in mySet:
    mySet.remove("banana")


#solution 2
mySet.discard("facebok")


#solution 3
mySet.pop()


#solution 4
mySet.clear()

