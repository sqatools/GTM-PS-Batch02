### 22nd Feb 2024 ###

list1=[12,3.6,"Python",[3,5,6],(4,8,2),{'a':123,'b':567},{5,8,3},True]

"""
Properties:
....> List is mutable , can modify at any point of time.
....> List can contain all type of data
....> List follow the positive and negative indexing as like string
"""

print("list1:",list1)
print(type(list1))

### Get value from list
var1 = list1[2]
print("var1:",var1)           #Python

var2 = list1[-4]
print("var1:",var2)

print(list1[-4][1])          # right to left -1 ,... left to right 0,....

## Apply loop on the list

lista = ['a','Hello','Python','Programming']

#Get values Without indexing

for val in lista:
   # print(val,end = " ")        # same line
    print(val)

##########################################
# get list values with indexing

for i in range(len(lista)):
    print(i,lista[i])

"""
0 a
1 Hello
2 Python
3 Programming

"""

### Slicing in the  list

list1 = [4,7,9,2,8,12]
print(list1[2:5])                # [9, 2, 8]
print(list1[1:-2])              #[7, 9, 2]
print(list1[-4:])               # [9, 2, 8, 12] left to right bcoz difference is 1 not -1

lista = [5,7,'a','b','c','d',33,22,14]
print(lista[2:8:1])            # ['a', 'b', 'c', 'd', 33, 22]

print(lista[:3:-1])           # [14, 22, 33, 'd', 'c']
print(lista[:-6:-1])

print(lista[:5:-2])          # [14,33]

print(lista[::-1])           # [14, 22, 33, 'd', 'c', 'b', 'a', 7, 5]

print(lista[-5::-1])
print(lista[-1::2])         # [14]
print(lista[-7::2])        # ['a', 'c', 33, 14]

print(lista[-1:-8:-2])     # [14, 33, 'c', 'a']     Right to left

################################# List Methods #######################################

print(dir(list))

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# 1)append() method :
#Add data at the end of the list

lista = [4,6,8,1]
lista.append(100)               # append()  only for the list
print("lista:",lista)

#2) insert() method: Thsi method add data at specific index position

listb = [4,7,8,22,99]

listb.insert(2,500)
print("listb:",listb)

# 3) extends() method: This method add values from list1 to list2

list1 = [4,7,9]
list2 = ['a','b','c']
list2.extend(list1)            # Modified list2 is the new one
print("list2:",list2)

list2.append("Hello")
print("list2:",list2)

l1 = [4,5,6]
l2 = ['a','b','c']
l3 = ['p','q','r']

l3.extend(l1)                  # extends modifies the existing list
print("l3:",l3)               # Modified l3  ['p', 'q', 'r', 4, 5, 6]

l3.append(l2)
print("l3:",l3)              # l3: ['p', 'q', 'r', 4, 5, 6, ['a', 'b', 'c']]  child list

################### List concatenation

la = [4,7,9,"Programming"]     # Duplication allowed
lb = [6,2,1,4,"Python"]
ld = [7,9,1,"Learning"]
str1 = "Hello I'm here"

lc = la+lb+ld+list(str1)
print("lc:",lc)
print("lc:",set(lc))          # No duplicates allowed and random order, unique


################# Remove data from list
print("_"*60)

lista = [5,7,9,2,'a','b','c','a']

#4) remove() method: This removes specific data from list
# If same data available multiple times then it will remove only first occurrence of the data

lista.remove('a')                      # Only one argument
print("lista:",lista)

# 5) pop() method: Remove data from list using index position
# default index value is -1
# remove with default index

listb =[5,7,22,66,344,77]
val = listb.pop()                       # remove 77
print("Removed data:",val)
print("listb:",listb)
val1 = listb.pop(3)                       # remove 66
print("Removed data:",val1)
print("listb:",listb)

##################################################
# Move data from list1 to list2

list1 =[4,7,9,2,8]
list2 =[]
for i in range(len(list1)):           # length 5
    val = list1.pop()
    list2.append(val)
    print(val,list2)                 # 8 [8]

print("list2:",list2)
print("list1:",list1)

#6) clear() method : This method remove all the data from list, empty list

listc = [5,7,98,22,4]
listc.clear()
print("listc:",listc)

# delete entire list variable from memory , so no available at all

listd = [6,7,98,22,4,68]
del listd

#print("listd:",listd)                 # NameError: name 'listd' is not defined. Did you mean: 'list1'?, deleted completely

# delete partial values from the list, apply slicing rule

listf = [5,87,89,23,54,56,23]
del listf[-3:]                        # [5, 87, 89, 23]
print(listf)

del listf[1::2]                      # [5, 89] from the existing list
print(listf)

###### List data manipulation

# Replace data from the list using slicing rule

print("_"*60)
listv = [6,8,9,43,56,22]
listv[0] = 600                        # listv: [600, 8, 9, 43, 56, 22] Replaced
print("listv:",listv)

listv[-3:]=[100,200,300]             # in the updated list
print("listv:",listv)                # listv: [600, 8, 9, 100, 200, 300]

list4 = [67,8,99,43,569,22]
print("list4:",list4[::])           # [67, 8, 99, 43, 569, 22] same list no change

# 7) count() method: This method provides number of occurrences of any value

listj = [5,8,9,2,5,8,9,5]
print("Count of 5:",listj.count(5))

################# list most important data type in python

## 8) index() method: This method returns the index position of any given value

listk = [6,8,3,9,23]
print(listk.index(8))                  # 1
#print(listk.index(100))               # ValueError: 100 is not in list

print(listk.index(9))                 # 3

for i in range(len(listk)):
    print(i,listk[i])

"""
0 6
1 8
2 3
3 9
4 23
"""

## 9) sort() method: This method sort the list in ascending and descending order and modify the original list

listb =[6,8,1,8,2,16]
listb.sort()                           # This will sort in ascending order
print("listb:",listb)                 # listb: [1, 2, 6, 8, 8, 16]

listc =[69,81,15,82,82,27,163]
listc.sort(reverse=True)                   # reverse=False means by default ascending order
print("listc:",listc)

## sorted function
# This function sort the list and returns the output does not modify original  list

listn = [5,7,2,8,1,17]

result = sorted(listn)
print("Ascending Order:",result)
print("listn:",listn)

## sorted function                # sort() is a method and sorted , del is a function
# Descending order

result = sorted(listn,reverse=True)
print("Descending Order:",result)                     # ctrl +Alt +i
print("listn:",listn)

###########################################################################
# WAP to sort the list without using sorted function

listm = [5,7,1,8,22,89,2,99,10]

for i in range(len(listm)):                     #i=0
    for j in range(i+1,len(listm)):             #j=1,2
        if listm[i]>listm[j]:                   #5>7,5>1
            temp = listm[i]                     # a=b and b=c then a=c , temp is parking data temporarily
            listm[i]=listm[j]
            listm[j]=temp
        else:
            continue
        print("listm:",listm)

print("listm in ascending order:",listm)











