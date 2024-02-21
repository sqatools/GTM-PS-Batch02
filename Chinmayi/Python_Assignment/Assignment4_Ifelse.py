#11.Python program to print a square or cube if the given number is divided by 2 or 3 respectively.

Var1=int(input("Enter a number : "))

if Var1 % 2 == 0:
    print("Square :", Var1**2 )
elif Var1 % 3 == 0:
    print("Cube:", Var1**3 )
else:
    print("Given Number is not divisible by 2 or 3")

print('*'*70)

#12). Python program to describe the interview process.

round1 = input("Enter round 1 Result : ")
round2 = input("Enter round 2 Result : ")

if round1 == "Passed":
    print("Round1 is cleared")
    if round2 == "Passed":
        print("Round 2 is cleared")
        print("Congratulations you are selected")
    else:
        print("Sorry you are not selected for round 2")
        print("Please try next time")
else:
    print("Round 1 is not Clered")
    print("Please try next time")

#13. Python program to determine whether a given number is available in the list of numbers or not.

List1 = [1,45,67,89,43,90,25,78]

Num1 = int(input("Enter a Number : "))
if Num1 in List1:
    print("Given number is in the list")
else:
    print("Given number is not in the list")

print('*'*70)


#14. Python program to find the largest number among three numbers.

Num1 = int(input("Enter first Number : "))
Num2 = int(input("Enter second Number : "))
Num3 = int(input("Enter third Number : "))

if Num1>Num2 and Num1>Num3:
    print(Num1,"It is the largest Number")
elif Num2>Num1 and Num2>Num3:
    print(Num2,"It is the largest Number")
else:
    print(Num3,"It is the largest Number")

print('*'*70)

#15). Python program to check any person eligible to vote or not.

Age1 = int(input("Enter your Age : "))

if Age1 >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

print('*'*70)

#16.Python program to check whether any given number is a palindrome.

Num = 12121
Num1 = Num
Length = len(str(Num))
reverse = 0

while Num > 0:
     temp = Num%10
     reverse = reverse * 10 + temp
     Num = Num//10
print("Number:",Num1)
print("Reverse value:",reverse)

if reverse == Num1:
    print("Given number is Palindrome")
else:
    print("Given number is not a palindrome")

print('*'*70)


#17.Python program to check if any given string is palindrome or not

Str1 = 'jaj'
Str2 = Str1[::-1]

if Str1 == Str2:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")

print('*'*70)


#18. Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.

Mark1 = float(input("Enter Marks : "))

if Mark1 > 35:
    print("Passed")
else:
    print("failed")

print('*'*70)


#19. Python program to check whether the given number is positive or not.

Num1 = int(input("Enter a Number : "))

if Num1 > 0:
    print("True")
else:
    print("False")

print('*'*70)

#20). Python program to check whether the given number is negative or not.

Num1 = int(input("Enter a Number : "))

if Num1 < 0:
    print("True")
else:
    print("False")

print('*'*70)


