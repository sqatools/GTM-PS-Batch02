
#21.Python program to check whether the given number is positive or negative and even or odd.
Num1 = int(input("Enter a Number : "))

if Num1 > 0:
    if Num1%2==0:
        print("The given is positive and even")
    else:
        print("The given is positive and odd")
else:
    if Num1 % 2==0:
        print("The given is negative and even")
    else:
        print("The given is negative and odd")

print('*'*70)

#22). Python program to print the largest number from two numbers.

a = int(input("Enter a Number : "))
b = int(input("Enter another Number : "))

if a > b:
    print(f"{a} is the largest")
else:
    print(f"{b} is the largest")

print('*'*70)
#23). Python program to check whether a given character is uppercase or not.

Str = input("Enter a Character : ")
if Str.isupper():
    print(Str.isupper())
else:
    print(Str.isupper())

print('*'*70)
#24.Python program to check whether the given character is lowercase or not.

str1 = input("Enter a Character : ")
if str1.islower():
    print(str1.islower())
else:
    print(str1.islower())

print('*'*70)


#25). Python program to check whether the given number is an integer or not.

Val1 = 78

if type(Val1) == int:
    print("True")
else:
    print("False")

print('*'*70)

#26.Python program to check whether the given number is float or not.

Num = 34.56

if type(Num) == float:
    print("True")
else:
    print("False")

print('*'*70)


#27.Python program to check whether the given input is a string or not.

Str2 = "sqatools"

if type(Str2) == str:
    print("True")
else:
    print("False")

print('*'*70)


#28.Python program to print all the numbers from 10-15 except 13.


for num in range(10,16):

    if num != 13:
        print(num)

print('*'*70)


#29). Python program to find the electricity bill. According to the following conditions:

Unit = int(input("Enter the units : "))
bill = 0

if Unit <= 50:
    bill = Unit * 0.50
    print("Total bill : ",bill)
elif Unit > 50 and Unit <= 100:
    bill = Unit * 0.75
    print("Total bill : ",bill)
elif Unit > 100 and Unit <= 250:
    bill=Unit * 1.25
    print("Total bill : ",bill)
elif Unit > 250:
    bill = Unit * 1.50
    print("Total bill : ",bill)

Sur = bill*0.17
print("Total Electricity Bill : ",bill+Sur)


print('*'*70)


#30). Python program to check whether a given year is a leap or not.

Year = int(input("Enter a Year: "))

if (Year%400==0 or Year%100 !=0) and Year%4==0:
    print(f"{Year} is a leap year")
else:
    print(f"{Year} is not a leap year")

print('*'*70)
