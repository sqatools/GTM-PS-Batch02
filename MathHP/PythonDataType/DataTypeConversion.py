#################Integer#######
import json

#int ...> float
num1 = 55
var1 = float(num1)
print(var1,type(var1))
#55.0 <class 'float'>

#int ...> String
num2 = 4877779567
var2 = str(num2)
print(var2,type(var2))                   #4877779567 <class 'str'>
print(var2,type(var2),var2[2])          #4877779567 <class 'str'> 7

#int ....> list  conversion is not possible
# num3 = 759
# var3 = list(num3)
# print(var3)                           #TypeError: 'int' object is not iterable

#int ....> tuple , conversion is not possible

#int - dict, conversion is not possible

#int ....> set conversion is not possible

#int ....> Boolean

num4 = 568
var4 = bool(num4)
print(var4,type(var4))                 #True <class 'bool'>

num5 = 0
var5 = bool(num5)
print(var5,type(var5))                 #False <class 'bool'>

#Convert number digit int list value , then two conversion will require
#int...>string ....>list

a = 234
var1 = list(str(a))
print(var1)                           #['2', '3', '4']

######Float#####
#float...>int
f1=55.78
v1 = int(f1)
print(v1,type(v1))                    #55 <class 'int'>

####float...>string

f2 = 8765.3455
v2 = str(f2)
print(v2,type(v2),v2[-2])              #8765.3455 <class 'str'> 5

#float..>list conversion not possible
#float..>tuple conversion not possible
#float..>Dict conversion not possible
#float..>set conversion not possible

#float...>Boolean

f3 = 5.67
v3 = bool(f3)
print(v3,type(v3))

f4 = 0.0
v4 = bool(f3)
print(v4,type(v4))

str1 = "Hello"
print(str1)                            #Hello in console, no " quotes

###String

#string...>int
# str1 = "Hello"
# v1 = int(str1)
# print(v1,type(v1))
#ValueError: invalid literal for int() with base 10: 'Hello'
#If string contains only numbers then string to integer conversion is possible

str2 = "5768"
v2 = int(str2)
print(v2,type(v2),v2*2)

#####string...> flost

str2 = "65476.7897"
v3 = float(str2)
print(v3,type(v3))

###string ...> list
stra = "python"                             #['p', 'y', 't', 'h', 'o', 'n'] <class 'list'> y
l1 = list(stra)
print(l1,type(l1),l1[1])                    #IndentationError: unexpected indent if space

####string...>tuple

strb = "Programming"
t1 = tuple(strb)
print(t1,type(t1),t1[-1])                  #('P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g') <class 'tuple'> g

####string ....> dict

# strc = "good"
# d1 = dict(strc)
# print(d1,type(d1))                        #ValueError: dictionary update sequence element #0 has length 1; 2 is required

#import json

stre = '{"Name" : "Rahul", "age" : 25 ,"mobile" : 7850568756}'
d2 = json.loads(stre)
print(d2,type(d2))                         #{'Name': 'Rahul', 'age': 25, 'mobile': 7850568756} <class 'dict'>
print(d2,['mobile'])                       #{'Name': 'Rahul', 'age': 25, 'mobile': 7850568756} ['mobile']

####string ....> set

strd = "Learning"
s1 = set(strd)                            #{'r', 'n', 'L', 'g', 'i', 'a', 'e'} <class 'set'> , duplicate n is printed only once
print(s1,type(s1))

####string ...>Boolean

str_g = "Hello"
b1 = bool(str_g)
print(b1,type(b1))                       #True <class 'bool'>

str_h = " "
b2 = bool(str_h)
print(b2,type(b2))                       #True <class 'bool'>

str_i = ""
b3 = bool(str_i)
print(b3,type(b3))                       #False <class 'bool'>

#####List###

#list...>int  conversion not possible
#list...>float conversion not possible
#list...>string  conversion not possible

l1 = [4,7,8]
s1 = str(l1)
print(s1,type(s1), s1[0], s1[1], s1[2], s1[3])                                  #[4, 7, 8] <class 'str'> [ 4 ,

###list...>tuple

l2= [5,8,6,3,2,9]
t1 = tuple(l2)
print(t1,type(t1),t1[0])                                                       #(5, 8, 6, 3, 2, 9) <class 'tuple'> 5

#####list ....> dict

# l3 = [5,7,8,89,2,6]
# d3 = dict(l3)
# print(d3,type(d3))                            #cannot convert dictionary update sequence element #0 to a sequence

lista = ['a','b','c']
listb = [345,786,876]
result = dict(zip(lista,listb))                #{'a': 345, 'b': 786, 'c': 876}
print(result)

####list...> set

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

########################## Tuple #######################
print("_"*40)
#  tuple ->int : conversion is not possible
#  tuple -> float : conversion is not possible
# tuple -> string
tup1 = (3, 6, 8, 1)
str1 = str(tup1)
print(str1, type(str1), str1[-2])
# (3, 6, 8, 1) <class 'str'> 1

# tuple -> list

tup2 = (5, 7, 8, 2)
l1 = list(tup2)
print(l1, l1[1], type(l1))
# [5, 7, 8, 2] 7 <class 'list'>

