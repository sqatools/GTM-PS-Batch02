"""
SQA Tools
Python If-Else Programs
1 to 10
"""
"""
#    1). Python program to check given number is divided by 3 or not.

num = int(input("Enter number: "))
if num%3 ==0:
    print("divisible by 3")
else:
    print("not divided by 3")

print("_"*100)

"""


"""
#2. If else program to get all the numbers divided by 3 from 1 to 30

for i in range(1,31):
    if i%3==0:
        print(i)

print("_"*100)

"""


"""
3). If else program to assign grades as per total marks.
    marks > 40: Fail
    marks 40 – 50: grade C
    marks 50 – 60: grade B
    marks 60 – 70: grade A
    marks 70 – 80: grade A+
    marks 80 – 90: grade A++
    marks 90 – 100: grade Excellent
    marks > 100: Invalid marks

marks = int(input("Enter Total Marks: "))

if marks < 40:
    print("Fail")
elif marks >= 40  and marks <=50:
    print("grade C")
elif marks >50 and marks <=60:
    print("grade B")
elif marks >60 and marks <=70:
    print("grade A")
elif marks >70 and marks <=80:
    print("grade A+")
elif marks>80 and marks <=90:
    print("grade A++")
elif marks>90 and marks<=100:
    print("grade Excellent")
else:
    print("Invalid Marks")

print("_"*100)

"""

"""
    4). Python program to check the given number divided by 3 and 5.
"""
"""
num2 = int(input("Enter Number divided by 3 and 5: "))
if (num2%3 == 0) and (num2%5 == 0):
    print("Yes,Divisible by 3 & 5: ",num2)
else:
    print("No,Not divisible by 3 & 5: ",num2)
print("_"*100)
"""


"""
    5. Python program to print the square of the number if it is divided by 11.


num3 = int(input("Enter Number divided by 11: "))
if ( num3%11 ==0 ):
    #number is divisible by 11 then do sqaure of num3
    sqaureofnum = num3**2
    print("Sqaure of number divisible by 11 is : ",sqaureofnum)
else:
    print("Number is not divisible by 11")
"""

"""
6.Python program to check given number is a prime number or not.
"""
num4 = int(input("Enter Number to check prime or not: "))
count = 0

for i in range(2,num4):
   if(num4%i==0):
       count = count+1
       print("count: ",count,' ', i)

if count > 0:
    print("Number is Prime")
else:
    print("Number is not Prime")

print("_"*100)

"""
7. Python program to check given number is odd or even.
"""
num5 = int(input("Enter Number to check even or odd: "))

if (num5%2==0):
    print("Number is even")
else:
    print("Number is Odd")

print("_"*100)


"""
8. Python program to check a given number is part of the Fibonacci series from 1 to 10.
"""

# initialize two variables, with value 0

a,b = 0,1
endvalue = 10

print(a,b,end="")
for i in range(endvalue):
    c = a+b
    print(c,end=" ")
    a=b
    b=c
print('\n')
print("_"*100)

"""
    9. Python program to check authentication with the given username and password.
"""
username = 'madhuri'
password = 'password'

username_input = input("Enter username: ")
password_input = input("Enter password: ")

if(username_input == username) and (password_input == password):
    print("User Authenticated Sucessfully")
else:
    print("Invalid username or password")

"""
    10). Python program to validate user_id in the list of user_ids.
"""
#assume user_ids list as
user_ids = [1,2,3,4,5,6,7,8,9,10]

user_id = int(input("Enter User ID you want to Search: "))

if user_id in user_ids:
    print("User id Validated")
else:
    print("User id is Invalid")