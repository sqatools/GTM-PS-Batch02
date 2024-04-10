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
Input = {'name':'yash', 'city': 'pune'}
# Output = {name:’pune’, city: ‘yash’}

Output = {}

for key,values in Input.items():
    Output[key] = values

print(Output)