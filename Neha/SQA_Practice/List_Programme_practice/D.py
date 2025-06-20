#31). Python program to merge all elements of the list in a single entity using a special character.

# list31 = ['q','w','e','r','t','y']
# out_list31 = '@'.join(list31)
# print(out_list31)
#
# #32). Python program to get the difference between two lists.
#
# list32_a = [1,2,3,4,5]
# list32_b = [3,4,5,6,7]
#
# for i in list32_a:
#     if i not in (list32_b):
#         print(i,end = " ")

#33). Python program to reverse each element of the list.
# Input = ['Sqa', 'Tools', 'Online', 'Learning', 'Platform']
# #output = [‘aqS’, ‘slooT’, ‘enilno’, ‘gninraeL’, ‘mroftalP’]
# output = []
# for word in Input:
#     output.append(word[-1::-1])
#
# print(output)

#35 35). Python program to get keys and values from the list of dictionaries.

# list1 = [{"a":12}, {"b": 34}, {"c": 23}, {"d": 11}, {"e": 15}]
# # Output :  [‘a’, ‘b’, ‘c’, ‘d’, ‘c’]
# #                 [12, 34, 23, 11, 15]
#
# list_key = []
# list_value = []
#
# for pair in list1:
#     for key in pair:
#         list_key.append(key)
#         list_value.append(pair[key])
# print(list_value,list_key)

#36). Python program to get all the unique numbers in the list.

# list1 = [9,8,7,6,57,8,9,7,5,1]
# print(list(set(list1)))

#37). Python program to convert a string into a list.

# str = "I am QA automation Tester"
#
# final = str.split(" ")
# print(final)

#38). Python program to replace the last and the first number of the list with the word.
list = [12, 32, 33, 5, 4, 7]
# output : [‘SQA’, 32, 33, 5, 4, ‘Tools’]

list[0] = 'SQA'
list[-1] = 'Tools'
print(list)

#39). Python program to check whether the given element is exist in the list or not.
list39 = [9,6,,5,3,2,2]

