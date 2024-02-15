"""
Take Username and password as input through the user.
If the username and password is equal then it is authenticated.
Use if-else statement for this purpose.
Print the output.
"""
user_name = input("Enter user_name :")
password = input("Enter password :")
name = "Thushara"
pass_word = "1234"
if user_name == name:
    if password == pass_word:
        print(" Authentication successful")
    else:
        print("Password is incorrect")

else:
    print("Incorrect username and password")