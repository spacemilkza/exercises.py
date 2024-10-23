"""
task: merge two dictionaries
"""

dict1 = {2**x:"2^{}".format(x) for x in range(2, 5)}
dict2 = {3**x:"3^{}".format(x) for x in range(2, 5)}

dict1.update(dict2)

print(dict1)
