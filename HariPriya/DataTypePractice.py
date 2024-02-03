"""
Python is a OOP language
Not 100%
Scripted programming language

Python data type

1)Numbers
  a)Integer
  b)Float
  c)Complex

2)Sequential data
a)String    -immutable
b)List      - mutable
c)Tuple     - immutable

3)Dictionary - mutable
4)Set - mutable
5)Boolean
"""

#Integer

var1 = 2
var2 = 456
var3 = 47659785046749698754548666666694
print(type(var1), "\n")                                     #To know the type of data value
print(type(var2))                                          #<class 'int'>
print(type(var3))                                         #By default \n one line

var4 = int

"""
Properties of Integer

1)Integer is immutable data type - can't be changed once defined
2)Any whole number is considered as integer
3)There is no specific range or limit for integer value, any long number can be defined
"""

print("_"*50)

#float data type

vara = 67.76
varb = 6677.878
varc = 33444.887

print(type(vara))                                           #<class 'float'>
print(type(varb))                                           #Any decimal number
print(type(varc))

"""
Properties of float

1)float is immutable data type - can't be changed once defined
2)Any decimal number is considered as integer
3)There is no specific range or limit for integer value, any long decimal number can be defined
"""

#Complex numbers only j not any other alphabets
val = 4+5j                                                  #4,5 are real numbers ,4 in real part ,5 in imaginary part
print(val)
val2 = 534766+6.87j
print(val2,type(val2))

var8 = 800                                                  #same variable diff values ,value overridden
var9 = 1000                                                 #most recent value
print(var1)

print("_"*60)
######Sequential data type######

#String

str1 = "H"
str2 = 'Hello'
str3 = """
  Prints the values to a stream, or to sys.stdout by default.
    
      sep
        string inserted between values, default a space.
      end
        string appended after the last value, default a newline.
      file
        a file-like object (stream); defaults to the current sys.stdout.
      flush
        whether to forcibly flush the stream.
 """



str4 = ' '                                                                                     #indentation error if space is there str1 no space from beginning
str5 = '''
   sep
        string inserted between "values", default a space.
      end
        string appended after the last value, default a newline.
      file
        a file-like object (stream); defaults to the current sys.stdout.
 '''
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))
print(str5,type(str5))

strm = "Python"
# 0 1 2 3 4 5                      +ve indexing           right to left        takes space as well
" P y t h o n"
# -6 -5 -4 -3 -2 -1                -ve indexing           left to right

print(strm)
print(strm[2],strm[-4])

strb = "Hello Good"                    # takes space as well
print(strb[9])
#print(strb[10])                       #string index out of range  exception only 9   creates a breakpoint ,terminates

"""
Properties of String
1)String is immutable
2)String follows positive and negative indexing
3)We can store any long raw data as String inside ' '    " "     """  ''


# List data type

  #      0  1      2       3
list1 = [3,4.5,'Hello' ,[4,8,7]]                #Heterogenous data
#       -4  -3   -2        -1
#follows indexing

print(list1,type(list1))
print(list1[2])
print(list1[-3])

print(list1[3])                                #[4, 8, 7]
print(list1[3][1])                             #8

listb = [5,7,9]
listb.append(20)                               #existing data can be modified , changed mutable
print(listb)                                   #append , add at the end of the list
listb[1]=100
print(listb)

"""
List is mutable data type, we can modify List at any point of time
List follows the similar positive and negative indexing as like String
All type of data can store in the list..like int,float,String,boolean,dict,list,tuple,set
If we compare list and tuple, then list is bit slower than tuple
"""

print("_"*50)

#######Tuple######

#       0    1     2          3         4     5
tup1 = (3, 4.5 , 'Python' ,[3,5,6], (3,2,1), True)
#      -6   -5      -4       -3        -2     -1

tup2 =(4)                       #<class 'int'>
print(type(tup2))

tup3 =(4,)                       #<class 'tuple'>
print(type(tup3))

list6 = [5]
print(type(list6))              #<class 'list'> , even if single element 5 still []

print(tup1)
print(type(tup1))
print((tup1[3]))             #[3, 5, 6]
print((tup1[3][1]))          #5
print((tup1[-4]))            #Python
print((tup1[-4][1]))         #y

