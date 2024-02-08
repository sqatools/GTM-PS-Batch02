
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

Properties of Integer
-----------------------
1) Integer is an immutable data type.
2) Any whole number will be considered as an integer.
3)There is no specific range or limit for integer value.

"""
num1 = 3
num2 = 45
num3 = 547698709464654767
print(num1 , type(num1))
print(num2, type(num2))
print(num3 , type(num3))
num4 = int()
print(type(num4))
print('*'* 50)

"""
Properties of float
-------------------------
1)Float is an immutable data type.
2)Any decimal number will be consider as float.
3)There is no specific range or limit for float value, we can define
any long number decimal number as float.
"""
num1 = 34.67
num2 = 455.67565454234657657668769879879
print(num1 , type(num1))
print(num2 , type(num2))

print("%" * 50)

"""
Complex Numbers
-----------------
 complex number (x+yj)
 real number : x
 imaginary number : y
"""
var1 = 5+ 6j
var2 = var1 + 454677
print(var1 , type(var1))
print(var2, type(var2))

print('@'* 50)

"""
 Sequential Data Type
 --------------------
 String
 ---------
 
Properties of string
------------------------
String is an immutable data type.
String follows the positive and negative indexing
We can store any long raw data as string.

 """
str1 = "Hello"
str2 = "Welcome to 'Python Programming'"
str3 = " "

str4 = "Python 0989879867876765646 Programming"

print(str1, type(str1))
print("_"*50)
print(str2, type(str2))
print("_"* 50)

print(str3, type(str3))
print("_" * 50)
print(type(str4))

str1 = "Python "
# 0  1  2  3  4  5   # +ve Indexing
" P  y  t  h  o  n"
# -6 -5 -4 -3 -2 -1  # -ve indexing
print(str1)

print(str1[2], str1[-4])

str2 = "Hello! Good Morning"
print(str2[6])
print(str1 + str2 )

# print(str2[10])
# IndexError: string index out of range



"""
List
-------
List is a mutable data type, we can modify the list at any point of time
        ------------------
List follows the similar positive and negative indexing as like string.
All type of data can be stored in a list, like , int, float, string, boolean, dict, list, tuple, set.
IF we compare list and tuple , then list is a bit slower than tuple.

"""
#       0     1      2          3            4            5
list1 =[34 , 56.8, "Helloo", (4 , 5 , 6), {34, 5.6, "A"},[56, 78 , 5+6j]]
#        -6      -5     -4             -3            -2              -1
print(list1 , type(list1))
print(list1[3] , type(list1[3]))
print(list1[-3][2] , type(list1[-3][2]))
print(list1[4] , type(list1[4]))
print(list1[5][2] , type(list1[5][2]))
list1.append(10000000)
list1.append({"Thushara" , "Aadhu"})
print(list1)

print(dir(list1))



print("&"*50)

"""
# Properties of  tuple 
--------------------------
->  Tuple is immutable data type, we can not modify once it is defined.
->  Tuple follows the positive and negative indexing as like string and list
->  All type of data can be part of the tuple, like int. float, string, list, tuple, dict, set, boolean
->  Tuple is faster than list to access the data.
"""
#       0     1      2          3            4            5
tup1 =(34 , 56.8, "Helloo", (4 , 5 , 6), {34, 5.6, "A"},[56, 78 , 5+6j])
#     -6      -5     -4             -3          -2              -1

print(tup1)
print(type(tup1)) # class 'tuple'>

print(tup1[3])
print(tup1[3][1])

print(tup1[-4])
print(tup1[-4][1])


tup2 = (56,)
list1 = [45]
print(tup2 ,type(tup2))

print(list1 ,type(list1))

print(dir(list))
print(dir(tuple))
print(tup1[-2] ,type(tup1[-2]))

print("!"*50)




dict1 = {'name' : 'Rahul', 'age' : 20, 'address' : 'Mumbai'}
#       {key : value}
"""
DICTIONARY
-------------
Dictionary properties
Dictionary  is a mutable data type, we can modify it any point of time.
               -------------------
All keys should be unique in the dict, duplicate keys are not allowed.
Only immutable data type can key in the dict, e.g int, float, string, tuple, boolean.
We can set all type of data as dict value , int, float, string, list, tuple, set, boolean.
Dict does not follow any indexing, it stores the data un-structure order.
     ----------------------------
