# 1). Python program to check given number is divided by 3 or not.
"""
a=10
b=5

if a%3==0:
    print("value is divide by 3",a)
elif b%3==0:
    print("value is divide by 3", b)
else :
    print("value is not divide by 3")

# 2. If else program to get all the numbers divided by 3 from 1 to 30.
lower = int(input("Enter lower range limit:"))
upper = int(input("Enter upper range limit:"))
for i in range(lower, upper+1):
    if i%3==0:
        print(i)



#3). If else program to assign grades as per total marks.
Marks= float(input("please enter you mark"))

if Marks > 41 and Marks<=50:
    print("You have C Grade")
elif Marks > 51 and Marks<=60:
    print("You have B Grade")
elif Marks >61 and Marks <=70:
    print("You have A Grade")
elif Marks >71 and Marks <=80 :
    print("You have A+ Grade")
elif Marks >81 and Marks <=90 :
    print("You have A++ Grade")
elif Marks >91 and Marks <=100 :
    print("You have Excellent Grade")
elif 100 < Marks:
    print("Invalid marks")
else:
    print("you are failed")


#4 Python program to check the given number divided by 3 and 5.

a=int(input("pls enter number"))

if a%3==0 and a%5==0:
    print("number is divide by 3 and 5")
else :
    print("number is not divide by 3 and 5")


#5). Python program to print the square of the number if it is divided by 11.
a=int(input("enter number"))
if a**2 and a%11==0:
    print("this is divide by 11 :",a)
else:
    print("number is not divide by 11 :",a)



#6). Python program to check given number is a prime number or not.
a=int(input("enter number"))
if 1%a==0:
    print("number is prime")
else:
    print("number is not prime")

  #2|correct
num=int(input("enter number"))
flag = 0
if num<2:
  flag = 1
else:
  for i in range(2,int((num/2)+1)):
    if num%i==0:
      flag = 1
      break

if flag == 1:
  print('Not Prime')
else:
  print("Prime")


#7). Python program to check given number is odd or even.
a=int(input("enter number"))
if a%2==0 :
    print("number is even",a)
else:
    print("number is odd")



#8)Check a number is part of the Fibonacci series
#checking is the part of fibonacci series
fb=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
num=int(input("please enter fb series"))

if num in fb:
    print("this is part of fb series", num)
else:
    print("this num is not part of fb",num)

#taken from internet
num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()

#9). Python program to check authentication with the given username and password.
db_ub = "swamini"
db_pass= "swamini123"
username= input("enter username :")
password = input("enter password :")
if username == db_ub and password == db_pass:
    print("authenticate successfully done ")
else:
    print("please enter correct username and password")
 ---------------------------------------------------------

details=[("swami","swami123"),
         ("swamini","swamini123")
         ]

username= input("enter username :")
password = input("enter password :")

euser=(username,password)
if euser in details:
    print("Login successful")
else:
    print("Invalid username and password :", euser)

#10). Python program to validate user_id in the list of user_ids.

user_ids=[1,2,3,4,5,6,7,8,9]

user_id=int(input("enter valid user id : "))
if user_id in user_ids :
    print("valid id")
else:
    print("invalid user id")

"""
"""
#11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.

num=int(input("pls enter number"))

if num%2==0:
    print ("number is divide by 2 ",num**2)

elif num%3==0 :
    print("number is divide by  3",num**3)
else:
    print("number is not divide by 2 and 3")

"""
"""
num=int(input("pls enter number"))
if num%2==0 or num%3==0:
    print ("number is divide by 2 and 3 ",num**2,num**3)
else:
    print("number is not divide by 2 and 3")

#12). Python program to describe the interview process.
r1= input("enter round1 result")
r2 = input("enter round1 result")
if r1=="passed":
    print("you clear round 1")
    if r2=="passed":
        print("you clear round 2")
    else :
        print("round 2 is not clear")
else :
    print("round 1 is not clear")

#13). Python program to determine whether a given number is available in the list of numbers or not.
l1=[1,2,3,4,5,6,7,8,9]

num=int(input("pls enter num"))

if num in l1:
    print("number is available in list ")
else:
    print("number is not available in list")

#14). Python program to find the largest number among three numbers.
a=int(input("pls enter num1"))
b=int(input("pls enter num2"))
c=int(input("pls enter num3"))
if a>b and a>c:
    print("a is largest num than b and c")
    if b>a and b>c:
        print("b is largest num than a and c")
        if c>a and c>b:
            print("c is largest num than a and b")
        else:
            print("a and b is largest number")
    else :
        print("a and c is largest number")
else:
    print("b and c is largest number")
"""
"""
#15). Python program to check any person eligible to vote or not
age > 18+ : eligible
age < 18: not eligible
"""
"""
age = int(input("pls enter age"))

if age >=18:
    print("you are eligble for vote")
else :
    print("you are not eligible for vote")


#-------------------------------------------------------------------------------------
#16). Python program to check whether any given number is a palindrome.
num1 = 121
num2 = str(num1)

if num1 == int(num2[::-1]):
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")
----------------------------------------------------------------------------------------------------------------
#18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.

marks=float(input("pls enter marks"))
if marks>=35:
    print("student is passed")
else:
    print("student is failed")


#19). Python program to check whether the given number is positive or not.
num=int(input("enter number"))
if num>=0:
    print("the num is positive")
elif num<0:
        print("the number is negative")
else:
    print("invalid number")

#21). Python program to check whether the given number is positive or negative and even or odd.
num = int(input("Enter a number: "))

if num>0:
    if num%2 == 0:
        print("The given number is positive and even")
    else:
        print("The given number is positive and odd")
else:
    if num%2 == 0:
        print("The given number is negative and even")
    else:
        print("The given number is negative and odd")

#22). Python program to print the largest number from two numbers.
num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
if num1>num2:
    print("num1 is greater number")
elif num1==num2:
    print("both number is equal")
else:
    print("num2 is greater num")
"""
"""
23). Python program to check whether a given character is uppercase or not.
Input = A
Output = The given character is an Uppercase

a=input("enter input: ")
if a.isupper():
    print("char is upper case")
else :
    print("char is small case")
"""
"""24). Python program to check whether the given character is lowercase or not.
Input = c
Output = True

a=input("enter character: ")
if a.islower():
    print("True")
else :
     print("False")

"""

"""25). Python program to check whether the given number is an integer or not.
Input = 54
Output = True
a=34.2
if type(a)==int:
    print("number is interger")
else:
    print("number is not integer")
"""
"""26). Python program to check whether the given number is float or not.
Input = 12.6
Output = True


a=23.3
if type(a)==float:
    print("number is float")
else:
    print("number is not float")
"""

"""
27). Python program to check whether the given input is a string or not.
Input = ‘sqatools’
Output = True
a="Swamini"
if type(a)==str:
    print("True")
else:
    print("false")
"""

"""28). Python program to print all the numbers from 10-15 except 13

for a in range(10,16):
    if  a!=13:
        print(a)
"""
"""
30). Python program to check whether a given year is a leap or not.
Input = 2000
Output = The given year is a leap year"""
a=int(input("enter year"))
if a%400==0 or a%4==0:
    print("year is leap year")
else:
    print("year is not leap year")








