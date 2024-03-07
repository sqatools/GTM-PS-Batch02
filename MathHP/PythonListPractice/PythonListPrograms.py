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










