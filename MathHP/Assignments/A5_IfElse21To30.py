####################### Assignment 5    ####################

# Python If_Else
# 21)Python program to check whether the given number is positive or negative and even or odd.
# Input = 26
# Output = The given number is positive and even

num = int(input("Enter any number"))       # Getting the user's input
if num%2==0:
    print("The given number is even")
    if num>0:
        print("The given number is positive, hence even and positive")
    else:
        print("The given number is negative , hence even and negative")
else:
    print("The given number is not even, which is odd")
    if num>0:
        print("The given number is positive, hence odd and positive")
    else:
        print("The given number is negative, hence odd and negative")


# 22)Python program to print the largest number from two numbers.
# Input:
# 25, 63
# Output = 63

a = 25
b = 63
if a>b:
    print(f"{a}  is the larger number than {b}")                      # f formatting in String
else:
    print(f"{b}  is the larger number than {a}")

# 23) Python program to check whether a given character is uppercase or not.
# Input = A
# Output = The given character is an Uppercase

alpha = input("Enter any alphabet")
if ord(alpha)>=65 and ord(alpha)<=90:                                 # ord(char)=65 , chr(90)=Z
    print("The entered alphabet is in Upper Case")
else:
    print("The entered alphabet is in Lower Case")

# 23) Other Way

alpha = input("Enter any alphabet")
if alpha.isupper():                                                  # isupper() is a method to check whether given alphabet is upper
    print("True")
else:
    print("False")

# 24) Python program to check whether the given character is lowercase or not.
# Input = c
# Output = True

character = input("Enter any alphabet")
if character.islower():                                              #islower() is a method to check whether given alphabet is in lowercase
    print("True")
else:
    print("False")

# 25)Python program to check whether the given number is an integer or not.
# Input = 54
# Output = True

num = 54
if num.is_integer():                                               # is_integer() is applicable only for integer numbers
    print("True")                                                  # if you are taking user's input , then pass the value inside parameters
else:
    print("False")

# Other Way
num = 86
if type(num)==int:
    print("True")
else:
    print("False")

# 26) Python program to check whether the given number is float or not.
# Input = 12.6
# Output = True

input = 12.6
if type(input)==float:
    print("True")
else:
    print("False")

#27) Python program to check whether the given input is a string or not.
# Input = ‘sqatools’
# Output = True

Input = "sqatools"
if type(Input)==str:                # Don't do string its only str
    print("True")
else:
    print("False")

#28)Python program to print all the numbers from 10-15 except 13
# Output:
# 10
# 11
# 12
# 14

for i in range(10, 16):             # starts with initial index and prints until last index -1
    if i == 13:
        continue                    # Skips 13 only
    print(i)

#29)Python program to find the electricity bill. According to the following conditions:
# Up to 50 units rs 0.50/unit
# Up to 100 units rs 0.75/unit
# Up to 250 units rs 1.25/unit
# above 250 rs 1.50/unit
# an additional surcharge of 17% is added to the bill
# Input = 350
# Output = 438.75

units_consumed = int(input("Enter number of units consumed"))
bill_amount =0

for billunit in range(1,units_consumed+1):
    if billunit <=50:
        bill_amount =  bill_amount+ 0.50
    elif billunit>50 and billunit<=100:
        bill_amount =  bill_amount+0.75
    elif billunit>100 and billunit <=250:
        bill_amount = bill_amount +1.25
    elif billunit >250:
        bill_amount = bill_amount +1.50
bill_surcharge = bill_amount+bill_amount*(17/100)
print("Bill amount with surcharge :", bill_surcharge)


#30)Python program to check whether a given year is a leap or not.
# Input = 2000
# Output = The given year is a leap year

year = int(input("Enter any year"))
if year%4==0 and (year%100!=0 or year%400==0):
    print("The given year is a leap year")
else:
    print("The given year is not a leap year")

## Year divisible by 4
## Year not divisible by 100 OR
## Year divisible by 400










