########################## Assignment 3

#### 1)Python program to check given number is divided by 3 or not

num = 30
if num%3 == 0:
    print("The given number is divisible by 3")
else:
    print("The given number is not divisible by 3")

###### Take input from the user

num = int(input("Enter any number to check the divisibility of 5"))                         # input() function is only for String
if num%5==0:
    print("The given number is divisible by 5")                                            #TypeError: not all arguments converted during string formatting
else:
    print("The given number is not divisible by 5")                                       # Convert String into int



######  2)If else program to get all the numbers divided by 3 from 1 to 30

print("_"*50)
for i in range(1,31):                                                                   # starts from 1 and ends with final-1 , 30
    if i%3 == 0:
        print(i, end = " ")                                                            # end = " " , to print on the same line



####### 3) If else program to assign grades as per total marks

print("_"*50)
marks = int(input("Enter the student marks"))
if marks < 40:
    print("Fail")
elif marks >=40 and marks <=50:                                                      # elif any one of the condition will exceute whichever is first true
    print("Grade C")
elif marks >=51 and marks <=60:
    print("Grade B")
elif marks >=61 and marks <=70:
    print("Grade A")
elif marks >=71 and marks <=80:
    print("Grade A+")
elif marks >=81 and marks <=90:
    print("Grade A++")
elif marks >=91 and marks <=100:
    print("Excellent")

######## 4)Python program to check the given number divided by 3 and 5

print("@"*60)
number = int(input("Enter any number to check if its divisible by both 3 and 5"))           #Users input using input() function
if number%3 == 0 and number%5 == 0:
    print("The given number is divisible by both 3 and 5 ")
else:
    print("The given number is not divisible by both 3 and 5 ")


######### 5)Python program to print the square of the number if it is divided by 11

print("$"*60)
num = int(input("Enter any number to check if its divisible by 11"))
if num%11 == 0:
    square = num**2
    print("The given number is divisible by 11 ")
    print("The square of the given number :" , square)
else:
    print("The given number is not divisible by 11")

######### 6)Python program to check given number is a prime number or not

print("@"*60)
num = int(input("Enter any number to check prime or not"))
for i in range(2,num):
    if num%i == 0:
        print("The given number is not a prime number")
        break
    else:                                                                                    # In case else is in the same line of if, your print is many times
     print("The given number is prime")                                                      # Just 1 time print


######### 7)Python program to check given number is odd or even

print("&"*60)
num = int(input("Enter any number to check odd or even"))
if num%2 == 0:
    print("The given number is even : " ,num)
else:
    print("The given number is odd : ",num)

######## 8)Python program to check a given number is part of the Fibonacci series from 1 to 10
#0 1 1 2 3 5 8  13 21 34

print("&"*60)
fib_series = [0,1,1,2,3,5,8,13,21,34]
num = int(input("Enter any number:"))
if num in fib_series:
    print("The given number is in the Fibonacci series : ",num)
else:
    print("The given number is not in the fibonacci series : ",num)

####### 9)Python program to check authentication with the given username and password

print("&"*60)
username = input("Enter the username")
password = input("Enter the password")
if username == password:
    print("Authentication proper and valid")
else:
    print("Authentication is not valid")

####### 10)Python program to validate user_id in the list of user_ids

print("&"*60)
listOfUser_Ids = [45,3,67,84,23,47,99,100,71,25,56]
user_id = int(input("Enter any user id to check :"))
if user_id in listOfUser_Ids:
    print("The given user id is present in the list:" ,user_id)
else:
    print("The given user id is not in the list :" , user_id)










