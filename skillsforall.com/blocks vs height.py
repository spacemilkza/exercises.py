blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	

height = 0
start = 1

while blocks > start:
    blocks -= start
    start += 1
    height +=1

print("The height of the pyramid:", height)