"""
# tuple -> dict
t1 = (4, 7, 9, 2)
d1 = dict(t1)
print(d1, type(d1))
# TypeError: cannot convert dictionary update sequence element #0 to a sequence
"""

t2 = ('a', 'b', 'c', 'd', 'e')
t3 = (456, 67, 83, 32, 12)
print(t2, t3)

result = dict(zip(t3, t2))
print(result, type(result))
# {'a': 456, 'b': 67, 'c': 83, 'd': 32, 'e': 12} <class 'dict'>
# {456: 'a', 67: 'b', 83: 'c', 32: 'd', 12: 'e'} <class 'dict'>

print("_"*40)

######## tuple -> set ###########
t5 = (4, 6, 2, 8, 1, 2, 6)
s1 = set(t5)
print(s1, type(s1))
# {1, 2, 4, 6, 8} <class 'set'>


######## Tuple -> Boolean #######
t1 = (5, 7, 3, 8)
b1 = bool(t1)
print(b1, type(b1))
# True <class 'bool'>

t2 = () # empty tuple
print(t2, type(t2))
b2 = bool(t2)
print(b2, type(b2))
# False <class 'bool'>

################# Dictionary #############
print("_"*40)
# dict -> int : conversion not possible
"""
dict1 = {'a' : 456, 'b' : 256, 'Name': 'Rahul', 'a' : 666}
print(dict1['a'])
val1 = int(dict1)
print(val1)
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
"""


# dict -> float : conversion is not possible
# dict -> string :
dict1 = {'Name' : 'john', 'mobile' : 5654645, 'email' : 'john123@gmail.com'}
s1= str(dict1)
print(s1, type(s1), s1[0], s1[2])
# {'Name': 'john', 'mobile': 5654645, 'email': 'john123@gmail.com'} <class 'str'> { N

### dict -> list ###
dict1 = {'Name' : 'john', 'mobile' : 5654645, 'email' : 'john123@gmail.com'}
l1 = list(dict1)
print(l1, type(l1), l1[-1], l1[1])
# ['Name', 'mobile', 'email'] <class 'list'> email mobile


#### dict -> tuple  ####
dict1 = {'Name' : 'john', 'mobile' : 5654645, 'email' : 'john123@gmail.com'}
t1 = tuple(dict1)
print(t1, type(t1))
# ('Name', 'mobile', 'email') <class 'tuple'>

#### dict -> set #####
dict2 = {'Name' : 'john', 'mobile' : 5654645, 'email' : 'john123@gmail.com'}
set1 = set(dict2)
print(set1, type(set1))
# {'Name', 'email', 'mobile'} <class 'set'>


##### dict -> boolean ####

dict11 = {'a' : 123}
b1 = bool(dict1)
print(b1, type(b1))
# True <class 'bool'>

dict2 = {}
b2 = bool(dict2)
print(b2, type(b2))
# False <class 'bool'>

############ Set ##############

set1 = {5, 'B', 7, 2, 8, 'a', 1, 3, 5, 7, 8}

# set -> int # conversion is not possible
# set -> float #  conversion is not possible
# set -> string #
print("_"*50)
print(set1, type(set1))
s1 = str(set1)
print(s1, type(s1), s1[0], s1[1])
# {1, 2, 3, 5, 7, 8, 'a', 'B'} <class 'str'> { 1


# set -> list
set2 = {4, 6, 8, 'C', 2, 6, 7, 2, 8, 'a', "B"}
l1 = list(set2)
print(l1, l1[0])
# [2, 4, 6, 7, 8, 'a', 'B', 'C'] 2

# set -> tuple
s2 = {4, 7, 9, 12}
t1 = tuple(set2)
print(t1, type(t1))
# ('B', 2, 4, 6, 7, 8, 'a', 'C') <class 'tuple'>


# set -> dict : conversion is not possible
# set -> bool
set1 = {4, 6}
b1 = bool(set1)
print(b1, type(b1))
# True <class 'bool'>

set2 = {}
b2 = bool(set2)
print(b2, type(b2))
# False <class 'bool'>

s1 = {4, 6, 8, 9}
s2 = {'a', 'b', 'c', 'd'}

result = dict(zip(s1, s2))
print(result)
# {8: 'c', 9: 'd', 4: 'b', 6: 'a'}


###### Boolean ###########

# bool -> int
v1 = True
v2 = int(v1)
print(v2) # 1

v3 = False
v4 = int(v3)
print(v4) # 0

# bool -> float
v1 = True
v2 = float(v1)
print(v2)  # 1.0

v3 = False
v4 = float(v3)
print(v4) # 0.0

# bool -> string
var1 = True
s1 = str(var1)
print(s1, type(s1), s1[0])
# True <class 'str'> T


# bool -> list # conversion is not possible
"""
b1 = True
l1 = list(b1)
print(l1, type(l1))
"""
# bool -> tuple # conversion is not possible
# bool -> dict # # conversion is not possible
# bool -> set # # conversion is not possible
"""
v1 = True
s1 = set(v1)
print(s1)
"""












