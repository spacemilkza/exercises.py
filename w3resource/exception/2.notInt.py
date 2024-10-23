try:
  integer = int(input("Integer: "))
  print("You've entered", integer)
  
  if not type(integer) is int:
      raise ValueError("not an integer.")
except ValueError as obj:
  print("Error: ", obj)
