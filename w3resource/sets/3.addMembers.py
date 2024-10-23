"""
task: add members to a set
"""

mySet = set(("apple", "microsoft", "google", "facebook", "amazon"))


mySet.update({"spacemilk"})

for x in mySet:
    print(x)
