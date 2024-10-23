"""
task: create the set difference
"""

mySet = set(("apple", "microsoft", "google", "facebook", "amazon"))
myOtherSet = {"openAI", "spacemilk", "bytedance"}


#solution 1
myOtherOtherSet = mySet.symmetric_difference(myOtherSet)


#solution 2
mySet.symmetric_difference_update(myOtherSet)



