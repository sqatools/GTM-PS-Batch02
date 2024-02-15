# write a python program for authenticate
db_username = 'user123'
db_password = 'user@123'

user_name = input("please enter user name")
password = input("please enter password")

if user_name == db_username and password == db_password:
   print("Login is successfull")
else:
     print("wrong password")
