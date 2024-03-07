# dict1 = {'key':value}

"""
#properties:
1) dict store the day in the form of key value pair format
2) dict is mutable data type, we can modify at any point of time
3) Only immutable data type can be key in the dict eg) int,float,string,tuple,boolean
4) All type of data can be in the value in the dict . int,float,string,list,tuple,dict,set,boolean
5)dict only contains unique keys, it means duplicate keys are not allowed
 If we define duplicate key then latest defined data will be considered.

"""

dict1 = {'a':456,
          4:'Hello',
          4.5:[4,7,8],
          (1,4,6):{'a':4567,'b':123},
          True:{5,7,9,2}
         }
print(dict1)   #{'a': 456, 4: 'Hello', 4.5: [4, 7, 8], (1, 4, 6): {'a': 4567, 'b': 123}, True: {9, 2, 5, 7}}

# Access data from dict
print(dict1[True])                        # {9, 2, 5, 7} Set data type random order , insertion order not preserved, no indexing
print(dict1[4.5][1])                      # 7

# add new data to the existing dict
dict1[False] = [4,7,8,2,5]               # Set no indexing

print(dict1)         #{'a': 456, 4: 'Hello', 4.5: [4, 7, 8], (1, 4, 6): {'a': 4567, 'b': 123}, True: {9, 2, 5, 7}, False: [4, 7, 8, 2, 5]}

# Program : Create a dictionary with the given two lists

list1 = ['a','b','c','d']                      # 4 Keys and 4 values matching pair
list2 = [123,456,78,9]
                                               # output = {'a':123,'b':456,'c':78,'d':9
output={}
for i in range(len(list1)):
    output[list1[i]] = list2[i]               # add new data to the existing dict this format

print("Output:",output)                       #Output: {'a': 123, 'b': 456, 'c': 78, 'd': 9}
print("__"*60)

## WAP to get below result

str1 = "Python"
list1 = [4,6,8,2,9,10]

#output = {'PP' : 4, 'yy' : 6 ,'tt' : 8, 'hh' : 2, 'oo' : 9, 'nn' : 10}

output = {}
for i in range (len(str1)):
    output[str1[i]*2] = list1[i]     # Add data to the existing dict
print("Output:",output)             #Output: {'PP': 4, 'yy': 6, 'tt': 8, 'hh': 2, 'oo': 9, 'nn': 10}

print("$$"*60)

############# Apply loop on the dictionary ################
dict2 = {'Name':'Rahul','Age':24,'Address':'Mumbai'}

for data in dict2:
    print(data)                     # Only key printed

# Name
# Age
# Address

print("$$"*60)

for data in dict2.items():           # items will give value as well
    print(data)                     # Key,value printed

# ('Name', 'Rahul')
# ('Age', 24)
# ('Address', 'Mumbai')

print("$$"*60)

for key,val in dict2.items():       # items() method in dict
    print(key,":" ,val)            # key value pair printed

# Name : Rahul
# Age : 24
# Address : Mumbai

# Methods of dict

print(dir(dict))

# 'clear', 'copy', 'fromkeys', 'get', 'items'
# 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

# items() method: This method return the key value pair in the form of tuples

print(dict2.items())                    #dict_items([('Name', 'Rahul'), ('Age', 24), ('Address', 'Mumbai')])

# Get Method: This method return specific value with the help of keys

dict_a = {'a':456,'b':333,'c':123}
val = dict_a.get('c')
print("Value of Key c is :",val)       # 123
print(dict_a['c'])                    # 123 without using get() method

# keys() method: Thsi method returns list of keys , only keys

print(dict_a.keys())                # dict_keys(['a', 'b', 'c'])

# values() method : This method returns list of values

print(dict_a.values())             # dict_values([456, 333, 123])

print("$$"*60)

# update() method : This method updates the data from dict1 to dict2

dict1 = {'name':'John','email':'john@gmail.com','address':'Mumbai'}
dict2 = {'phone':6785445677,'country':'India','occupation':'Business'}

dict1.update(dict2)

print("dict1:",dict1)      # dict1 is updated with dict2 values , both combined
print("dict2:",dict2)      # dict2 remains same, no change

# dict1: {'name': 'John', 'email': 'john@gmail.com', 'address': 'Mumbai', 'phone': 6785445677, 'country': 'India', 'occupation': 'Business'}
# dict2: {'phone': 6785445677, 'country': 'India', 'occupation': 'Business'}

# Remove data from dictionary

# pop() method : This method removes data from the dictionary with the help of key passing inside the pop() method and return the value

