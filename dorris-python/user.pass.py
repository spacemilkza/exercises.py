#user predefined credentials
username= "DorrisHopane"
password = "dorris1988"

#prompt the user to enter username and password to log in
username_input = input("Username: ")
password_input = input("Password: ")

#validate user input against predefined credentials
if username_input == username and password_input == password:
    print("Access granted.") #log in if matches
else:
    print("Access denied. ") # deny access if username and password don't match
