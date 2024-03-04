#### 22nd Feb 2024 #######

list1 = [12, 3.6, "Python", [3, 5,6], (4, 8, 2), {'a': 123, 'b' : 567},
         {5, 8, 3}, True]

"""
Properties :
-> List is mutable data type, we can modify at any point of time.
-> List can contains all type of data.
-> List follows the positive and negative indexing as like string.
"""
print("list 1:", list1)
print(type(list1))
#########################################
# get the value from list
var1 = list1[2]
print("var1 :", var1)  # Python

var2 = list1[-4]
print("var2 :", var2) # (4, 8, 2)

print(list1[-4][1])  # 8
#########################################
# Apply loop on the list
print("_"*50)
lista = ['a','Hello', 'Python', 'Programming']

# get the values without index
for val in lista:
    print(val, end=" ")
# a Hello Python Programming
print()
################################
# get list values with indexing

for i in range(len(lista)):
    print(i, lista[i])

"""
0 a
1 Hello
2 Python
3 Programming
"""


################## slicing in the list #################
list1 = [4, 7, 9, 2, 8, 12]

print(list1[2:5])  # [9, 2, 8]

print(list1[1:-2])  # [7, 9, 2]

print(list1[-4:])  #  [9, 2, 8, 12]

lista = [5, 7, 'a', 'b', 'c', 'd', 33, 22, 14]
print(lista[2: 8: 1])  #  ['a', 'b', 'c', 'd', 33, 22]
print(lista[:3:-1])    #  [14, 22, 33, 'd', 'c']
print(lista[::-1])     #  [14, 22, 33, 'd', 'c', 'b', 'a', 7, 5]
print(lista[-5::-1])   #  ['c', 'b', 'a', 7, 5]
print(lista[-1::2])    #  [14]
print(lista[-7::2])    #  ['a', 'c', 33, 14]
print(lista[-1:-8:-2]) #  [14, 33, 'c', 'a']

