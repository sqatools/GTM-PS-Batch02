# range (initial value, end value, step)
for i in range(5, 10, 1):
    print(i)
# range with two parameters
# range (initial value, end value)
for i in (5 ,10):
    print(i)
print("-"*50)
for i in (1,10):
    print(i)
# range with one parameter : range(last value)

# default initial value will 0 and difference value will be 1
print("_"*50)
for j in range(5):
     print(j)
     print("*" * 5)
# Program to print multiplication table
num = input("Enter a number :")
for i in range(0,13,1):
    print(i , "*", num,"=", i*int(num))
print("-"*50)
# Program to print values in reverse order
num = int(input("Enter a number :"))
for i in range(num, 0, -1):
    print(i)
print("_"*50)
# Program to print all the even numbers from 1 to 100
for i in range(0 , 50 ,2):
    print(i)
print("_"*50)
for i in range(50 , 0 , -2):
    print(i)
print("_"*50)
print("Even numbers ")
for i in range(1, 50):
    if i%2 == 0:
        print(i)

print("_"*50)
# Program to find the factorial of a given number
num = int(input("Enter a number to find the factorial :"))
for i in range(1, num):
    num= i*num
print("Factorial : ", num)

# get factorial of any given number
# # factorial of 5 : 5*4*3*2*1 = 120
fact = 1
num = int(input("Enter a number to get the factorial :"))
for i in range(num, 0, -1):
    fact = fact*i # 5, 20, 60, 120
#     #i=5, 1*5 = 5
#     #i=4, 5*4 = 20
#     #i=3, 20*3 = 60
#     # i=2, 60*2 = 120
#     #i=1, 120*1 = 120
print("Factorial output :", fact)

print("_"*50)
 ### Continue and break condition

for i in range(10):
    if i >= 5 and i <=8:
        continue
    print(i)
#Break statement
print("_"*50)

for i in range(10):
    if i == 6:
       break
    print(i)
print("_"*50)
# Palindrome number
num = 12321
rev_num = str(num)[::-1]
print("Reverse Number :", rev_num)


w = "abcdefghij"
rev_w = w[::-1]
print("Reverse string :",rev_w)

# # find out the palimdrop number and check its output.
# print("_"*50)
num1 = 12345654321
rev_num1 = str(num1)[::-1]

print("###",rev_num1)
if num1 == int(rev_num1):
    print("This number is palimdrome")
else:
    print("This number is not a palimdrome")
# Query question:



var1 = '40'
print(type(var1))
if isinstance(var1, int):
    print("This is an integer")
else:
    print("This is not an integer")
if isinstance(var1, str):
    print("It's a string!")
else:
    print("It's not a string!")

# apply loop on the list
input_values = [1, "cat", "dog", True, 10, 6.7, [4, 6, 7]]
for data in input_values:
    print(data)
    if isinstance(data, bool):
       print("this is bool value :", data)
    elif isinstance(data, str):
        print("Its a string :", data)
    elif isinstance(data, float):
        print("It's a float value:", data)
    elif isinstance(data, list):
        print("It's a list :", data)
    elif isinstance(data, int):
        print("It's an int :")


# Apply loop on the string
# Remove all the vowels from the string
print("_"*50)
str1 = "Hello, Good MOrning 567"
vowels = ['a','i','e','o','u','A','E','I','O','U']

result = ""
for char in str1: # Hel
    print(char)
    if char in vowels:
       continue
    else:
        result = result + char # ""+H = H | H + l = Hl
    print("Result =", result)
print(dir(str))

# # apply loop on tuple:
# # Add all number from given tuple.
print("_"*50)
tup1 = (5, 7, 'Hello', (4, 7, 9), 7, 9)
sum = 0
for a in tup1:
    if isinstance(a, int):
        sum = sum +a
    else:
        continue
print("Sum of all integers in the tuple :", sum)


# Apply loop on dictionary
print("_"*50)
dict1 = {'a' : 123, 'b' : 345, 'c' : {'e' : {'f' : 456}}}

for val in dict1.items():
    print(val)

# apply loop on set
set1 = {50, 60, 70, 80}
for val in set1:
    print(val**2, end=" ")
