"""
if condition1:
   code
elif condition2:
   code
elif condition3:
   code
else:
    code
"""

a = 600
b = 500
c = 500
d = 50
e = 60

if a > b and a > c:
    print("a has greater value :", a)
elif b > a and b > c:
    print("b has greater value :", b)
elif c > a and c > b:
    print("C has greater value :", c)
else:
    print("No variable has greater value")

if a > b and a >c :
    print("a has greater value")

if b > d and b > e:
    print("b has greater value than e and d")


# Provide grade to the students on the basis marks percentage.
print("_"*50)
marks = float(input("Please enter marks :"))

if marks >= 40 and marks <= 50:
    print("student got 3rd grade")
elif marks > 50 and marks <= 60:
    print("student got 2nd grade")
elif marks > 60 and marks <= 80:
    print("student got 1st grade")
elif marks > 80 and marks <= 100:
    print("student got Excellent A+ grade")
elif marks > 100:
    print("Marks can not be more than 100")
else:
    print("Student got failed")


# write a python for authentication

db_username = 'user123'
db_password = 'User@123'

user_name = input("Please enter username :")
password = input("Please enter password :")

if user_name == db_username and password == db_password:
    print("Login Successful")
else:
    print("Wrong username and password")