# Python program to print a combination of 2 elements from the list whose sum is 10

comb_list= [2, 5, 8, 5, 1, 9]
output = []
for i in range(len(comb_list)):
    for j in range(i+1, len(comb_list)):
        #combination = sum(comb_list[i],comb_list[j])
        combination = comb_list[i] + comb_list[j]
        if combination == 10:
            output.append((comb_list[i], comb_list[j]))
print("_"*100)

print("output :", output)

# program to get sum of digit
"""
n= input("enter the numbers :")
sum=0
for i in n:
    print(i, type(i))
    sum=sum+int(i)
print(sum) # 29

# print reverse of the number
num = input("please the number :")
print(num[::-1])

n = int(input("Please enter the number to reverse :")) # 234//10 =
reverse = 0

while n > 0:
    temp = n%10 # 4, 3, 2
    reverse = reverse*10 + temp # 4 | 4*10 + 3 = 43 | 43*10 + 2 = 432
    n = n//10 # 23, 2

print(" reverse output :", reverse)
"""

print("_"*50)
####################################################
# 1)Print most simultaneously repeated characters in the input string

str1 = "Hello we aaare leeeearning Python Programming"

count = 1
max_count = 0
max_r_char = ''

for i in range(len(str1)-1):
    if str1[i] == str1[i+1]:
        count += 1
        if count > max_count:
            max_count = count
            max_r_char = str1[i]
            print("max", max_count, max_r_char)
    else:
        count = 1

print("max count :", max_count)
print("max repeated character :", max_r_char)
