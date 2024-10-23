"""
task: get the largest number from a list
"""

numbers = [12, 43, 64, 23, 23]
largest = 0

#solution 1
for x in numbers:
    if x > largest:
        largest = x

print(largest)


#solution 2
print(sorted(numbers)[-1])


#solution 3 
print(max(numbers))
