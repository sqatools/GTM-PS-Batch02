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
# {2, 'e', 4, 6, 7, 9, 'H', 'Python', 'l', 'o',