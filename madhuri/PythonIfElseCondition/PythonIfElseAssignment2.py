"""
    11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
"""
num1 = int(input("Enter Number divided by 2 or 3: "))
if (num1 % 2 ) ==0:
    print("Number is divisible by 2 : Sqaure of: ",num1, '=', num1**2)
elif (num1 % 3 == 0):
    print("Number is divisible by 3 : Cube of: ",num1, '=', num1**3)
else:
    print("Number is not divisible by 2 nor by 3")

"""
 12). Python program to describe the interview process.
"""

"""
13.Python program to determine whether a given number is available in the list of numbers or not.
"""
input_list = [10,20,30,40,50,60,78,8899]
num2 = int(input("Enter Number to check present in list or not: "))

if num2 in input_list:
    print("Present in list")
else:
    print("Not Present in list")


