"""
task: Write a function to find if two lists have at least a common item
"""

limpopo = ["township", "south africa", "country"]
capeTown = ["city", "south africa", "coastal"]

def commonItem(list1, list2):

    for x in list1:
        if x in list2:
            return True
    return False


print(commonItem(limpopo, capeTown))
