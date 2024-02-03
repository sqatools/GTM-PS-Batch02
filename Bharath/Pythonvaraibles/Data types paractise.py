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



"""