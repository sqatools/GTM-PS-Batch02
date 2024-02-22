"""
--Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
--Python program to describe the interview process.
--Python program to determine whether a given number is available in the list of numbers or not.
--Python program to find the largest number among three numbers.
--Python program to check any person eligible to vote or not
age > 18+ : eligible
age < 18: not eligible
-- Python program to check whether any given number is a palindrome.
Input: 121
Output: palindrome
--- Python program to check if any given string is palindrome or not.
Input: ‘jaj’
output = palindrome
---Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
Input = Enter marks: 45
Output = Pass
-- Python program to check whether the given number is positive or not.
Input = 20
Output = True
---Python program to check whether the given number is negative or not.
Input = -45
Output = True

"""

#Python program to print a square or cube if the given number is divided by 2 or 3 respectively.

number=int(input("enter the number:"))

if number%2 ==0 :
    print(number**2,"square of the number")
elif number%3==0:
    print(number**3,"cube of the number")
else:
    print(number,"neither divided by 2 nor 3")
#
# #-Python program to describe the interview process.

round1 = "Cleared"
round2 = "Cleared"
round3 = "Got opportunity"

if round1 == "Cleared":
    print("Congratulation first round is clear")
    if round2 == "Cleared":
        print("Congratulation 2nd round is also clear")
        if round3 == "Got opportunity":
            print("Congratulation you are placed")
        else:
            print("Failed in 3rd round better luck next time")
    else:
        print("sorry, you are failed in 2nd round")
else:
    print("sorry, you are failed in first round")
#
# #-Python program to determine whether a given number is available in the list of numbers or not.

list=[1,2,3,4,5,6,7,8,9,23,25]

list_1= int(input("enter the number"))

if list_1 in list:
    print(list_1,"is available in list")
else:
    print(list_1,"no not available in list")

#-Python program to find the largest number among three numbers.

n = str(input("enter the three number:"))

if max(n) in n:
    print ("First digit of number:",max(n))
else:
    print("its not the largest number")

#--Python program to check any person eligible to vote or not
#age > 18+ : eligible
#age < 18: not eligible

age =int(input("enter the age:"))
if age< 18 :
    print("Not Eligible for Vote")
else:
    print("Eligible for Vote")
#
# # -- Python program to check whether any given number is a palindrome.
# # Input: 121
# # Output: palindrome

number = int(input("enter the number:"))
reverse_number = str(number)[::-1]
print(reverse_number)


if int(reverse_number) == number:
    print("Palindrome Number")
else:
    print("Not palindrome number")
#
# # --- Python program to check if any given string is palindrome or not.
# Input: ‘jaj’
# output = palindrome

str = input("enter the text:")
reverse_str = str[::-1]


if (reverse_str) == str:
    print("Palindrome string")
else:
    print("Not palindrome string")
#
# #---Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
#Input = Enter marks: 45
#Output = Pass

print("_"*50)

marks=int(input("Please enter the value:"))

if marks<35:
    print("fail")
elif marks>=35 and marks < 50:
    print("Pass")
else:
    print("marks not exceeded than 100")

# #-- Python program to check whether the given number is positive or not.
# #Input = 20
# #Output = True

num=int(input("Please enter the value:"))

if num>0:
    print("True")
else:
    print("false")


#Python program to check whether the given number is negative or not.
#Input = -45
#Output = True

num=int(input("Please enter the value:"))

if num<0:
    print("True")
else:
    print("false")