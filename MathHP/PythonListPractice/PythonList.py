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
print("lc:",set(lc))          # No duplicates allowed and random order



