
"""
task: get the smallest number from a list
"""

numbers = [12, 43, 64, 23, 23]
smallest = numbers[0]

#solution 1
for x in numbers:
    if x < smallest:
        smallest = x

print(smallest)


#solution 2
print(sorted(numbers)[0])


#solution 3 
print(min(numbers))