dict_b= {'name': 'John', 'email': 'john@gmail.com', 'address': 'Mumbai', 'phone': 6785445677, 'country': 'India', 'occupation': 'Business'}

val = dict_b.pop('address')                   # address Key along with its value removed
print("Remove data:", val)                   #Remove data: Mumbai
print("After Removal of address:",dict_b)

#After Removal of address: {'name': 'John', 'email': 'john@gmail.com', 'phone': 6785445677, 'country': 'India', 'occupation': 'Business'}

# popitem() method: This method remove data from the dictionary in the combination of key and value and return it with tuple combination
# LIFO Last In First Out

dict_c = {'name': 'John', 'email': 'john@gmail.com', 'phone': 6785445677, 'country': 'India', 'occupation': 'Business'}
output = dict_c.popitem()
print("Removed data:",output)            #Removed data: ('occupation', 'Business') last part key and value removed
print("After popitem removal :",dict_c)#After popitem removal : {'name': 'John', 'email': 'john@gmail.com', 'phone': 6785445677, 'country': 'India'}

print("__"*60)
############################################################################
# string , list, tuple sequential data type mostly methods are common
# But dict not follows positive and negative indexing
# Unique Methods in dict

# clear() method: This method remove all data from dict

dict_d = {'name': 'John', 'email': 'john@gmail.com', 'phone': 6785445677, 'country': 'India'}
dict_d.clear()
print("Clears all data:",dict_d)            # Clears all data: {} , blank dict , structure maintained still

#######################
# Remove dict variable from memory using del

dict_e = {'name':'John','email':'john@gmail.com','phone':6567890,'country':'India'}

#del dict_e
#print("dict_e:",dict_e)         # It will completely delete dict from memory
#NameError: name 'dict_e' is not defined. Did you mean: 'dict'?

del dict_e['phone']
print("dict_e:",dict_e)

#dict_e: {'name': 'John', 'email': 'john@gmail.com', 'country': 'India'}

#####################   setdefault method
# If value is there for a key, then same value printed
# If key is not available , then it will take new key and new value

dict_f={'name':'John','email':'john@gmail.com','phone':6567890,'country':'India'}
output=dict_f.setdefault('email','Hello')  #john@gmail.com
print("output:",output)
output=dict_f.setdefault('phone','Hello')  #output: 6567890
print("output:",output)
output=dict_f.setdefault('phone',None)    #output: 6567890
print("output:",output)
output=dict_f.setdefault('DOB',None)  #dict_f: {'name': 'John', 'email': 'john@gmail.com', 'phone': 6567890, 'country': 'India', 'DOB': None}
print("dict_f:",dict_f)

#################################################

list1 = ['a','b','c','d','e']
list2 = [123,456,78,9]
# Output = {'a':123,'b':456,'c':78,'d':9

output = {}
for i in range(len(list1)):                      # IndexError: list index out of range 5 Keys but only 4 values
      if i<len(list2):
        output[list1[i]] = list2[i]
      else:
        output[list1[i]] = None                 # Output: {'a': 123, 'b': 456, 'c': 78, 'd': 9, 'e': None}
print("Output:",output)                         #Output: {'a': 123, 'b': 456, 'c': 78, 'd': 9} Nothing is there for e

#################################################
# Assignment  Questions
# WAP to get below result

#Q1)
# list1 =[5,7,9,3,7,2]
# output={'A':5,'B':7,'C':9,'D':3,'E':17,'F':2}

list1 = [5, 7, 9, 3, 7, 2]

# Define alphabets to assign to elements
alphabets = ['A', 'B', 'C', 'D', 'E', 'F']                        # list

# Calculate the sum of list1 along with alphabets
output = {}
for i in range(len(list1)):
    output[alphabets[i]] = list1[i]

print(output)                               #{'A': 5, 'B': 7, 'C': 9, 'D': 3, 'E': 7, 'F': 2}
print("_"*60)

###################################################

# Question2
Str1 = "We are Learning Python Programming"
Output = {"wE" : "2We2", "AE" : "3are3", "lG": "8Learning8", "pN" : "6Python6", "pG" : "11Programming11"}

Str1 = "We are Learning Python Programming"

# Initialize an empty dictionary to store the output
output = {}

# Iterate through the string Str1
for char in Str1:
    # Check if the character is an alphabet
    if char.isalpha():
        # Count the occurrences of the character in Str1
        count = Str1.count(char)
        # Construct the output string as per the format specified
        output[char.upper() + char.lower()] = str(count) + char.upper() + str(count)

print(output)
print("_"*60)


