# range(initial value, end value, different value)
# it will print the value till end_value - 1
for i in range(5, 10, 1):
    print(i)

# range with two parameter
# range(initial value, end value)
# default difference value is 1 and exclude last value.

for i in range(1, 10):
    print(i)

# range with one parameter : range(last value)
# default initial value will 0 and difference value will be 1
print("_"*50)
for j in range(5):
    print(j)
    print("*" * 5)

# write a program to print the table of any given number
print("_"*40)
num1 = 6
for i in range(1, 11):
    print(i, "*", num1, ":", i*num1)


# print values in reverse order
print("_"*50)
for i in range(10, 0, -1):
    print(i)

# check if condition in loop
# get all the even number from 1 to 50
print("_"*50)
for i in range(1, 50):
    if i%2 == 0:
        print(i)


# get factorial of any given number
# factorial of 5 : 5*4*3*2*1 = 120
fact = 1
num = 7

for i in range(num, 0, -1):
    fact = fact*i # 5, 20, 60, 120
    #i=5, 1*5 = 5
    #i=4, 5*4 = 20
    #i=3, 20*3 = 60
    # i=2, 60*2 = 120
    #i=1, 120*1 = 120

print("Factorial output :", fact)


print("_"*50)
### Continue and break condition

for i in range(10):
    if i >= 5 and i <=8:
        continue
    print(i)

# Break statement
print("_"*50)

for i in range(10):
    if i == 6:
        break
    print(i)



# find out the palimdrop number and check its output.
print("_"*50)
num1 = 565
rev_num = str(num1)[::-1]
print("rev_num :", rev_num)

if num1 == int(rev_num):
    print("This number is palimdrome")
else:
    print("This number is not a palimdrome")


# Query question:

# input_values = [1,"cat","dog", True, 10, 6.7, [4, 6, 7]]

# var1 = '40'
# print(type(var1))
#
# if isinstance(var1, int):
#     print("this is integer")
# else:
#     print("this is not integer")

# apply loop on the list
input_values = [1, "cat", "dog", True, 10, 6.7, [4, 6, 7]]
for data in input_values:
    print(data)
    if isinstance(data, bool):
        print("this is bool value :", data)
    elif isinstance(data, str):
        print("this is string value :", data)
    elif isinstance(data, float):
        print("this is float value :", data)
    elif isinstance(data, list):
        print("this is list value :", data)
    elif isinstance(data, int):
        print("this is int value :", data)


# apply loop on the string
# remove all the vowels from the string.
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

print("result :", result)

print(dir(str))


# apply loop on tuple:
# Add all number from given tuple.
print("_"*50)
tup1 = (5, 7, 'Hello', (4, 7, 9), 7, 9)
addition = 0
for a in tup1:
    if isinstance(a, int):
        print(a)
        addition = addition + a
    else:
        continue

print("addition output :", addition)


# Apply loop on dictionary
print("_"*50)
dict1 = {'a' : 123, 'b' : 345, 'c' : {'e' : {'f' : 456}}}

for val in dict1.items():
    print(val)

# apply loop on set
set1 = {50, 60, 70, 80}
for val in set1:
    print(val**2, end=" ")




