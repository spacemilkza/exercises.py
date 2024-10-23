"""
task: find the max of three numbers
"""

myTuple = (1, 2, 3)

def findMax(nums):
    maxNum = 0

    for x in nums:
        if x > maxNum:
            maxNum = x

    return maxNum


print("Max number is " + str(findMax(myTuple)))
