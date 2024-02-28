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



















