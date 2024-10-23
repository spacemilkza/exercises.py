"""
task: check if key exists in dictionary
"""


myDict = {

    "name": "calvin", 
    "surname": "mas", 
    "location": "south africa, cape town"
}

print("Key exists") if "name" in myDict.keys() else print("Key doesn't exist")