print(dir(tuple))
print(dir(list))

"""
Properties of tuple
1)Tuple is immutable data type ,we cant change once defined, if you dont want to change , if its fixed , like 7 days in a week , days in a month
2)Tuple follows the positive and negative indexing As like String and list
3)All type of data can be part of the tuple,like int,float,String,list,tuple,dict,set,boolean
4)Tuple is faster than list to access the data
"""

#############dictionary data type ##############
###key-value pair####
dict1 = {'name' : 'Rahul','age' : 20, 'address' : 'Mumbai'}             #key not duplicated, value can be duplicated

"""
Dictionary properties
1)Dict is mutable data type, we can modify it any point of time
2)All keys are unique in the dict, values can be duplicated
3)Can store only immutable data type can be the key in the dict, eg, int,float,string,tuple,boolean.
4)We can set all type of data as dict value, int, float,list,string,tuple,boolean
5)Does not follow any indexing, it stores the data un-structure order
"""

print(dict1,type(dict1))                   #<class 'dict'>

#dict is mutable data type, we can modify it any point of time
dict1['email'] = "rahul@gmail.com"        #{'name': 'Rahul', 'age': 20, 'address': 'Mumbai', 'email': 'rahul@gmail.com'} add to existing one
print(dict1)

dict2 = {}
dict2['phone'] = 987654321
print(dict2)

print(dict1['address'])                   #Mumbai

#All keys should be unique in the dict,duplicate keys not allowed
dict3 = {'a': 123, 'b' : 567, 'a':654, 'c':543}                      #Latest one is shown
print(dict3)

#Can store only immutable data type can be the key in the dict, eg, int,float,string,tuple,boolean.
dict4 = {}
dict4[3] = [5,6,7]
dict4['Hello'] = {'name':'john','age':25}
dict4[(2,4,6)] = "Python program"
print(dict4)

#Try list as key not possible
# dict5={}                                              #define and then use
# dict5[[4,7,8]] = 76543
# print(dict5)                                          #TypeError: unhashable type: 'list' error
#
# dict4[{'a': 123}] = "Good"                              #TypeError: unhashable type: 'dict'
# print(dict4)
#
# #dict does not follow indexing
# print(dict4[0])                                        #If program is terminated , its stopping and cant proceed

school = {'admin' : [
    {'username': 'user1','email':'user1@gmail.com'},
    {'username': 'user2','email':'user2@gmail.com'}
],
          'teachers':
              {
              'physics':
                  [
                  {'teach_name': 'teach1','email':'teach1@gmail.com'},
                  {'teach_name': 'teach2','email':'teach2@gmail.com'},
                  ],

              'maths':[
                  {'teach_name': 'mathteach1', 'email': 'mathteach1@gmail.com'},
                  {'teach_name': 'mathteach2', 'email': 'mathteach2@gmail.com'},

              ]
              },
          'student': []
}
print(school['teachers']['physics'][1])

######Set data type#######
### In curly braces
#Unique data
#All immutable data type can be member
#Random order
#No duplicates allowed

set1 = {4,7,'a',7,4,3,'b'}
print(set1,type(set1))                       # <class 'set'>

"""
Properties of set
1)Mutable data type , can modify data at any point of time
2)Set only store unique data, duplicates not allowed
3)All immutable data type can be member of set, int,string,float,tuple,boolean
4)Any mutable data type cannot be a member of set eg) list,dict,set
5)Set store the data in a random order
6)Not follow indexing

"""

print(dir(set))
set2 = {4,6,8,4}
set2.add(50)
print("set2:" ,set2)                #set2: {8, 50, 4, 6} any order

set3 = { 4,3.5,'Hello',(4,7,8),True}
print(set3)

#4)Any mutable data type cannot be a member of set eg) list,dict,set
#Set is mutable but no mutable elements inside in it

#set4 = {6,8,9,{'a':123,'b':657}}
#print(set4)

set6 = set()
set6.add(50)
print("set6: ",set6)

#var1 = int()
#var2 = str()
#var3 = list()
#var4 = tuple()

########Boolean
#Represents True or False
#Immutable data type

var1 = 200
var2 = 100
var3 = 100
print(var1 == var2)  #False
print(var2 == var3)  #True







