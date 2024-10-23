"""
task: remove member if in set
"""

mySet = set(("apple", "microsoft", "google", "facebook", "amazon"))


if "bytedance" in mySet:
    mySet.remove("bytedance")
