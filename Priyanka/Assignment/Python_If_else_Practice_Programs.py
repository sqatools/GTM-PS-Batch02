#1). Python program to check given number is divided by 3 or not.
num = int(input("Enter the number: "))
if num % 3 == 0:
    print("Given number is divisible by 3")
else:
    print("Given number is not divisible by 3")

#2). If else program to get all the numbers divided by 3 from 1 to 30.

for i in range(1, 31, 1):
    if i % 3 == 0:
        print(i)
    else:
        continue

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
"""
marks = int(input("Enter the total marks: "))
if marks < 40:
    print("Result: Fail")
elif marks >= 40 and marks <= 50:
    print("Result: grade C")
elif marks > 50 and marks <= 60:
    print("Result: grade B")
elif marks > 60 and marks <= 70:
    print("Result: grade A")
elif marks > 70 and marks <= 80:
    print("Result: grade A+")
elif marks > 80 and marks <= 90:
    print("Result: grade A++")
elif marks > 90 and marks <= 100:
    print("Result: grade Excellent")
elif marks > 100:
    print("Invalid marks")

#4). Python program to check the given number divided by 3 and 5.
num4 = int(input("Enter the number: "))
if num4 % 3 == 0:
    print("Given number is divisible by 3")
elif num4 % 5 == 0:
    print("Given number is divisible by 5")
else:
    print("Given number is not divisible by 3 or 5")


#5). Python program to print the square of the number if it is divided by 11.
num5 = int(input("Enter the number: "))
if num5 % 11 == 0:
    print(num5,"is divided by 11 and its square is: ", num5**2)
else:
    print("Given number is not divisible by 1")

#6). Python program to check given number is a prime number or not.

#7). Python program to check given number is odd or even.
num7 = int(input("Enter the number: "))
if num7 % 2 == 0:
    print("Even number")
else:
    print("Odd Number")

#8). Python program to check a given number is part of the Fibonacci series from 1 to 10.

#9). Python program to check authentication with the given username and password.
db_user = ["user1","user2","priya"]
db_pw = ["pw1","pw2","priya"]

username = input("Enter the user name: ")
pw = input("Enter the pass word: ")
if username in db_user and pw in db_pw:
    print("Authentication successful")
else:
    print("Authentication failed")

#10). Python program to validate user_id in the list of user_ids.
db_user = [101,102,103,104,105,106]
userid = int(input("Enter the user ID: "))

if userid in db_user :
    print("userid is present in the list of user_ids")
else:
    print("userid is not present in the list of user_ids")

#11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
num11 = int(input("Enter the number: "))
if num11 % 2 == 0:
    print("square is: ", num11 ** 2)
elif num11 % 3 == 0:
    print("cube is: ",num11**3)
else:
    print("Given number is not divisible by 2 or 3")

#12). Python program to describe the interview process.
round1 = "pass"
round2 = "pass"
round3 = "pass"

if round1 == "pass":
    print("congrats first round is clear")
    if round2 == "pass":
        print("congrats 2nd round is also clear")
        if round3 == "pass":
            print("Congratulation you are placed")
        else:
            print("Failed in 3rd round better luck next time")
    else:
        print("sorry, you are failed in 2nd round")
else:
    print("sorry, you are failed in first round")

#13). Python program to determine whether a given number is available in the list of numbers or not.
list = [1,2,3,4,5,6,7,8,9]
number = int(input("Enter the number: "))

if number in list :
    print(number," is available in the list")
else:
    print(number," is not available in the list")

#14). Python program to find the largest number among three numbers.
a = 10; b = 20; c = 30
if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
else:
    print("c is greater")

#15). Python program to check any person eligible to vote or not. age > 18+ : eligible age < 18: not eligible
age = int(input("Enter the age: "))
if age > 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")
