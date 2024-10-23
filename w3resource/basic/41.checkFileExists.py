#check whether a file exists

import os

while True:
    fileName = str(input("Type a filename: "))

    if fileName in os.listdir():
        print("File exists")
    else:
        print("File doesn't exist")
