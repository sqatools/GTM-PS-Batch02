"""
Python DAta Types
-------------------
1)Numbers:
----------
    Integer
    Float
    Complex
2) Sequential Data Types
------------------------
    String
    List
    Tuple
3) Dictionary
-------------
4) Set
-------
5) Boolean
------------
"""
"""
############# Integer#########
Integer to float
----------------------------
"""
num1 = 56
print(type(num1))
# <class 'int'>
print(type(float(num1)))
# <class 'float'>
print(num1) # 56
print(float(num1)) # 56.0
"""
integer to string
-----------------------------
"""
num2 = 34455666777
var1 = str(num2)
print(var1, type(var1), var1[5],var1[6]) #34455666777 <class 'str'> 6 6

"""
int to list -----. Conversion is not possible
------------------------------------------------
num3 = 46475746344
var2 = list(num3)
print(var2)
TypeError: 'int' object is not iterable.
int to tuple ---> Conversion is not possible
int to dict------> conversion is not possible
int to set -------> conversion is not possible
"""
##################################################3
"""
Integer to boolean
------------------------
If the variable is assigned a value (other than 0) , it returns 'True' else it returns 'False'
"""
num3 = -45
bool1 = bool(num3)
print(bool1) #True

num4 = int()
bool2 = bool(num4)
print(bool2) #False
print(type(bool2)) #<class 'bool'>

num5 = 0
print(bool(num5)) #False

a = 46547476575
print(list(str(a))) # ['4', '6', '5', '4', '7', '4', '7', '6', '5', '7', '5']
print(tuple(str(a))) # ('4', '6', '5', '4', '7', '4', '7', '6', '5', '7', '5')
print(set(str(a))) # {'4', '5', '7', '6'}


"""
Float
--------------

"""
fl1 =67.758768
var1 = int(fl1)
print(var1)#67

var2= str(fl1)
print(var2, var2[4])

"""
float to list-----> conversion not possible
float to tuple-----> conversion not possible
float to dict-----> conversion not possible
float to set-----> conversion not possible
"""

fl2 = 567.68768768
print(list(str(fl2)))
print(tuple(str(fl2)))
print(set(str(fl2)))

'''Float to Boolean
 ----------------'''
fl1 = float()
print(bool(fl1))  # False
fl2 = 34.89
print(bool(fl2))  # True
fl3 = 0
print(bool(fl3))  # False


"""
String to integer
------------------------

str1= "Hello"
var1 = int(str1) # ValueError: invalid literal for int() with base 10: 'Hello'
string to integer is only possible if the string contains a number
"""

str2 = "4567  "
var2 = int(str2)
print(var2) # 4567
print(str2, type(str2), str2* 5) # 4567   <class 'str'> 4567  4567  4567  4567  4567
print(var2 , type(var2), var2*5) # 4567 <class 'int'> 22835

"""
String to float
String to float is possible only if the string contains a floating point number
"""

str3 = 56.89
var3 =str(str3)
print(var3)

"""
String to list

"""
stra = "Python"
list1 =list(stra)
print(list1) # ['P', 'y', 't', 'h', 'o', 'n']
print(list1[4])
list1.append("p")
print(list1)
print(set(list1))
print(tuple(list1))


"""
string to tuple
---------------
"""
str1 = "Programming"
tu = tuple(str1)
print(tu) # ('P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g')
# String to set
st = set(str1)
print(st)

"""
String to Dictionary
Conversion is possible only the string contains the data in the same format as the dictionary
"""
import json
str1= '{"name":"Raj", "age": 25,"email":"raj@gmail.com"}'
#dict1 = dict(str1) # Error
dict1 = json.loads(str1)
print(dict1) # {'name': 'Raj', 'age': 25, 'email': 'raj@gmail.com'}
print(dict1["email"])


"""
String to set
"""
str1= "Learnig"
st = set(str1)
print(st) # {'r', 'a', 'e', 'L', 'g', 'i', 'n'} #nrandom order, no duplication


"""
 String to Boolean
"""
str1 ="Boolean"
str2 =""
str3 =" "

bl1 = bool(str1)
bl2 = bool(str2)
bl3 = bool(str3)
print(bl1 , type(bl1)) # True <class 'bool'>
print(bl2 , type(bl2)) # False <class 'bool'>
print(bl3 , type(bl3)) # True <class 'bool'>

"""
List
==========
list to integer-----> conversion is not possible
list to float-----> conversion is not possible
"""
# List to Str
li =[6, 8.9 ,9]
st = str(li)
print("----------")
print(st , type(st) ,st[4],st[6],st[7]) # [6, 8.9, 9] <class 'str'> 8 9 ,

# List to tuple
#-------------

li =[56 , 78 , 89, 90.09,"hi"]
tu = tuple(li)
print(tu, type(tu)) # (56, 78, 89, 90.09, 'hi') <class 'tuple'>
# List to Dictionary

"""
l3 =[56 , 78 , 89, 90.09,"hi"]
d1 = dict(l3)
print(d1) # TypeError: cannot convert dictionary update sequence element #0 to a sequence
conversion is not possible
"""
##################################################3
l1 = ['a','b','c','d']
l2 =[3,6,8]
result = dict(zip(l1,l2))
print(result) # {'a': 3, 'b': 6, 'c': 8} # ignores the extra key
print("@#"*50)
######################################################

# list to set

l1 =[89, 98, 67,67,67,89,]
st =set(l1)
print(st, type(st)) # conversion is possible, doesn't show the duplicate values
#{89, 98, 67} <class 'set'>

##### List to boolean
l1 =[7,8]
l2 =[]
bl1 = bool(l1)
bl2 = bool(l2)
print(bool1) # True
print(bool2) # False


