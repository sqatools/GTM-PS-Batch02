"""
Program: write a python get below result
str1 = "Python"
list1 = [4, 6, 8, 2, 9, 10]
output = {'PP' : 4, 'yy' : 6, 'tt' : 8, 'hh': 2, 'oo': 9, 'nn' : 10}
"""

str = "Python"
str_list = list(str)
list1= [4,6,8,2,9,10]
output = {}

for i in range(len(str_list)):
    output[str_list[i] * 2] = list1[i]
print("output: ",output)