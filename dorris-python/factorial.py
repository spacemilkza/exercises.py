factorial_number = int(input("Enter number: "))

if factorial_number >= 1:
    factorial = 1
    usr_input = factorial_number
    while factorial_number > 1:
        factorial *= factorial_number
        factorial_number -=1
    print("Factorial of " + str(usr_input) + " is " + str(factorial))
else:
    print("Error: Please enter a positive number")