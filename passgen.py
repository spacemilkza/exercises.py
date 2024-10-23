#Password Generator Project
import random
letters = [chr(x) for x in range(65, 91)]
letters.extend([chr(x) for x in range(97, 123)])
numbers = [chr(x) for x in range(48, 58)]
symbols = [chr(x) for x in range(32, 48)]

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password_len = nr_letters + nr_symbols + nr_numbers
password = ["" for x in range(password_len)]


for x in range(len(password)):

  picked = None

  if nr_letters != 0:
    picked = letters[random.randint(0, len(letters)-1)]
    nr_letters -= 1
  elif nr_symbols != 0:
    picked = symbols[random.randint(0, len(symbols)-1)]
    nr_symbols -= 1
  elif nr_numbers != 0:
    picked = numbers[random.randint(0, len(numbers)-1)]
    nr_numbers -= 1

  while True:
    y = random.randint(0, password_len-1)
    if password[y] == "":
      password[y] = picked
      break

print(f"Here is your password: {''.join(password)}")
