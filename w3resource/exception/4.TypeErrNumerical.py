try:
    test_types = [int, float]
    num1 = input("Number 1: ")
    num2 = input("Number 2: ")
    
    if not type(float(num1)) is float or not type(float(num2)) is float:
        raise ValueError 
    print(num1, num2)
except ValueError:
    print("Error: not a numerical value.")

   
