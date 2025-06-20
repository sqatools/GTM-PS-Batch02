"""

{key_expression: value_expression for item in iterable if condition}
eg;
square_dict = {x: x**2 for x in range(1, 6)}
print(square_dict)

Here's a breakdown of the components:
key_expression: An expression that defines the keys of the dictionary.
value_expression: An expression that defines the values of the dictionary.
item: The variable representing each element in the iterable.
iterable: The sequence (like a list, tuple, string, etc.) that you're iterating over.
condition (optional): An optional condition that filters the items. Only items for which this condition is true will be included in the resulting dictionary.
"""




#Python Dictionary program to add elements to the dictionary.




# dict= {}
# dict['Name'] = 'Neha'
# dict['Age'] = 30
#
# print(dict)

#Python Dictionary program to print the square of all values in a dictionary.
# dict = {'a': 5, 'b':3, 'c': 6, 'd' : 8}
# Output :
# a : 25
# b : 9
# c : 36
# d : 64

# for key,val in dict.items():
#     print(key,":", val**2)

#3Python Dictionary program to move items from dict1 to dict2.
# Input :
# dict1 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}
# dict2 = {}
# # Output :
# # dict1 = {}
# # dict2 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
#
# for val in dict1:
#     dict2[val] = dict1[val]
#
# for value in dict1:
#     output_val = dict1.pop(name)
#     dict2['name'] = dict2[output_val]
#
# print(dict1)
# print(dict2)

#4 4). Python Dictionary program to concatenate two dictionaries.
# dict1 = {'Name': 'Harry', 'Rollno':345}
# dict2 = {'Age' : 25, 'salary': '$25k'}
# # Output :
# # dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’, ‘Age’ : 25, ‘salary’: ‘$25k’}
#
# dict1.update(dict2)
# print(dict1)

#Python Dictionary program to get a list of odd and even keys from the dictionary.
# dict_5 = {1: 25, 5:'abc', 8:'pqr', 21:'xyz', 12:'def', 2:'utv'}
# Output :
# Even Key = [[8, ‘pqr’], [12, ‘def’], [2, ‘utv’]]
# Odd Key = [[1, 25], [5, ‘abc’], [21, ‘xyz’]]
#
# odd_list = []
# even_list = []
# count = 0
#
# for data in dict_5:
#     if data%2 == 0:
#         even_list = [data,dict_5[data]]
#         count += 1
#     elif data%2 != 0:
#         odd_list = [data, dict_5[data]]
#         count +=1


# even_list = [[val,dict_5[val]] for val in dict_5 if val%2 == 0]
# odd_list = [[val,dict_5[val]] for val in dict_5 if val%2 != 0]

#6  Python Dictionary Program to create a dictionary from two lists.
# list1 = ['a', 'd', 'e']
# list2 = [12, 23, 24]
# # Output :
# # output dict: {'a': 12, 'd': 23, 'e': 24}
#
# output = {}
#
# for i in range (len(list1)):
#     if i < len(list2):
#         output[list1[i]] = list2[i]
#     else:
#         output[list1[i]] = None
#
# print ('output dict:',output)

#7 Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.

# dict_7 = [4, 5, 6, 2, 1, 7, 11]
# # Output :
# # {4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}
#
# output = {}
#
# for i in dict_7:
#     output[i] = i**2
#
# print(output)


#8 8). Python Dictionary program to clear all items from the dictionary.
# dict_8 = {4: 16, 5: 25, 6: 36, 2: 4, 1: 1, 7: 49, 11: 121}
#
# dict_8.clear()
# print(dict_8)

#9 Python Dictionary program to remove duplicate values from Dictionary.
# dict_9 = {'a': 12, 'b': 2, 'c': 12, 'd': 5, 'e': 35, 'f': 5}
# dict_9b = {}
# # Output :
# # {‘a’: 12, ‘b’: 2, ‘d’: 5, ‘e’: 35}
#
# for key,value in dict_9.items():
#     if value not in dict_9b.values():
#         dict_9b[key] = value
#
# print(dict_9b)
#
#
# dict_x = {'a': 'car', 'b': 'tempo', 'c': 'bus', 'd': 'train', 'e': 'car'}
# dict_xb = {}
# # Output :
# # {‘a’: 12, ‘b’: 2, ‘d’: 5, ‘e’: 35}
#
# for key,value in dict_x.items():
#     if value not in dict_xb.values():
#         dict_xb[key] = value
#
# print(dict_xb)

#10 10). Python Dictionary program to create a dictionary from the string.
str10  = 'SQATools'
#Output = {‘S’: 1, ‘Q’: 1, ‘A’: 1, ‘T’: 1, ‘o’: 2, ‘l’: 1, ‘s’: 1}
str10_output = list(str10)
print(str10_output)
out = {}

for i in str10_output:
    out[i] = str10_output.count(i)

print(out)









