#program to check given number is divided by 3 or not

num = int(input("Enter a num: "))
if num % 3 == 0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")
'''
Enter a num: 40
Number is not divisible by 3

Enter a num: 27
Number is divisible by 3
'''

#If else program to assign grades as per total marks.
'''
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks
'''

marks = int(input("Enter a marks of student :"))
if marks < 40:
    print("student failed")
elif marks > 40 and marks<50:
    print("student got grade C")
elif marks > 50 and marks <60:
    print("student got grade B")
elif marks > 60 and marks < 70:
    print("student got grade A")
elif marks > 70 and marks < 80:
    print("student got grade A+")
elif marks > 80 and marks < 90:
    print("student got grade A++")
else:
    print("student got grade A+++")


# program to check the given number divided by 3 and 5

num1 = int(input("Enter the number: "))
if num1 % 3 == 0 and num1 % 5 == 0:
    print("Number is divisible by 3 and 5")
else:
    print("Number is not divisible by 3 and 5")

# program to print the square of the number if it is divided by 11.

num2 = int(input("enter a number"))
val = num2 **2
if val % 11 ==0:
    print("square root of the num is divisible by 11")
else:
    print("square root of the num is not divisible by 11")

# program to check given number is odd or even

num3 = int(input("Enter the number: "))
if num3 % 2 == 0:
    print("the given number is even")
else:
    print("the given number is odd")

#Program to check the authentication of username and password

Username = "Ashwini_s"
Password = "password@123"

if  Username == "Ashwini_s" and Password == "password@123":
    print("Authentication is successful")
else:
    print("Authentication is failed")

#program to print a square or cube if the given number is divided by 2 or 3 respectively.

num4 = int(input("Enter the number: "))
if num4 % 2 == 0:
    square_root = num4**2
    print("square root of the num4 value is: ", square_root)
elif num4 % 3 == 0:
    cube_root = num4**3
    print("cube root of the num4 value is: ", cube_root)

# program to describe the interview process.

'''
Take two variables input from user round1 and round2 and assign the interview result as passed or failed.

If condition checks, if round1 is passed then the candidate, can appear for round2. If  round2 is also passed then the candidate will be considered as placed.

If a candidate failed in the first round1 then he can not appear for round2.'''

round1 = input("enter the round1 result: ")
round2 = input("enter the round2 result: ")

if round1 == "passed":
    print("candidate can appear for 2nd round")
    if round2 == "passed":
        print("congratulation, you have selected")
    else:
        print("Sorry, not cleared 2nd round. better luck next time")
else:
    print("sorry, not cleared 1st round. better luck next time")

# program to determine whether a given number is available in the list of numbers or not.
l1 = [1,2,3,4]
print(l1, type(l1))
num5 = int(input("Enter any number from the list: "))

if num5 in l1:
    print("Given number is present in the list")
else:
    print("Given number is not present in the list")

#program to check any person eligible to vote or not

Age = int(input("Enter your age: "))
if Age >= 18:
    print("You are eligible to vote casting")
else:
    print("you are not eligible to vote cast")



