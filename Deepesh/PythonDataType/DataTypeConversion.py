"""
Python Data Type

1. Numbers
    i)   Integer
    ii)  Float
    iii) Complex
2. Sequential Data
    i).   String
    ii).  List
    iii). Tuple
3. Dictionary
4. Set
5. Boolean
"""

############ Integer ###########

# int -> float

num1 = 55
var1 = float(num1)
print(var1, type(var1))
# 55.0 <class 'float'>

# int ->  string
num2 = 576892
var2 = str(num2)
print(var2, type(var2), var2[2])

# int -> list # conversion is not possible
"""
num3 = 6546
var3 = list(num3)
print(var3)
# TypeError: 'int' object is not iterable
"""

# int -> tuple # conversion is not possible
# int - dict # conversion is not possible
# int -> set # conversion is not possible
# int - Boolean
num4 = 568
var4 = bool(num4)
print(var4, type(var4))
# True <class 'bool'>

num5 = 0
var5 = bool(num5)
print(var5, type(var5))
# False <class 'bool'>

#######
# convert number digit int list value, then two conversion will required
# int -> string -> list
a = 234
var1 = list(str(a))
print(var1)
# ['2', '3', '4']

################ Float ###############

# float -> int
f1 = 55.78
v1 = int(f1)
print(v1, type(v1))
# 55 <class 'int'>


# Float -> string

f2 = 856.773
v2 = str(f2)
print(v2, type(v2), v2[-2])
# 856.773 <class 'str'> 7

# Float -> list # conversion is not possible
# Float -> Tuple # conversion is not possible
# Float -> Dict # conversion is not possible
# Float -> set # conversion is not possible
# Float -> Boolean

f3 = 5.5
v3 = bool(f3)
print(v3, type(v3))
# True <class 'bool'>

f4 = 0.3
v4 = bool(f4)
print(v4, type(v4))
# False <class 'bool'>

################ String ################

"""
# string -> int
str1 = "Hello"
v1 = int(str1)
print(v1, type(v1))
# ValueError: invalid literal for int() with base 10: 'Hello'
"""
# if string contains only numbers then the string to integer
# conversion is possible
str2 = "56734"
v2 = int(str2)
print(v2, type(v2), v2*2)
# 56734 <class 'int'> 113468

###### string -> float ######

str2 = "556.78"
v3 = float(str2)
print(v3, type(v3))
# 556.78 <class 'float'>

### string -> list ###

stra = "Python"
l1 = list(stra)
print(l1, type(l1), l1[1])
# ['P', 'y', 't', 'h', 'o', 'n'] <class 'list'> y
l1.append(40)
print(l1)
# ['P', 'y', 't', 'h', 'o', 'n', 40]

#### sting -> tuple #####

strb = "Programming"
t1 = tuple(strb)
print(t1, type(t1), t1[-1])
# ('P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g') <class 'tuple'> g


##### string -> dict ######
#
# strc = "Good"
# d1 = dict(strc)
# print(d1, type(d1))
# ValueError: dictionary update sequence element #0 has length 1; 2 is required

import json
stre = '{"Name" : "Rahul", "age" : 25, "mobile" : 795676959}'

d2 = json.loads(stre)
print(d2, type(d2))
# {'Name': 'Rahul', 'age': 25, 'mobile': 795676959} <class 'dict'>
print(d2['mobile'])
# 795676959


#d3 = dict(stre)
#print(d3)
# ValueError: dictionary update sequence element #0 has length 1; 2 is required

###### string -> set ########

strd = "Learning"
s1 = set(strd)
print(s1, type(s1))
# {'g', 'n', 'L', 'i', 'e', 'r', 'a'} <class 'set'>

##### string -> Boolean ######
str_g = "Hello"
b1 = bool(str_g)
print(b1, type(b1))
# True <class 'bool'>

str_h = " "
b2 = bool(str_h)
print(b2, type(b2))
# False <class 'bool'>

################## List #######################


# list -> int # conversion is not possible
# list -> float # conversion is not possible
# list -> string
l1 = [4, 7, 8]
s1 = str(l1)
print(s1, type(s1), s1[0], s1[1], s1[2], s1[3])
# [4, 7, 8] <class 'str'> [ 4 ,


### list -> tuple ####

l2 = [5, 7, 8, 2, 9]
t1 = tuple(l2)
print(t1, type(t1), t1[0])
# (5, 7, 8, 2, 9) <class 'tuple'> 5

#### list -> dict  ##### # conversion is not possible

# l3 = [5, 7, 2, 8, 3]
# d3 = dict(l3)
# print(d3, type(d3))
# cannot convert dictionary update sequence element #0 to a sequence


# convert two list data into dictionary with zip function.
lista = ['a', 'b', 'c']
listb = [345, 567, 789]
result = dict(zip(lista, listb))
print(result, result['a'])
# {'a': 345, 'b': 567, 'c': 789}, 345


##### list -> set #######
list2 = [4, 7, 8, 2, 3, 4, 7]
var2 = set(list2)
print(var2, type(var2))
# {2, 3, 4, 7, 8} <class 'set'>


##### list -> boolean #######
list2 = [4, 6, 8, 2]
b1 = bool(list2)
print(b1, type(b1))
# True <class 'bool'>

list3 =[]
b2 = bool(list3)
print(b2, type(b2))
# False <class 'bool'>





