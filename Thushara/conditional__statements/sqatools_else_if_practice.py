

"""
Use for loop with the range function to iterate over numbers from 1-30.
Using if else statement check whether a  number is divisible by 3 or not.
If it is divisible by 3 then print the number.
"""

for i in range(0, 30):
    if i % 3 == 0:
        print(i)

print("_"*50)
"""
Take a number as input through the user.
Use if-else statements to check whether the given number is divisible by 3 and 5 also.
If yes then then print True, if not then print False.
"""
print("Program to check if a number is divisible by both 3 and 5")
num = int(input("Enter a number  :"))

if num % 3 == 0 and num % 5 == 0:
    print(" Number is divisible by both 3 and 5")
else:
    print("The given number " + str(num) + "is not divisible by 3 and 5")

"""
Take a number as input through the user.
Use an if-else statement to check whether the given number is divisible by 11 or not.
If yes then print its square.
Else print False.
"""
print("-"*50)
print("Program to find the square of a number if its divisible by 11.")
number = int((input("Enter a number :")))
if number % 11 == 0:
    print("The square of ",number ,"is",(number**2))
else:
    print("Number is not divisible by 11")

print("_"*50)

"""
Take a number as input through the user and create a variable count and assign its value equal to 0.
Use for loop with the range function to iterate over 2 to the given number.
During the iteration check if any number divided the given number then add 1 to the count variable using if-else statement.
If value of the count variable is  greater then 0 then it is not a prime number.
"""
print("Program to check a number is prime")
num = int(input("Enter a number :"))
ct = 0
for i in range(2,num):
    if num%i == 0:
        ct = ct + 1
if ct == 0:
    print(" %s is prime" % num)
else:
    print("%s is not prime" % num)
"""
prime = False
for i in range(2, num-1):
    if num % i != 0:
        prime = True
    else:
        prime = False
        break
if prime:
    print("The number: %s is prime" % num)
else:
    print("The number: %s is not prime" % num)


"""
"""
Take the number as input through the user.
Using an if-else statement check whether the given number is odd or even.
If the number is divisible by 2 then it is even else odd.
Print respective output.
"""
print("*"*50)
print("Program to check given number is odd or even")
num = int(input("Enter a number :"))
if num % 2 == 0:
    print("The given number is even!")
else:
    print("The given number is odd!")
