print("Priyanka")
#print("Priyanka")

# if else
num1 = 10
num2 = 20
if num1 == num2:
    print("Both variables have same values")
else:
    print("values are not same")

print("-"*50)

UserName = "priya"
PW = "test"

input_username = input("Enter user name: ")
input_PW = input("Enter Pass word: ")

if UserName == input_username and PW == input_PW:
    print("Login Successful")
else:
    print("Wrong username and password")

# for loop
for i in range(1, 5, 1):
    print(i)
"""
1
2
3
4
"""

for i in range(1, 6, 1):
    print("*"*i)

for i in range(1, 6, 1):
    for j in range(i):
        print("*", end=" ")
    print()
"""
*
**
***
****
***** """
print("#"*20)
for i in range(5, 0, -1):
    print("*"*i)
"""
*****
****
***
**
*
"""

temp = 65
for i in range (1,8):
    for j in range (i):
        print(chr(temp), end=" ")
        temp +=1
    print()
"""
A 
B C 
D E F 
G H I J 
K L M N O 
P Q R S T U 
V W X Y Z [ \ 
"""

# range with one parameter : range(last value)
# default initial value will 0 and difference value will be 1
print("_"*50)
for j in range(1, 10):
    print(j*5) # prints 5 ones tables

str1 = "Good morning"
vowels = "aeiou"
result = ""
for char in str1:
    print(char)
    if char in vowels:
        continue
    else:
        result = result+char
print("results: ", result)

# while
n = 1
while n <= 10:
    print(n)
    n += 1

num = 24587
rev = 0
while num > 0:
    temp = num % 10
    rev = rev * 10 + temp
    num = num // 10
print(rev)

for i in range(0,9):
    for j in range(0,9):
        if i == 0 or i == 1:
            print("*", end=" ")
        elif 2 < j < 6:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

