# 1) Write a python program to find the duplicate names from given string.
# str1 = “Rahul Mohit John Rahul Vaibhav John”
# Output = “Rahul John”


# 2) Write a Python program find the longest word from given string.
# str1 = “India is best cricket Team in the World”
# output = “cricket”


# 3) Write a Python Program to create calculator for different math operation, add, multiple, subtraction and division.
# user has to take three inputs from command line, val1 to decide the math operation, then
# val2 and val2 for performing match operation.

# 4) Write Python Program to move all positive number on left side and negative values on right side.
# Input: [2, -16, 6, 44, -71, 18, -11, -1]
# Output: [2, 6, 44, 18, -16, -71, -11, -1]


# 5) What is the output of the following code?

x = 10

if x > 5:
    print("A")
if x > 7:
    print("B")
if x > 15:
    print("C")
else:
    print("D")


# a) A B C D
# b) A B D
# c) A D
# d) B D


# 6) What is the output of the following code?

x = 5
if x > 3:
    if x < 7:
        print("A")
    elif x < 10:
       print("B")
    elif x < 7:
       print("C")
    else:
      print("D")

# a) A
# b) B
# c) C
# d) D

# 7) What is the output of the following code?

for i in range(1, 6):
    if i == 3:
      continue
      print(i)

# a) 1 2 4 5
# b) 1 2 3 4 5
# c) 1 2 3
# d) 1 2 4

# 8) What is the output of the following code?

my_dict = {'grapes': 2, 'banana': 3, 'blue-berry': 4}

for key in my_dict:
    print(key)


# a) grapes banana blue - berry
# b) 1 2 3
# c) 0 1 2
# d) TypeError: ‘int’ object is not iterable

# 9) Which method is used to convert an integer to a string in Python?

# a) int_to_string()
# b) convert_to_string()
# c) str()
# d) to_string()

# 10) Which method is used to check if a string contains only lowercase characters?

# a) islower()
# b) islowercase()
# c) islowerchar()
# d) islc()


# 11) What is the output of the following code?

# text = “Hello World”
# print(text.join(“-“))

# a) Hello World!
# b) Hello - World!
# c) H - e - l - l - o - -W - o - r - l - d
# d) Error


#12) What is the output of the following code?

# string = “i am learning python”
#
# list1 = string.split(” “)
#
# print(list1)

# a) [“i”, “am”, “learning”, “python”]
# b) [“i am learning python”]
# c) [“i”, “am”, “learning”, “p”, “y”, “t”, “h”, “o”, “n”]
# d) [“i”, “, ”, “am”, “, ”, “learning”, “, ”, “python”]

#13) What is the output of the following code?

list1 = [2, 3, 4, 7, 8, 1, 5, 6, 2, 1, 8, 2]

index_list = [0, 3, 5, 6]

new_list = []

for value in index_list:
    new_list.append(list1[value])

print(new_list)


# a) [2, 7, 1, 5]
# b) [3, 4, 1, 6]
# c) [2, 4, 1, 5]
# d) [7, 3, 1, 6]

# 14) What is the output of the following code?

list1 = [("mike", 1), ("sarah", 20), ("jim", 16)]

dict1 = {}

for val in list1:
    dict1[val[0]] = val[1]

print(dict1)

# a) {‘mike’: 1, ‘sarah’: 20, ‘jim’: 16}
# b) {‘mike’: 1, ‘sarah’: 20, ‘jim’: 16, ‘val’: 1, ‘val’: 20, ‘val’: 16}
# c) {‘mike’: 1, ‘sarah’: 20, ‘jim’: 16, 0: ‘mike’, 1: ‘sarah’, 2: ‘jim’}
# d)Error


