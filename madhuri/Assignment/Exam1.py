"""
Write a python program to find the duplicate names from given string.
str1 = “Rahul Mohit John Rahul Vaibhav John”
Output = “Rahul John”
"""
str1 = "Rahul Mohit John Rahul Vaibhav John"
strlist1 = str1.split(" ")
dup_word = []

for i in range(len(strlist1)-1):
    for j in range(i+1, len(strlist1)):
        if strlist1[i] == strlist1[j]:
            dup_word.append(strlist1[i])

print("Find the duplicate names from given string: ", dup_word)

"""
Write Python Program to move all positive number on left side and negative values on right side.
Input: [2, -16, 6, 44, -71, 18, -11, -1]
Output: [2, 6, 44, 18, -16, -71, -11, -1]
"""
input1 = [2, -16, 6, 44, -71, 18, -11, -1]
negative_list = []
positive_list = []
for val in input1:
    if val > 0:
        positive_list.append(val)
    if val < 0:
        negative_list.append(val)

new_list = positive_list + negative_list
print("move all positive number on left side and negative values on right side: ", new_list)

"""
Write a Python program find the longest word from given string.
str1 = “India is best cricket Team in the World”
output = “cricket”
"""
str1 = "India is best cricket Team in the World"
strlist = str1.split(" ")
max_count = 0
max_word = ''

for val in strlist:
    if len(val) > max_count:
        max_count = len(val)
        max_word = val
print("longest word from given string: ", max_word)



"""
Write a Python Program to create calculator for different math operation,
add,
multiple,
subtraction and
division.
user has to take three inputs from command line, val1 to decide the math operation, then
val2 and val2 for performing match operation.
"""


def calculator(val1, val2, val3):
    if val1 == "add":
        addition = val2 + val3
        print("_" * 50)
        print("addition: ", addition)
        print("_"*50)
    elif val1 == 'subtract':
        addition = val2 - val3
        print("_" * 50)
        print("subtraction: ", addition)
        print("_" * 50)
    elif val1 == 'multiply':
        addition = val2 * val3
        print("_" * 50)
        print("multiplication: ", addition)
        print("_" * 50)
    elif val1 == 'division':
        addition = val2 / val3
        print("_" * 50)
        print("division: ", addition)
        print("_" * 50)
    else:
        print("Please provide proper math operation name to perfrom")


val1 = input("Enter name of math operation you want to perform (e.g add/subtract/multiply/division) : ")
val2 = float(input("Enter Value 1: "))
val3 = float(input("Enter Value 2: "))
calculator(val1, val2, val3)


