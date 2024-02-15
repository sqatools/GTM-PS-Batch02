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

