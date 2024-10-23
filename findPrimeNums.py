#tprogram to list prime numbers

startFrom = int(input("From: "))
endTo = int(input("To: "))
primeNums = []

for x in range(startFrom, endTo + 1):
  if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 or x in [2, 3, 5]:
    if x != 1: primeNums.append(x) 

print(primeNums, "\n", len(primeNums))
