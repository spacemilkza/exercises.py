"""
task: print the name and surname in reverse order input by the user
    separated by a space
"""

name = str(input("Name: "))
surname = str(input("surname: "))

print("{1} {0}".format(name, surname))
