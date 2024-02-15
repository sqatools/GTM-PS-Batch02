
"""
Take a list of all the numbers in a Fibonacci series from 0-10.
Take a number as input through the user.
Use if-else statement to check whether the given number is a part of the Fibonacci series or not.
Print the output.
"""

li =[1, 1, 2, 3, 5, 8]
num = int(input("Enter a number less than 10 :"))
fb = 0
if num in li:
    print("Number %s is a part of the Fibonacci series from 1 to 10" % num)
else:
    print("Number %s is not a part of the Fibonacci series from 1 to 10" % num)



