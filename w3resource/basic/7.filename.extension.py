#7. Write a Python program that accepts a filename from the user and prints the
#extension of the file.
#Sample filename : abc.java
#Output : java


try:
    filename = input("Filename: ")
    
    if "." in filename:
        x = filename.rfind(".")
        y = filename[x:]
        print(y.replace(".", ""))
    
except Exception as err:
    print(err)
