## Python program to check given number is divided by 3 or not

number = 30
if number%3 == 0 :
    print("No divided by 3")
else:
    print("no not divided by 3")


## Python program to print the square of the number if it is divided by 11.

number = 22

if number%11 == 0:
    square =number**2
    print("square of the number:",square)
else:
    print("Not divisible by 11")

##Python program to check given number is a prime number or not.
# --Is it possible to find the prime no without using range function

##If else program to get all the numbers divided by 3 from 1 to 30.
for i in range (1,30):
    if i % 3 == 0:
        print(i)

## Python program to check the given number divided by 3 and 5.
number=9

if number%3 ==0 :
    print(number,"divided by 3")
elif number%5==0:
    print(number,"divided by 5")
else:
    print(number,"neither divided by 3 nor 5")

#python for even or odd:

for i in range(1,10):
    if i%2==0:
        print (i,"is even no")
    else:
        print(i,"odd no")



#Python program to check given number is a prime number or not
number=4

for i in range()

if number%number==0 and number%1==0:
    print(number,"is prime no")
else:
    print(number,"is not prime no")


#If else program to assign grades as per total marks.
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
    print("marks not exceeded than 100")--##

#Python program to check a given number is part of the Fibonacci series from 1 to 10.
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









