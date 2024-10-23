"""
task: multiply items in a list
"""

items = [12, 43, 54]
product = 1

for i in range(len(items)):
    product *= items[i]

print(product)