############################### List Methods ################################
print(dir(list))
"""
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""

######### Add data to the list #######
print("_"*50)
# 1. append() method :  add data at the end of list

lista = [4, 6, 8, 1]
lista.append(100)
print("lista :", lista) # [4, 6, 8, 1, 100]

# 2 insert() method : This method add data at specific index position
listb = [4, 7, 8, 22, 99]

listb.insert(2, 500)
print("listb :",listb) # [4, 7, 500, 8, 22, 99]

# 3.  extend() method : This method add values from list1 to list2

list1 = [4, 7, 9]
list2 = ['a', 'b', 'c']
list2.extend(list1)
print("list2 :", list2)  # ['a', 'b', 'c', 4, 7, 9]

list2.append("Hello")
print("list2 :", list2)
list2.append(list1[1])

l1 = [4, 5, 6]
l2 = ['a', 'b', 'c']
l3 = ['p', 'q', 'r']

l3.extend(l2)
l3.extend(l1)
print("l3 :", l3)
# l3 : ['p', 'q', 'r', 'a', 'b', 'c', 4, 5, 6]
l3.append(l2)
print("l3 :", l3)
# l3 : ['p', 'q', 'r', 'a', 'b', 'c', 4, 5, 6, ['a', 'b', 'c']]

############## list concatenation ##########

la = [4, 7, "Programming"]
lb = [6, 2, 4, "Python"]
ld = [7, 9, "Learning"]
str1 = "Hello"

lc = la + lb + ld + list(str1)
print("lc :", lc)
# lc : [4, 7, 'Programming', 6, 2, 'Python', 7, 9, 'Learning', 'H', 'e', 'l', 'l', 'o']

print("lc :", set(lc))
# {2, 'e', 4, 6, 7, 9, 'H', 'Python', 'l', 'o', 'Learning', 'Programming'}

##################### Remove data from list #######################
# 23rd Feb 2024

print("#"*50)

lista = [5, 7, 9, 2, 'a', 'b', 'c', 'a']

# 4. remove() method : This remove specific data from list
# if same data available multiple times then it will remove only first occurance of the data.

var1 = lista.remove('a')
print("lista :", lista, var1)
# lista : [5, 7, 9, 2, 'b', 'c', 'a']

print("_"*50)
# 5. pop() method : Remove data from list using index position and return it.
# default index value is -1

# remove with default index
listb = [5, 7, 22, 66, 344, 77]
val = listb.pop()
print("removed data :", val)
print("listb :", listb)

# remove with index
val2 = listb.pop(3)
print("remove value :", val2)
print("listb :", listb)

print("#"*70)
###############################################
# move data from list1 to list2
list1 = [4, 7, 9, 2, 8]
list2 = []

for i in range(len(list1)):
    val = list1.pop(0)
    list2.append(val)
    print(val, list2)

print("list2 :", list2)
print("list1 :", list1)

#6.  clear() method : this method remove all the data from list

listc = [5, 7, 98, 22, 4]
listc.clear()

print("listc :", listc)  # []

##### delete entire list variable from memory ####

listd = [6, 8, 2, 8, 23, 55]
del listd

# print("listd :",listd)
# name 'listd' is not defined. Did you mean: 'list1'?


#### delete partial values from list ####
# delete value on the basis of slicing rules

listf = [5, 7, 9, 22, 66, 33]

#del listf[3:]    # [5, 7, 9]
#del listf[1::2]  # [5, 9, 66]
del listf[:3]     # [22, 66, 33]
print("listf :", listf)



############# List data menupulation ########
print("_"*50)
# replace data from the list using slicing rules

listv = [6, 8, 33, 88, 22, 16, 18, 23]

listv[0] = 600  # [600, 8, 33, 88, 22, 16, 18, 23]
print("listv :", listv)


listv[-3:] = [100, 200, 300]  # [600, 8, 33, 88, 22, 100, 200, 300]
print("listv :", listv)


listv[0] = listv[-1]
print("listv :", listv)


#list2 = [4, 6, 8, 22, 12]
#print(list2[::-1])


# 7. count() method : this method provide number of occurence of any value

listj = [5, 8, 9, 2, 5, 8, 9, 5]
print("count of 5 :", listj.count(5))  # 3


#8. index() method : this method return the index position of any give value

listk = [6, 8, 3, 9, 23, 9]
print(listk.index(8))  # 1
# print(listk.index(100))  # 100 is not in list
print("index of 9:", listk.index(9)) # 9

for i in range(len(listk)):
    print(i, ":", listk[i])

"""
0 : 6
1 : 8
2 : 3
3 : 9
4 : 23
5 : 9
"""

print("#"*40)
# 9. sort() method : this method sort the list in ascending and decending order and modify the original list.

listb = [6, 8, 1, 8, 2, 16]
# listb.sort()   # this will sort the list in ascending order
# print("listb :", listb)  # [1, 2, 6, 8, 8, 16]

listb.sort(reverse=True)  # this will sort the list in descending order
print("listb :", listb) # [16, 8, 8, 6, 2, 1]


print("_"*50)
###### sorted function ######
# this function  sort the list and return the output, does not modify the origin list.
listn = [5, 7, 2, 8, 1, 17]

# sort in ascending order
result = sorted(listn)  # [1, 2, 5, 7, 8, 17]
print(result)
print("listn :", listn)

# sort the list in descending order
result2 = sorted(listn, reverse=True)  # [17, 8, 7, 5, 2, 1]
print("descending order :", result2)
print("listn :", listn)

print("_"*50)
###################################################################
# write a python program to sort the list

listm = [5, 7, 3, 8, 22, 89, 2, 10]
#  [3, 7, 5, 8, 22, 89, 2, 10]
#  [2, 7, 5, 8, 22, 89, 3, 10]
#  [2, 5, 7, 8, 22, 89, 3, 10]
#  [2, 3, 7, 8, 22, 89, 5, 10]

for i in range(len(listm)): # i = 0
    for j in range(i+1, len(listm)): # j = 1, 2
        if listm[i] > listm[j]: # 5 > 7, 5 > 3
            temp = listm[i] # 5
            listm[i] = listm[j] # [3, 7, 3, 8, 22, 89, 2, 10]
            listm[j] = temp # [3, 7, 5, 8, 22, 89, 2, 10]
        else:
            continue
        print("listm :", listm)

print("listm :", listm)

# 26th Feb 2024
# 10. reverse() : This method any given list and modify the original list

list1 = [4, 7, 92, 8, 1, 12]
list1.reverse()

print("list 1:", list1) #  [12, 1, 8, 92, 7, 4]

# reversed() function : this function take list as input and reverse the list values with interator object and
# loop
list2 = [5, 8, 2, 9, 11, 55]
result = reversed(list2)
print("result :", result)
for val in result:
    print(val, end=" ")
# 55 11 9 2 8 5

#### reverse the list with slicing ####
list3 = [5, 7, 8, 92, 3]
print(list3[::-1])
# [3, 92, 8, 7, 5]


# Inbuilt function
# get sum of list value
list4 = [5, 7, 8, 3, 1]

print("sum of list value :", sum(list4))
print("Max value from list :", max(list4))
print("Min value from list :", min(list4))


lista = ["Hello", "Howreterte", "Are", "You", "Hope", "YOu", "doing", "good"]
print("longest word :", max(lista, key=len)) # Howreterte
print("Smallest word :", min(lista, key=len))  # Are

# listc = [5, 7, 8, "H", "W"]
# print(max(listc))
# TypeError: '>' not supported between instances of 'str' and 'int'


print("_"*50)
################################ Deep copy and Shallow Copy ##################
# shallow copy #
# In shallow copy if we change the values in copied list and it will reflect on original list as well

listp = [5, 7, 9, 12]
listq = listp
listr = listq
lists = listr
listr.append(100)

print("listp :", listp, id(listp)) #  [5, 7, 9, 12, 100]
print("listq :", listq, id(listq)) #  [5, 7, 9, 12, 100]

# Deep Copy
# In deep copy if we change the values in the copies list, then changes will not reflect in original list.
listx = [5, 7, 33, 22]
listy = listx.copy()
listy.append(30)

print("listx :", listx, id(listx))
print("listy :", listy, id(listy))

######################## List Comprehension ################################
print("#"*50)

list1 = [5, 7, 8, 2, 3]
#output = [25, 49, 64, 4, 9]

output = []
for val in list1:
    sqr = val**2
    output.append(sqr)
print("output :", output)

# loop with list comprehesion
result = [x**2 for x in list1]
print("result :", result)

str1 = "We are Learning Python Programming"
upper_result = [word.upper() for word in str1.split(" ")]
#upper_result = [word.upper() for word in str1]
print("upper list:", upper_result)
#  ['WE', 'ARE', 'LEARNING', 'PYTHON', 'PROGRAMMING']

output = " ".join(upper_result)
print("output :", output)
# WE ARE LEARNING PYTHON PROGRAMMING

# list comp with if else condition
lista = [5, 7, 8, 2, 1, 6]
#output = [(5, "odd"), (7, "odd"), (8, "even"), (2, "even"), (1, "odd"), (6, "even")]
# if we have if else condition then we have to write in left most position of the loop
output = [(val, "even") if val%2 == 0 else (val, "odd") for val in lista]
print("output :", output)

# get even length word
# if we have only if condition then write it to the right most of the loop
word_list = ['WE', 'ARE', 'LEARNING', 'PYTHON', 'PROGRAMMING']
result = [word for word in word_list if len(word)%2 == 0]
print("result :", result) # ['WE', 'LEARNING', 'PYTHON']


# Python program to print a combination of 2 elements from the list whose sum is 10.

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


############################################
print("_"*50)
# write a python program to get all the number which are divisible 3 and 7 from given list

lista = [4, 6, 7, 8, 15, 21, 35, 40, 18, 28]
output = []
for val in lista :
    if val%3 ==0 or val%7 ==0:
        output.append(val)
    else:
        output.append(None)

print("output :", output)

#result = [val for val in lista if val%3 == 0 or val%7 == 0]
#print("result :", result)


result = [val if val%3 ==0 or val%7 ==0 else None for val in lista]
print("result :", result)

#21. Write a Python to remove unwanted characters from the given string.
Input_val = "Prog^ra*m#ming"
#Output = “Programming”

result = [char for char in Input_val if char.isalpha()]
print("result :", result)
print("output :", "".join(result))


































