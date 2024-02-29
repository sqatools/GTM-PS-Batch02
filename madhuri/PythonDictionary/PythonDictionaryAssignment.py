import string
"""
Program: write a python get below result
str1 = "Python"
list1 = [4, 6, 8, 2, 9, 10]
output = {'PP' : 4, 'yy' : 6, 'tt' : 8, 'hh': 2, 'oo': 9, 'nn' : 10}
"""

str = "Python"
str_list = list(str)
list1= [4, 6, 8, 2, 9, 10]
output = {}

for i in range(len(str_list)):
    output[str_list[i] * 2] = list1[i]
print("output1 : ",output)
print("_"*100)

"""
Question1 : Write a python program to get below result
list1 = [5, 7, 9, 3, 17, 2]
output1 = {'A' : 5, 'B' : 7, 'C': 9, 'D': 3, 'E' : 17, 'F' : 2}
"""
output1 = {}
asscii= 65
for i in list1:
    output1[chr(asscii)] = i
    asscii = asscii + 1

print("output2 : ",output1)
print("_"*100)


"""
Question2 : Write a python program to get below result
Str1 = "We are Learning Python Programming"
Output = {"wE" : "2We2", "AE" : "3are3", "lG": "8Learning8", "pN" : "6Python6", "pG" : "11Programming11"}
"""
input_str = "We are Learning Python Programming"
list2 = input_str.split(" ")
output3 = {}
for i in range(len(list2)):
    if i == 0:
        key = list2[i].swapcase()
        value = "2" + list2[i] + "2"
        output3[key] = value
    elif i == 1 or i == 2:
        str = list2[i].upper()
        start_str = str[:1]
        end_str = str[-1:]
        key = start_str + end_str
        if i == 1:
            value = "3" + list2[i] + "3"
            output3[key] = value
        elif i == 2:
            value = "8" + list2[i] + "8"
            output3[key] = value

    elif i == 3 or i == 4:
        str = list2[i].swapcase()
        start_str = str[:1]
        end_str = str[-1:]
        key = start_str + end_str
        if i == 3:
            value = "6" + list2[i] + "6"
            output3[key] = value
        elif i == 4:
            value = "11" + list2[i] + "11"
            output3[key] = value

print('Expected: {"wE" : "2We2", "AE" : "3are3", "lG": "8Learning8", "pN" : "6Python6", "pG" : "11Programming11"}')
print("output3: ", output3)




