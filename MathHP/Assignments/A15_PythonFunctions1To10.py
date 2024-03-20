########### Python Function Programs ###################

# 1). Python function program to add two numbers.

def addition(val1,val2):
    val3 = val1+val2
    print("Addition:",val3)

addition(60,50)

# 1). Python function program to add two numbers , taking user's input

def add(a,b):
    total=a+b
    print("Addition:",total)

# a = int(input("Enter number1"))
# b = int(input("Enter number2"))
#add(a,b)

##################################################################################

# 2). Python function program to print the input string 10 times.

str1 = "Hello I'm a string"
def timesten(str1):
    print("Printing 10 times :",str1*10)

timesten(str1)

# 2). Python function program to print the input string 10 times, getting input from the user

def tentimes(str1):
    print(str1*10)

# s = input("Enter any string")
# tentimes(s)

#######################################################################################################

# 3). Python function program to print a table of a given number.

def table(num):
    for i in range(1,13):
     print(num, "*" ,i ,"=" ,num*i)

table(6)

# n=int(input("Enter any number"))
# table(n)

#########################################################################################################

# 4). Python function program to find the maximum of three numbers.

# Input: 17, 21, -9
# Output: 21

def maxfunction(a,b,c):
    if a>b and a>c:
        print(a , "is the maximum")                            # elif whichever is first true will get executed
    elif b>a and b>c:
        print(b, "is the maximum" )
    else:
        print(c, "is the maximum" )

maxfunction(17,21,-9)

# a = int(input("Enter the first number"))
# b = int(input("Enter the second number"))
# c = int(input("Enter the third number"))
# maxfunction(a,b,c)

#########################################################################################################

# 5). Python function program to find the sum of all the numbers in a list.
# Input : [6,9,4,5,3]
# Output: 27

def sumfunction(a,b,c,d,e):
    print("Sum of all numbers:" ,a+b+c+d+e)

sumfunction(6,9,4,5,3)

# 5). Python function program to find the sum of all the numbers in a list.

def total(list):
    t=0                                                           # initially t=0
    for val in list:
        t = t+val                                                # t += val
    print("Total of all numbers in the list:",t )               # print must follow intendation with for

#list = int(input("Enter numbers in the list"))                # ValueError: invalid literal for int() with base 10: ' [1,2,3,4,5,6,7]'
# Can't enter list in place of integers

l = [7,8,9,10,11,12,13]
total(l)

##############################################################################################################

# 6). Python function program to multiply all the numbers in a list.
# Input : [-8, 6, 1, 9, 2]
# Output: -864

def multiplyNumbers(list):
    p=1                                                  # initially product = 1
    for val in list:
        p = p*val                                       # p *= val
    print("Multiplication of all numbers :", p)

#l = [1,2,3,4,5,6]
l=[-8,6,1,9,2]
multiplyNumbers(l)

##############################################################################################################

# 7). Python function program to reverse a string.
# Input: Python1234
# Output: 4321nohtyp

def reverse(str1):
    a = str1[::-1]                                    # -1 is the default index starting from end
    print("Reverse of a string:" ,a)

s = "Python1234"
reverse(s)

################################################################################################################

# 8). Python function program to check whether a number is in a given range.
# Input : num = 7, range = 2 to 20
# Output: 7 is in the range

def numberInRange(num):
    if num in range(2,21):
         print("Number is within the range","True")
    else:
        print("Number is not within the range:","False")


#numberInRange(7)                       # Number is within the range True
numberInRange(22)                      # Number is not within the range: False

################################################################################################################

# 9). Python function program that takes a list and returns a new list with unique elements of the first list.
# Input : [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
# Output : [2, 3, 1, 4, 6 ]

def uniqueNumber(list):
    unique = set(list)                                          # Set always removes duplicates
    print("Remove duplicates:",unique)                         # Remove duplicates: {1, 2, 3, 4, 6}

list = [2,2,3,1,4,4,4,4,4,6]
uniqueNumber(list)


#################################################################################################################

# 10). Python function program that take a number as a parameter and checks whether the number is prime or not.
# Input : 7
# Output : True

def primeNumberFunction(num):
    count=0
    for i in range(2,num):        # prime number is  divisible by only numbers 1 and itself, range is num means before that num-1
       if num % i == 0:
           count = count+1

    if count>0:
         print(num, "is not prime")
    else:
         print(num, "is prime")

primeNumberFunction(7)            # Can call function as many number of times
primeNumberFunction(13)
primeNumberFunction(22)








