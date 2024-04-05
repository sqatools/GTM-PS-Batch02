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
dict1 = {'name': 'john', 'city': 'Landon', 'country': 'UK'}
dict2 = {}
# Output :
# dict1 = {}
# dict2 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}

for val in dict1:
    dict2[val] = dict1[val]

for value in dict1:
    output_val = dict1.pop(name)
    dict2['name'] = dict2[output_val]

print(dict1)
print(dict2)


