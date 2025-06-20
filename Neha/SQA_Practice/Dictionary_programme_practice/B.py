#
print(dir(dict))
#
# #12 Python Dictionary program to sort a dictionary in python using values.
# Input = {'d' : 14, 'b': 52,  'a': 13, 'c': 1 }
# # Output= (c, 1) (a,13) (d, 14) (b, 52)
#
# out= {key : value for key,value in sorted(Input.items(),key = lambda item :item[1])}
# print(out)
#
# #13Python Dictionary program to add a key in a dictionary.
# Input= {1:'a', 2:'b'}
# # Output= (1:’a’, 2:’b’, 3:’c’}
#
# Input[3]= 'c'
# print(Input)
#
# #14). Python Dictionary program to concatenate two dictionaries.
# D1 = {'name' : 'yash', 'city' :  'pune'}
# D2 = {'course' : 'python', 'institute' : 'sqatools'}
#
# D1.update(D2)
# print(D1) #{'name': 'yash', 'city': 'pune', 'course': 'python', 'institute': 'sqatools'}

#15). Python Dictionary program to swap the values of the keys in the dictionary.
# Input = {'name':'yash', 'city': 'pune'}
# # Output = {name:’pune’, city: ‘yash’}
#
# Output = {}
#
# for key,values in Input.items():
#     Output[key] = values
#
# print(Output)
#
# #20 20). Python Dictionary program to create a dictionary in the form of (n^3) i.e. if key=2 value=8
# # Input: n=4
# #Output ={1 : 1, 2 : 8, 3 : 27, 4 : 64}
#
# i = int(input("Enter the numeric value:"))
# out_dict = {}
#
# for i in range (1,5):
#     out_dict.update({i:i**3})
#
# print(out_dict)

#21). Python Dictionary program to insert a key at the beginning of the dictionary.
# dict1 = { 'course' : 'python' , 'institute' : 'sqatools' }
# dict2 =  {'name' : 'Neha' }
# # Output= { ‘name’ : ’omkar’, ‘course’ : ’python’, ‘institute’ : ’sqatools’}
# dict2.update(dict1)
# print(dict2)

#Python Dictionary  program to create a dictionary where keys are between 1 to 5 and values are squares of the keys.
#Output ={1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25}
#
# i = int(input("Enter the value between 1-5:"))
# out_dict = {}
#
# for i in range (1,i+1):
#     out_dict.update({i:i**2})
#
# print(out_dict)

#23 23). Python Dictionary program to find the product of all items in the dictionary.
# Input = { 'a': 2, 'b' : 4, 'c' : 5}
# # Output = 40
# result = 1
#
# for i in Input.values():
#     result = result*i
# print(result)

#24). Python Dictionary program to remove a key from the dictionary.
# Input = {'a':2,'b':4,'c':5}
# # Output = (a:1,b:4}
#
# Input.pop('c')
# print(Input)

#25). Python Dictionary program to map two lists into a dictionary.

# list1 = [ 'name', 'sport', 'rank', 'age']
# list2 = ['Neha', 'QA professional', '1',  '32']
# # Output =  { ‘name’ : ’virat’, ‘sport’ : ’cricket’, ‘rank’: 1, ‘age’ : 32}
#
# out_dict = {}
#
# for i in range (len(list1)):
#     if i < len(list2):
#         out_dict[list1[i]] = list2[i]
#     else:
#         None
#
# print(out_dict)
#
# #26). Python Dictionary program to find maximum and minimum values in a dictionary.
# Dict = { 'a' : 10, 'b' : 44 , 'c' : 60, 'd' : 25}
# # Output :
# # Maximum value: 60
# # Minimum value: 10
# list1 =[]
#
# for value in Dict.values():
#     list1.append(value)
#
# print(f"Maximum value in Dictionary:{max(list1)}")
# print(f"minimum value in Dictionary:{min(list1)}")

#28 28). Python Dictionary program to replace words in a string using a dictionary.
string = 'learning python at sqa-tools'
Dict = { 'at' : 'is', 'sqa-tools' : 'fun'}
# Output = ‘learning python is fun’

for key,value in Dict.items():
    string = string.replace(key,value)

print(string)

