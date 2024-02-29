# dict1 = {'key' : 'value'}

"""
#properties :
 ->  dict store the data in key value formate
 ->  dict is mutable data type, we can modify at any point of time.
 ->  Only immutable data type can be key in the dict e.g int, float, string, tuple, boolean
 ->  All type of data can value in the dict, int, float, string, list, tuple, dict, set, boolean
 ->  dict only contains unique keys, it means duplicate keys are not allowed.
     if we defined duplicate key then latest defined data will be considered.
"""

dict1 = {'a' : 456,
         4: 'Hello',
         4.5 : [4, 7, 8],
         (1, 4, 6) : {'a' : 4567, 'b' : 123},
         True : {5, 7, 9, 2},
         }

print(dict1)
# {'a': 456, 4: 'Hello', 4.5: [4, 7, 8], (1, 4, 6): {'a': 4567, 'b': 123}, True: {9, 2, 5, 7}}

# access data from dict
print(dict1[True])   # {9, 2, 5, 7}
print(dict1[4.5][1]) # 7

# add new data to the dict
dict1[False] = [4, 7, 8, 2, 5]

print(dict1)
# {'a': 456, 4: 'Hello', 4.5: [4, 7, 8], (1, 4, 6): {'a': 4567, 'b': 123}, True: {9, 2, 5, 7}, False: [4, 7, 8, 2, 5]}

str = "Python"
str_list = list(str)
print(str_list)
list1= [4,6,8,2,9,10]
output = {}

for i in range(len(str_list)):
    output[str_list[i] * 2] = list1[i]
print(output)
