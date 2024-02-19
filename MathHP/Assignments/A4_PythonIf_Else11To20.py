################ Assignment 4

# If Else Programs
#### 11)Python program to print a square or cube if the given number is divided by 2 or 3 respectively

num = int(input("Enter any number :"))
if num%2 == 0 or num%3 == 0:
    print("Square of the number :" ,num**2)          # ** power ^2
    print("Cube of the number   :" ,num**3)
else:
    print("The given number is not divisible by either 2 or 3")

#### 12)Python program to describe the interview process

round1 = input("Enter the result as 'Pass' or 'Fail'")
round2 = input("Enter the result as 'Pass' or 'Fail'")
if round1 == "Pass":
    print("Congrats , The person has cleared the 1st round")
    if round2 == "Pass":
        print("The person has cleared the 2nd round and selected , Congrats")
    else:
        print("The person has not cleared the 2nd round and try next time")
else:
    print("Failed in 1st round and Better luck next time")

#### 13)Python program to determine whether a given number is available in the list of numbers or not

listOfNumbers = [10,20,30,40,50,60,70,80,90,100]
num = int(input("Enter any number to check:"))
if num in listOfNumbers:
    print(f"{num} The entered number is in the list")                            # f formatting of the String
else:
    print(f"{num} The entered number is not in the list")

#### 14)Python program to find the largest number among three numbers

a = int(input("Enter the first  number"))
b = int(input("Enter the second  number"))
c = int(input("Enter the third number"))
if a>b and a>c:
    print(f"{a} is the largest")
else:
    print(f"{a} is not the largest")
if b>a and b>c:
    print(f"{b} is the largest")
else:
    print(f"{b} is not the largest")
if c>a and c>b:
    print(f"{c} is the largest")
else:
    print(f"{c} is not the largest")

#### 15)Python program to check any person eligible to vote or not
# age > 18+ : eligible
# age < 18: not eligible

age = int(input("Enter any age to check the eligibility to vote"))
if age > 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")

#### 16)  Python program to check whether any given number is a palindrome.
# Input: 121
# Output: palindrome

num = int(input("Enter any number to check palindrome"))
num1 = num
reverse = 0
while num>0:
    temp = num%10                                               # to extract last digit 1
    reverse = reverse*10 +temp                                  # reverse = 1
    num = num//10                                               # ignores last digit 1
if reverse == num1:
    print("The given number is palindrome :" ,num1)
else:
    print("The given number is not  palindrome :", num1)

#### 17)Python program to check if any given string is palindrome or not.
# Input: ‘jaj’
# output = palindrome

str1 = "MOM"
length = len(str1)
print("Length of the given String :",length)
reversed_String = str1[2] + str1[1] +str1[0]
print("Reversed String is :" ,reversed_String)
if str1 == reversed_String:
    print("The given String is a Palindrome",str1)
else:
    print("The given String is not a Palindrome" ,str1)

#### 18)Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
# Input = Enter marks: 45
# Output = Pass

marks = int(input("Enter the student's marks :"))
if marks>35:
    print("Student passed")
else:
    print("Student failed")

#### 19)Python program to check whether the given number is positive or not.
# Input = 20
# Output = True

number = int(input("Enter any number:"))
if number == 0:
    print("The given number is neither positive nor negative")
elif number>0:
    print("The given number is positive:" ,number)
else:
    print("The given  number is negative :", number)

#### 20)Python program to check whether the given number is negative or not.
# Input = -45
# Output = True

number2 = int(input("Enter any number"))
if number2 == 0:
    print("The given number is neither positive nor negative" ,number2)
elif number2 <0:
    print("The given number is negative" ,number2)
else:
    print("The given number is positive" ,number2)






