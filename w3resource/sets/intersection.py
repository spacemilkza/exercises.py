"""
task: create an itersection of sets
"""

mySet = set(("apple", "microsoft", "google", "facebook", "amazon"))
otherSet = {"spacemilk", "apple"}


#solution 1 
mySet.intersection(otherSet)


#solution 2
mySet.intersection_update(otherSet)