"""

dict1 = {'name': 'Ammu' , 'age' : 30,'address': 'Kerala'}

print(dict1)

print(dict1, type(dict1))
# <class 'dict'>

# Dict is a mutable data type, we can modify it at any point of time.
dict1['email'] = "ammu@gmail.com"
dict1['phone'] = 12233444445555
print(dict1)

dict2 = {}
dict2["gender"] = 'female'
print(dict2)
print(dir(dict))

var1 = dict1["email"]
print(var1)
var2 = dict2["gender"]
print(var2)
# All keys should be unique in the dict, duplicate keys are not allowed.
dict3= {'a':45, 'a': 56}# duplicate key
print(dict3) #{'a': 56}
# Only immutable data types can be a key in a dictionary

dict4={}
dict4["a"]= (2, 3, 4)
dict4[("Achu", 'ad', 56, 45.8)] = {"Anu", 567,(45, 67 ,78)}
dict4["Hi"] = {'name': 'Sarah', 'age': 20}
dict4[3] =(5, 6, 'a')
print(dict4)


print('^'*50)
"""
dict4[[4, 7, 8]] = 463565 # We can not add list as key
print(dict4) # TypeError: unhashable type: 'list'

dict4[{'a': 123}] = "Good Morning" # # We can not dict as key
print(dict4)  # unhashable type: 'dict'

dict does not follow indexing
print(dict4[0])  #KeyError: 0
"""

school = {
                   'admin': [
                                   {'username': 'madhav','email': 'madhav@gmail.com'},
                                   {'username': 'Tarun','email':'tarun@gmail.com'}
                            ],
                   'teachers': {
                             'physics': [
                                    {'name': 'Arav', 'email': 'arav@gmail.com'} ,
                                    {'name': 'Jane','email': 'jane@gmail.com'}
                                        ],
                             'maths': [
                                    {'name':'john','email':'john@gmail.com'},
                                    {'name':'Jaya','email':'Jaya@gmail.com'}
                                      ]
                   },
                    'student': []
           }

print(school)
print(school['teachers']['maths'][1]['name'])

print('+'*50)


"""
# Properties of Set
-------------------------
Set is mutable data type, we can modify the data at any point of time.
       ------------
Set only store unique data, duplicate data is not allowed.
All the immutable data type can be member of set, int, string, float, tuple, boolean.
Mutable data type can not be a member of set eg: list, dict, set
----------------------
Set store the data in random order, it does not follow any indexing.
"""

set1 = {4, 7, 'a', 'b', 7, 5, 3, 4}
print(set1, type(set1))

# Set is a mutable data type, we can modify the data at any point of time.
print(dir(set))
set2 = {4, 6, 8, 4}
set2.add(50)
print("set2 :", set2) # {8, 50, 4, 6}

# repeated values will not consider, 4 will consider only once.

# All the immutable data type can be member of set, int, string, float, tuple, boolean.
set3= {4, 3.5, 'Hello', (4, 7, 8), True}
print(set3) # {True, 3.5, 4, (4, 7, 8), 'Hello'}
"""
Mutable data type can not be a member of a Set eg: list, dict, set
set4 = {[4, 6, 7], 6, 8, 9}
print(set4)
TypeError: unhashable type: 'list'

set4 = {6, 8, 9, {'a': 123, 'b': 345}}
print(set4)
TypeError: unhashable type: 'dict'
"""
set6 = set()
set6.add(10000)
print("set6 :", set6)

# var1 = int()
# var2 = str()
# var3 = list()
# var4 = tuple()
"""
Boolean  Data type
---------------------
Boolean data represent with True or False
Boolean is immutable data type.
"""
var1 = 200
var2 = 100
var3 = 200

print(var1 == var2) # False
print(var1 == var3) # True

"""
Mutable data types ---> List,Dictionary,Set
-----------------------------------------------
Mutable data types cannot be a key.
Mutable data types cannot be a member of a Set
Immutable data types------> Integer ,Floating Point Numbers,String , Tuple, Boolean
------------------------------------------------------------------------------
"""




