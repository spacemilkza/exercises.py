"""
Task: Sum all the items in a list
"""

items = [12, 23, 54, 86]
sum = 0

#method 1
for i in items:
    sum += i


"""
#method 2
index = 0
while index < len(items):
    sum += items[index]
    index += 1


#method 2
for i in range(len(items)):
    sum += items[i]
"""

print(sum)

