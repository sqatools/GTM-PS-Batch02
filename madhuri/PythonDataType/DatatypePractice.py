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

# Integer data type

var1 = 2
var2 = 456
var3 = 532454325432543254325
print(type(var1), "\n")
print(type(var2))
print(type(var3))

var4 = int
"""
Properties of integer
-> Integer is immutable data type.
-> Any whole number will be consider as integer.
-> There is no specific range or limit for integer value, we can define 
any long number as int.
"""

print("_"*50)
# float data type

var_a = 80.25
var_b = 0.25
var_c = 45.67657657657

print(type(var_a), var_a)
print(type(var_b), var_b)
print(type(var_c), var_c)  # <class 'float'>

"""
Properties of integer
-> Float is immutable data type.
-> Any decimal number will be consider as float.
-> There is no specific range or limit for float value, we can define 
any long number decimal number as float.
"""

# complex number (x+yj)
# real number : x
# imaginary number : y

val = 4+5j
val2 = 435435 + 5.6j
print(val, type(val))
# (4+5j) <class 'complex'>
print(val2, type(val2))
print("Hello Good Morning")
var3 = "Good Evening"
print("Hey ", var3)

var1 = 800
var1 = 1000
print(var1)


print("_"*40)
######### Sequantial Data Type #######

# String

str1 = "H"
str2 = 'Hello'
str3 = """programmer in any programming language 
(whatever it may be) can 'pick' up Python very quickly. 
It's also easy for beginners to use and learn, 
so jump in!"""

str4 = '''
programmer in any "programming" 
language (whatever it may be) 
can pick up Python very quickly. 
It's also easy for beginners to 
use and learn, 
so jump in!
'''

str5 = ''

str6 = "Python 5645645645 Programming"

print(str1, type(str1))
print("_"*40)
print(str2, type(str2))
print("_"*40)

print(str3, type(str3))
print("_"*40)

print(str4, type(str4))
print("_"*40)

print(str5, type(str5))
print("_"*40)


stra = "Python"
# 0  1  2  3  4  5   # +ve Indexing
" P  y  t  h  o  n"
# -6 -5 -4 -3 -2 -1  # -ve indexing

print(stra)

print(stra[2], stra[-4])

strb = "Hello Good"
print(strb[6])

# print(strb[10])
# IndexError: string index out of range

"""
Properties of string
-> String is immutable data type
-> String follows the positive and negative indexing
-> We can store any long raw data as string.
"""

print("_"*40)
###### List #########

#        0  1     2       3
list1 = [3, 4.5, 'Hello', [4, 6, 8]]
#       -4  -3   -2      -1


print(list1, type(list1))  # <class 'list'>

print(list1[2])
var1 = list1[-3]
print(var1, type(var1))  # 4.5 <class 'float'>

print(list1[3]) # [4, 6, 8]
print(list1[3][1]) # 6

listb = [5, 7, 9]
listb.append(20)
print(listb) # [5, 7, 9, 20]
listb[1] = 100
print(listb) # [5, 100, 9, 20]
"""
# Properties of list
 -> List is mutable data type, we can modify the list at any point of time
 -> List follows the similar positive and negative indexing as like string.
 -> All type of data can store in the list, like , int, float, string, boolean, dict, list, tuple, set.
 -> IF we compare list and tuple , then list is a bit slower than tuple.
"""
print("_"*50)
############ Tuple ###########

#       0  1     2        3          4          5       # +ve
tup1 = (3, 4.5, 'Python', [3, 5, 6], (3, 2, 1), True)
#      -6  -5    -4      -3          -2         -1      # -ve

print(tup1)
print(type(tup1)) # class 'tuple'>

print(tup1[3]) # [3, 5, 6]
print(tup1[3][1])  # 5

print(tup1[-4]) # Python
print(tup1[-4][1])  # y

print(dir(list))
print(dir(tuple))

tup2 = (4, )
print(type(tup2))

list1 = [5]
print(type(list1))
"""
# Properties of  tuple :
->  Tuple is immutable data type, we can not modify once it is defined.
->  Tuple follows the positive and negative indexing as like string and list
->  All type of data can be part of the tuple, like int. float, string, list, tuple, dict, set, boolean
->  Tuple is faster than list to access the data.
"""

