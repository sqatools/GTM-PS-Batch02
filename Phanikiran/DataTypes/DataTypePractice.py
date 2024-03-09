"""
Python data types
1.Numbers
    i. Integers
    ii.Float
    iii.complex
2.Sequential Data
    i.String
    ii.List
    iii.Tuple
3.Dictionary
4.Set
5.Boolean

"""

# Integer data type
print("-----Integer----")
var1 = 2
var2 = 223
var3 = 34535435535353454353543535
var4 = int
print(var1, var2, var3)
print(type(var1), type(var2), type(var3))
print(var4)

"""
- Integer is immutable data type.
- Any whole number will be consider as integer.
- There is no limit for integer value.
"""
print("---" * 50)
# -------------------------- String----------------------------------------#
"""
Properties of string:
- String is immutable
- String follows positive and negative indexing.
- We can store any long value.

"""
Str1 = "Hi"
print(Str1, type(Str1))
print(Str1 * 20)

# +Ve Indexing
#     0 1 2 3 4 5
str2 = "P  Y  T  H  O  N"
#    -6  -5 -4 -3 -2 -1
print(str2[-4])
# --------------------------- List -------------------------------- #
"""
Properties of list:
- List is mutable data type.It can be modified at any point of time.
- List follows positive and negative indexing like string.
- All type of data can be stored in the list like int,float,string,boolean,dict, list, tuple, set.
- Comparatively list is slower than tuple.
- List data values are enclosed with sqaure brackets.
"""
print("-" * 50, "List", "-" * 50)
list1 = [23, 2343, 3453, 676, "this is list", 33.4, True, dict, [33, 4, 5, 52]]
print(list1)
print(type(list1))  # It defines the type of variable
list1[2] = [56, 6, 78]  # It is replacing value of index 2 in the above list 1 variable i.e 3453
print(list1)
# Output: [23, 2343, [56, 6, 78], 676, 'this is list', 33.4, True, <class 'dict'>, [33, 4, 5, 52]]

# -----------------------------------Tuple ----------------------------------------------#
print("-" * 50, "Tuple", "-" * 50)
"""
- Tuple is immutable data type we cannot modify once it is defined.
- Tuple follow the positive and negative indexing.
- It can store all types of data like int,float, string, list, tuple, dict, set, boolean,
- Tuple is faster than list
- Tupe data is enclosed with round brackets.
- Tuple allows duplicate values.
"""
#       0   1   2   3             4     5
tuple1 = (12, 34, 56, [44, 55, 64], 34, "This is tuple")
#       -6  -5   -4  -3           -2    -1
# Positive indexing
print("'Value of index 2'is ", tuple1[0])

# Negative indexing
print("'value of -5", tuple1[-5])
print(tuple1[3][2], tuple1[3])  # Printing values of 3rd indexing
print(type(tuple1))

# ------------------------------------- Dictionary ------------------------------------------------#
print("-" * 50, "Dictionary", "-" * 50)
"""
- Dictionary stores data in the form of key and value.
- Dictionary is mutable data type and it can be modified at any point of time.
- It doesn't support indexing.It stores data un-structure order.
- Dictionary stores data in curly braces.
- It stores different data types like integer, float,list,tuple.
- We cannot initialize list as a key 
"""
dict1 = {"name": "phani", "Roll no:": 546, "Company": "IBM", "Address": "HYDERABAD", "email": "pk@gmail.com"}
print(dict1["email"])
print(dict1["Address"])

dict1["Address"] = "Bangalore"
print(dict1)
# We store values in the form key like '2':23, 'fname':pk, (2,4,3,4):"24"

dict2 = {}
dict2[34] = 233
dict2[(23, 44, 2)] = 234
dict2[(2, 5, 3)] = "Python programming language"
print(dict2)

# school={
#   'admin':[
#        {'username': 'pk', 'email id':'pk@gmail.com'}], "teachers":{['physics':['teacher name':'pk', '']]} }

# ---------------------------------------------- Sets ------------------------------------#
"""
- Set is mutable data type.We can modify data at any point of time.
- Set stores only unique data no duplicate.
- all immutable data type can be member of member of set, int, string, float, tuple, boolean.
- Any mutable data type can not be a member of set eg.list, dist, set
- Set store the data in random order, it does not follow any indexing.
- Set data is enclosed with curly braces {}
"""
print("-" * 50, "Sets", "-" * 50)
set1 = {3, 5, 6, 2, 35, 6, 7}
set2 = {2, 6, 78, 2567, 356}
print(set1, type(set1))
set1.add(33)
print(set1)
# ------------------------------- Boolean --------------------------------- #
print("-" * 50, "Boolean", "-" * 50)
var1 = 100
var2 = 200
print(var1 == var2)

var3 = 300
var4 = 300
print(var3 != var4)
