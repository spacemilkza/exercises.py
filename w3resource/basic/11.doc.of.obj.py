#11. Write a Python program to print the documents (syntax, description etc.)
#of Python built-in function(s).
#Sample function : abs()
#Expected Result :
#abs(number) -> number
#Return the absolute value of the argument.

try:
    func = input("Name of function: ")
    y = lambda x: x.__doc__
    print(y(func))
except Exception as err:
    print(err)
