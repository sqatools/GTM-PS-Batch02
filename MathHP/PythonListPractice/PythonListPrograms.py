# Python program to print a combination of 2 elements from the list whose sum is 10.

list1 = [2,9,8,1,3,7,4,6]
output =[]
for i in range(len(list1)):                       # range 0 to length-1  , 0 to 7
    for j in range(i+1,len(list1)):
        combination = list1[i]+list1[j]
        if combination == 10:
            output.append((list1[i],list1[j]))        #Output: [(2, 8), (9, 1), (3, 7), (4, 6)]
print("_"*100)
print("Output:",output)

# Program to get sum of digits in a given number

num = (input("Enter any number:"))           #TypeError: unsupported operand type(s) for +: 'int' and 'str'
sum=0
for  i in num:                             # If num is int , then cant apply loop on integer, not on sinle digit
    print(i,type(i))
    sum = sum+int(i)                     # While getting the users input give number without space
print(sum)

# Enter any number:245
# 2 <class 'str'>
# 4 <class 'str'>
# 5 <class 'str'>
# 11

# By default input values are String so should do int(input)
#for i in num:
#TypeError: 'int' object is not iterable

# Program to reverse the number

num = int(input("Enter any number:"))                      #345
reverse = 0
while num>0:
    temp = num%10                                         # 5 remainder
    reverse = reverse*10+temp                             # 0*10 + 5 = 5
    num = num//10                                          # 345/10 = 34 , ignores last digit and process repeats
print("Reverse:",reverse)

# / decimal quotient // integer quotient

print("__"*60)
########################################################

#1) Print most simultaneously repeated characters in the input String

str1 = "Hello we aaare leeeearning Python Programming"

count = 1
max_count =0
max_r_char = ''

for i in range(len(str1)-1):                   # index 0 starting from 1st char and end until before last char
    if str1[i] == str1[i+1]:                  # 1st char check with 2nd char
        count += 1
        if count > max_count:
            max_count=count
            max_r_char=str1[i]               # repeated character
            print("max",max_count,max_r_char)
    else:
        count =1                            # If no repeated char , then the count is same 1 not increased

print("max count:",max_count)
print("max repeated character:",max_r_char)

# WAP to get all the number which are divisible by either 3  or 7 from given list

list1 = [4, 6, 7, 8, 15, 21, 35, 40, 18, 28]
output =[]
for val in list1:
    if val%3==0 or val%7==0:
        output.append(val)
    else:
        output.append(None)                                                  # None is blank
print("Output:",output)

####### Using list comprehension, can do for String,numbers and tuple  as well

result = [val if val%3==0 or val%7==0 else None for val in list1]            # if else means extreme leftmost , for right
print("Result:",result)


# 21)Write a Python to remove unwanted characters from the given string

Input_val = "Prog^ra*m#ming"
# To get output Programming

result = [char  for char in Input_val if char.isalpha()]               # if character is an alphabet then print the alphabet
print("Result:",result)
print("Output:" ,"".join(result))











