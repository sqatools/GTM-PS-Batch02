# """
# 1). Python program to check given number is divided by 3 or not.
# 2). If else program to get all the numbers divided by 3 from 1 to 30.
# 3). If else program to assign grades as per total marks.
# marks > 40: Fail
# marks 40 – 50: grade C
# marks 50 – 60: grade B
# marks 60 – 70: grade A
# marks 70 – 80: grade A+
# marks 80 – 90: grade A++
# marks 90 – 100: grade Excellent
# marks > 100: Invalid marks
#
# 4). Python program to check the given number divided by 3 and 5.
# 5). Python program to print the square of the number if it is divided by 11.
# 6). Python program to check given number is a prime number or not.---??
# 7). Python program to check given number is odd or even.
# 8). Python program to check a given number is part of the Fibonacci series from 1 to 10.
# 9). Python program to check authentication with the given username and password.
# 10). Python program to validate user_id in the list of user_ids.

# """

# Python program to check given number is divided by 3 or not

number = 30
if number%3 == 0 :
    print("No divided by 3")
else:
    print("no not divided by 3")

#2). If else program to get all the numbers divided by 3 from 1 to 30.

for i in range(1,31):
    if i%3 == 0 :
        print(i, end=" ")

##If else program to assign grades as per total marks.
print("_"*50)

marks=float(input("Please enter the value:"))

if marks<40:
    print("Student failed")
elif marks>=40 and marks < 50:
    print("student got C grade")
elif marks>=50 and marks <60:
    print("student got B grade")
elif marks>=60 and marks<70:
    print("student got A grade")
elif marks>=70 and marks<80:
    print("student got A+ grade")
elif marks>=80 and marks<90:
    print("student got A++ grade")
elif marks>=90 and marks<=100:
    print("student got excellent rank")
else:
    print("marks not exceeded than 100")

## Python program to check the given number divided by 3 and 5.
number=9

if number%3 ==0 :
    print(number,"divided by 3")
elif number%5==0:
    print(number,"divided by 5")
else:
    print(number,"neither divided by 3 nor 5")

## Python program to print the square of the number if it is divided by 11.
number = 22
if number%11 == 0:
    square =number**2
    print("square of the number:",square)
else:
    print("Not divisible by 11")

#Python program to check given number is a prime number or not.
num = int(input("enter the input number:"))
count = 0

if num>1:
    for i in range(1,num+1):
        if (num%i)==0:
            count=count+1
    if count==2:
        print("prime")
    else:
        print("not prime")

#7). Python program to check given number is odd or even.

num=int(input("Enter the natural number:"))

if num%2 == 0 :
    print(num,"is even number")
else:
    print(num,"is odd number")

#8). Python program to check a given number is part of the Fibonacci series from 1 to 10.
n1=0
n2=1
print(n1)
print(n2)

for i in range (2,10):
    sum = n1+n2
    print(sum)
    n1=n2
    n2=sum

#check authentication with the given username and password.
username= "userid"
password="paswrd"

if username == "userid" and password == "xyz":
    print("Please enter correct password")
elif username=="ABC" and password== "xyz":
    print("Please enter the correct username and paswrd")
elif username=='ABC' and password=="pswrd":
    print("Please enter correct Username")
else:
    print("login successfully")


# 10). Python program to validate user_id in the list of user_ids.

user_ids= [2,3,4,5,6,7,8,9,19,18,90,1]
id = int(input("Enter the Value:"))

if id in user_ids:
    print(id,"is valid id")
else:
    print("Invalid user id")
