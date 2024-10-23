start = 1
end = int(input("Enter Pyramid height: "))

for x in range(end):
    print(" " *(end - start) + "*" * start + "*"*(start -1))
    start += 1