print("_"*50)
################# dictionary data type ############
dict1 = {'name' : 'Rahul', 'age' : 20, 'address' : 'Mumbai'}
#       {key : value}
"""
Dictionary properties
->  Dict is mutable data type, we can modify it any point of time
->  All keys should be unique in the dict, duplicate keys are not allowed.
->  Only immutable data type can key in the dict, e.g int, float, string, tuple, boolean.
->  We can set all type of data as dict value , int, float, string, list, tuple, set, boolean.
->  Dict does not follow any indexing, it stores the data un-structure order.
"""

print(dict1, type(dict1))
# <class 'dict'>

# Dict is mutable data type, we can modify it any point of time
dict1['email'] = "rahul@gmail.com"
print(dict1)

dict2 = {}
dict2['phone'] = 956755657
print(dict2) # {'phone': 956755657}

print(dict1['address'])  # Mumbai

# All keys should be unique in the dict, duplicate keys are not allowed.

dict3 = {'a' : 123, 'b' : 567, 'a' : 333, 'c': 789}
print(dict3)  # {'a': 333, 'b': 567, 'c': 789}


# Only immutable data type can key in the dict, e.g int, float, string, tuple, boolean.
dict4 = {}
dict4[3] = [5, 6, 7]
dict4['Hello'] = {'name' : 'john', 'age': 25}
dict4[(2, 4, 6)] = "Python Programming"

print(dict4)
# {3: [5, 6, 7], 'Hello': {'name': 'john', 'age': 25}, (2, 4, 6): 'Python Programming'}

# dict4[[4, 7, 8]] = 463565 # We can not add list as key
#print(dict4) # TypeError: unhashable type: 'list'

# dict4[{'a': 123}] = "Good Morning" # # We can not dict as key
#print(dict4)  # unhashable type: 'dict'

# dict does not follow indexing
# print(dict4[0])  #KeyError: 0


school = {
    'admin' : [
        {'username': 'user1', 'email': 'user1@gmail.com'},
        {'username': 'user2', 'email': 'user2@gmail.com'},
    ],
    'teachers' : {
        'physics' : [
                { 'teach_name': 'teach1', 'email': 'teach1@gmail.com'},
                { 'teach_name': 'teach2', 'email': 'teach2@gmail.com'},
        ],
        'maths' : [
                { 'teach_name': 'math_teach1', 'email': 'math_teach1@gmail.com'},
                { 'teach_name': 'math_teach2', 'email': 'math_teach2@gmail.com'},
        ]
    },
    'student' : []
}
print(school['teachers']['physics'][1]['email'])
# teach2@gmail.com

######################### set data type ########################
print("_"*50)

set1 = {4, 7, 'a', 'b', 7, 5, 3, 4}
print(set1, type(set1))

"""
# Properties of the set
-> Set is mutable data type, we can modify the data at any point of time.
-> Set only store unique data, duplicate data is not allowed.
-> All the immutable data type can be member of set, int, string, float, tuple, boolean.
-> Any mutable data type can not be a member of se e.g list, dict, set
-> Set store the data in random order, it does not follow any indexing.
"""

# Set is mutable data type, we can modify the data at any point of time.
print(dir(set))
set2 = {4, 6, 8, 4}
set2.add(50)
print("set2 :", set2) # {8, 50, 4, 6}

# repeated will not consider, 4 will consider only once.

# -> All the immutable data type can be member of set, int, string, float, tuple, boolean.
set3= {4, 3.5, 'Hello', (4, 7, 8), True}
print(set3) # {True, 3.5, 4, (4, 7, 8), 'Hello'}

# Any mutable data type can not be a member of se e.g list, dict, set

# set4 = {[4, 6, 7], 6, 8, 9}
# print(set4)
# TypeError: unhashable type: 'list'

# set4 = {6, 8, 9, {'a': 123, 'b': 345}}
# print(set4)
# TypeError: unhashable type: 'dict'

set6 = set()
set6.add(50)
print("set6 :", set6)

# var1 = int()
# var2 = str()
# var3 = list()
# var4 = tuple()

############### Boolean  Data type###########
# Boolean data represent with True or False
# Boolean is immutable data type.
var1 = 200
var2 = 100
var3 = 200
print(var1 == var2) # False
print(var1 == var3) # True