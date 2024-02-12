#Python Datatypes
"""
1)Numbers
Integer
Float
Complex

2)Sequential Data
String
List
Tuple

3)Dictionary
4.Set
5.Boolean
"""
##########Integer data type

var1 = 40
print(type(var1),var1)

print("-"*50)

"""
=Properties
-Integer is immutable datatype.
-Any whole number will be consider as Integer.
-There is  no Specific range or limit for Integer Value,We can define any long number as Integer.
"""

#########float datatype

a = 13.598
print(type(a),a)

"""
=Properties
-Float is immutable datatype.
-Any decimal number will be consider as float.
-There is no specific range or limit for float value.

"""
print("-"*50)

##########Complex datatype
Var1 = 4+5j
print(type(Var1),Var1)
"""
Complex number will be define with j.
-Scientific Calculation
-Imaginary number.
-Real Number.
"""
print("-"*50)

##########Sequential datatype
######String
Str1 = "H"
Str2 = 'Hello'
Str3 =  """ Hi Everyone This is Chinmayi Nayak.I am student of python selenium batch 02 student."""
Str4 = 'Hello "Good Morning" World'
Str5= "Hi 'Have a Nice Day' Everyone"

print(type(Str1),Str1)
print(Str1,'\n',Str2,'\n',Str3,'\n',Str4,'\n',Str5)

Stra = "python"

#python
#012345 - Positive Indexing,-6-5-4-3-2-1 - Negative Indexing

print(Stra[1],Stra[2],Stra[-2])

#Properties
"""
String is immutable datatype.
String follow postive & Negative Indexing.
No Specific range for Storage.
"""
print("-"*50)
##############list

list1 = [3,4.567,'hello',[5,7,8,5]]
print(type(list1),list1)

print(list1[1],list1[2])

print(list1[-1][-2],list1[-1][-3])

#Mutable

list2 = [4,6,7,40]
print(type(list2),list2)

list2.append(30)#append in the existing list
print(list2)

list2[1] = 50#replace the data using indexing
print(list2)

#properties
"""
It's a combination of all the datatypes,All type of datatype can  be stored in the list.
List is mutable datatype ,Can modify the data in the list at any point.
list follow Positive & Negative Indexing.
If we compare list with tuple then list is bit slow than tuple.
"""
print("-"*50)
#########Tuple
