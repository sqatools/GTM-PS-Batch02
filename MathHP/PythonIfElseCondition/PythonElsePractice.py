#WAP for authentication

"""
db_username = 'user123'                                                     ########################################
db_password = 'User@123'

user_name = input("Please enter username :")
password = input("Please enter password :")

if user_name == db_username and password == db_password:
    print("Login Successful")
else:
    print("Wrong username and password")
"""

user_details = [
    ('user1' , 'user@123'),
    ('user2' , 'user2_234'),
    ('user3' , 'user@12356'),
    ('user4' , 'user4@123'),
]

username = input("Please enter username:")
password = input("Please enter password:")

user_entry = (username,password)

if user_entry in user_details:
   print("Login successful")
else:
   print("Login not successful")
