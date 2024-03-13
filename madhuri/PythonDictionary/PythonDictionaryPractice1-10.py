"""
how to select multiple var and replace it with another shortcut

"""
"""
1). Python Dictionary program to add elements to the dictionary.
"""
import datetime
input_dict = {}
input_dict['name'] = 'madhuri'
input_dict['phone'] = 9860138618
input_dict['address'] = 'pune'
input_dict['last_seen'] = datetime.date.today()
input_dict['status_is_active'] = True
print("1. program to add elements to the dictionary: ")
print(input_dict)
print("_"*100)

"""
2). Python Dictionary program to print the square of all values in a dictionary.
Input : {‘a’: 5, ‘b’:3, ‘c’: 6, ‘d’ : 8}
Output :
a : 25
b : 9
c : 36
d : 64

Solution
"""
input2 = {'a': 5, 'b': 3, 'c': 6, 'd': 8}
for key, value in input2.items():
    input2[key] = value**2
print("2. print the square of all values in a dictionary: ")
print(input2)
print("_"*100)

"""
3). Python Dictionary program to move items from dict1 to dict2.
Input :
dict1 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
dict2 = {}
Output :
dict1 = {}
dict2 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
"""
dict1 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}
dict2 = {}

for key,value in dict1.items():
    dict2[key] = value
dict1.clear()

print("3. program to move items from dict1 to dict2: ")
print(dict1)
print(dict2)
print("_"*100)

"""
4). Python Dictionary program to concatenate two dictionaries.
Input :
dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’}
dict2 = {‘Age’ : 25, ‘salary’: ‘$25k’}
Output :
dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’, ‘Age’ : 25, ‘salary’: ‘$25k’}
"""
dict1 = {'Name': 'Harry', 'Rollno':345, 'Address': 'Jordan'}
dict2 = {'Age': 25, 'salary': '$25k'}

dict1.update(dict2)
print("4. to concatenate two dictionaries: ")
print(dict1)
print("-"*100)

"""
5). Python Dictionary program to get a list of odd and even keys from the dictionary.
Input :
{1: 25, 5:’abc’, 8:’pqr’, 21:’xyz’, 12:’def’, 2:’utv’}
Output :
Even Key = [[8, ‘pqr’], [12, ‘def’], [2, ‘utv’]]
Odd Key = [[1, 25], [5, ‘abc’], [21, ‘xyz’]]
"""
input3 = {1: 25, 5: 'abc', 8: 'pqr', 21: 'xyz', 12: 'def', 2: 'utv'}
even_key = []
odd_key = []

for key, value in input3.items():
    if key % 2 == 0:
        even_key.append([key, value])
    else:
        odd_key.append([key, value])
print("5. Even Key =", even_key)
print("5. Odd Key =", even_key)
print("_"*100)

"""
6). Python Dictionary Program to create a dictionary from two lists.
Input :
list1 = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’]|
list2 = [12, 23, 24, 25, 15, 16]
Output :
{‘a’: 12, ‘b’: 23, ‘c’: 24, ‘d’: 25, ‘e’: 15}
"""
list1 =['a', 'b', 'c', 'd', 'e']
list2 = [12, 23, 24, 25, 15, 16]
output = {}
for i in range(len(list1)):
    output[list1[i]] = list2[i]
print("6. to create a dictionary from two lists: ")
print(output)
print("_"*100)


"""
doubt: 7. Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
Input :
[4, 5, 6, 2, 1, 7, 11]
Output :
{4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}
"""
input = [4, 5, 6, 2, 1, 7, 11]
output = {}

output = [(val, val**2) if val % 2 == 0 else (val, val**3) for val in input]
print("7. to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension: ")
print(output)
print("_"*100)

"""
8). Python Dictionary program to clear all items from the dictionary.
"""
input = {'name': 'madhuri', 'mobile':  9860138618, 'address': 'pune'}
input.clear()

"""
9). Python Dictionary program to remove duplicate values from Dictionary.
Input :
{‘a’: 12, ‘b’: 2, ‘c’: 12, ‘d’: 5, ‘e’: 35, ‘f’: 5}
Output :
{‘a’: 12, ‘b’: 2, ‘d’: 5, ‘e’: 35}
"""
input = {'a': 12, 'b': 2, 'c': 12, 'd': 5, 'e': 35, 'f': 5}
dict2 = {}

for key, value in input.items():
    if value not in dict2.values():
        dict2[key] = value
print("9. Program to remove duplicate values from Dictionary: ")
print(dict2)

"""
10). Python Dictionary program to create a dictionary from the string.
Input  = ‘SQATools’
Output = {‘S’: 1, ‘Q’: 1, ‘A’: 1, ‘T’: 1, ‘o’: 2, ‘l’: 1, ‘s’: 1}
"""
# input = 'SQATools'
# input_list = list(input)
# print(input_list)
# output = {}
#
# for i in range(len(input_list)-1):
#     for j in range(i+1,len(input_list)-1):
#         if input_list[i]
#         print(input_list[i], '=', input_list[j])
#
# print(output)




