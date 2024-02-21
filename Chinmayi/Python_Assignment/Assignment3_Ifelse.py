# 1.Program to check if a number is divisible by 3

Var1 = int(input("Enter a Number "))

if Var1 % 3 == 0:
    print(Var1, " Is divisible by 3")
else:
    print(Var1, "Not divisible by 3")

print('*' * 70)

# 2.If else program to get all the numbers divided by 3 from 1 to 30.

for i in range(1, 31, 1):
    if i % 3 == 0:
        print(i, "Divisible by 3")

print('*' * 70)

# 3.If else program to assign grades as per total marks

marks > 40: Fail
marks
40 – 50: grade
C
marks
50 – 60: grade
B
marks
60 – 70: grade
A
marks
70 – 80: grade
A +
marks
80 – 90: grade
A + +
marks
90 – 100: grade
Excellent
marks > 100: Invalid
marks

marks = float(input("Please enter Marks :"))

if marks >= 40 and marks <= 50:
    print("Student got Grade 'C'")
elif marks > 50 and marks <= 60:
    print("Student got Grade 'B'")
elif marks > 60 and marks <= 70:
    print("Student got Grade 'A'")
elif marks > 70 and marks <= 80:
    print("Student got Grade 'A+'")
elif marks > 80 and marks <= 90:
    print("Student got Grade 'A++'")
elif marks > 90 and marks <= 100:
    print("Student got Grade 'Excellent'")
elif marks > 100:
    print("Marks are invalid")
else:
    print("Student is failed")

print('*' * 70)

# 4.Python program to check the given number divided by 3 and 5.

X = float(input("Enter a Number"))

if X % 3 == 0 and X % 5 == 0:
    print(X, "Is divisible by 3 and 5")
else:
    print(X, "Is not divisible by 3 and 5")

print('*' * 70)

# 5.Python program to print the square of the number if it is divided by 11.

Num1 = float(input("Enter a number :"))

if Num1 % 11 == 0:
    print((Num1 ** 2))
else:
    print("Given number is not divisible by 11")

print('*' * 70)

# 6.Python program to check given number is a prime number or not.

Num1 = int(input("Enter a Number: "))

Var1 = 0
for i in range(2, Num1):
    if Num1 % i == 0:
        Var1 += 1
if Var1 > 0:
    print("Not a Prime Number")
else:
    print("It's a Prime Number")

print('*' * 70)

# 7). Python program to check given number is odd or even.

Num1 = int(input("Enter a Number: "))

if Num1 % 2 == 0:
    print("It's an Even Number")
else:
    print("It's a Odd Number")

print('*' * 70)

# 8.Python program to check a given number is part of the Fibonacci series from 1 to 10.

Fib1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

Num1 = int(input("Enter a Number :"))
if Num1 in Fib1:
    print("Given number is a part of fibonacci Series")
else:
    print("Given number is not a part of fibonacci Series")

print('*' * 70)

# 9). Python program to check authentication with the given username and password.

UserId = "User@1234"
Pass = "Pass@1234"

User1 = input("Enter the Username:")
Pass1 = input("Enter the Password:")

if User1 == UserId and Pass == Pass1:
    print("Login Successful")
else:
    print("login UnSuccessful")

print('*' * 70)

# 10). Python program to validate user_id in the list of user_ids.

User_id = ["UserId1", "User@123", "User321", "User@1", "User@2"]

User1 = input("Enter the User_id:")

if User1 in User_id:
    print("UserId is valid")
else:
    print("UserId is invalid")

print('*' * 70)
