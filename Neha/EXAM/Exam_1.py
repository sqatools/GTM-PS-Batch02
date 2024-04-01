# 1) Write a python program to find the duplicate names from given string.
# str1 = “Rahul Mohit John Rahul Vaibhav John”
# Output = “Rahul John”

def find_duplicates(str1):
    names = str1.split(" ")
    seen_names = set()                                                # Initialize an empty set to store seen names
    duplicates = []                                                  # Initialize an empty list to store duplicate names
    for name in names:
        if name in seen_names and name not in duplicates:  # If the name has been seen before , it's a duplicate, set does not allow duplicates
            duplicates.append(name)
        else:
            seen_names.add(name)
    return ' '.join(duplicates)

str1 = "Rahul Mohit John Rahul Vaibhav John"
output = find_duplicates(str1)
print("Output:",output)                                      # Output: Rahul John

##############################################################################################################################

# 2) Write a Python program find the longest word from given string.
# str1 = “India is best cricket Team in the World”
# output = “cricket”

longest_word = ' '
long_len = 0
str1 = "India is best cricket Team in the World"
word_list = str1.split(" ")
for word in word_list:
    word_len = len(word)
    if word_len>long_len:
        long_len = word_len
        longest_word = word
print("Longest word:",longest_word)                           # Longest word: cricket

############################################################################################################################

# 3) Write a Python Program to create calculator for different math operation, add, multiple, subtraction and division.
# user has to take three inputs from command line, val1 to decide the math operation, then
# val2 and val3 for performing match operation.

def calculator(operation,val1,val2):
    if operation == "add":
        return val1+val2
    elif operation == "subtract":
        return val1-val2
    elif operation == "multiply":
        return val1*val2
    elif operation == "divide":
        if val2 == 0:
            return "Error:Cannot divide by zero"
        else:
            return val1/val2
    else:
        return "Error:Invalid opeartion"

result = calculator("add",5,4)
print("Result:",result)


########################################################################################################

# 4) Write Python Program to move all positive number on left side and negative values on right side.
# Input: [2, -16, 6, 44, -71, 18, -11, -1]
# Output: [2, 6, 44, 18, -16, -71, -11, -1]

def move_positive_left_negative_right(nums):

      positive_nums = [num for num in nums if num > 0]                         # Partition the list into positive and negative num
      negative_nums = [num for num in nums if num <= 0]

      return positive_nums + negative_nums                                      # Concatenate the positive and negative parts

input_list =  [2, -16, 6, 44, -71, 18, -11, -1]
output = move_positive_left_negative_right(input_list)
print("Output:",output)                                                         # Output: [2, 6, 44, 18, -16, -71, -11, -1]

#########################################################################################################

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

# Solution is  A B D


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

# Solution a) A

# a) A
# b) B
# c) C
# d) D

# 7) What is the output of the following code?

for i in range(1, 6):
    if i == 3:
      continue
    print(i)

# Solution  a) 1 2 4 5

# a) 1 2 4 5
# b) 1 2 3 4 5
# c) 1 2 3
# d) 1 2 4

# 8) What is the output of the following code?

my_dict = {'grapes': 2, 'banana': 3, 'blue-berry': 4}

for key in my_dict:
    print(key)

# Solution a) grapes banana blueberry


# a) grapes banana blueberry
# b) 1 2 3
# c) 0 1 2
# d) TypeError: ‘int’ object is not iterable

# 9) Which method is used to convert an integer to a string in Python?

# Solution c) str()

# a) int_to_string()
# b) convert_to_string()
# c) str()
# d) to_string()

# 10) Which method is used to check if a string contains only lowercase characters?

# Solution  a) islower()

# a) islower()
# b) islowercase()
# c) islowerchar()
# d) islc()


# 11) What is the output of the following code?

text = "Hello World"
print(text.join("-"))

# Solution d) Error

# a) Hello World!
# b) Hello - World!
# c) H - e - l - l - o - -W - o - r - l - d
# d) Error


#12) What is the output of the following code?

string = "i am learning python"

list1 = string.split(" ")

print(list1)

# Solution a) [“i”, “am”, “learning”, “python”]

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

# Solution a) [2, 7, 1, 5]


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

# Solution a) {‘mike’: 1, ‘sarah’: 20, ‘jim’: 16}

# a) {‘mike’: 1, ‘sarah’: 20, ‘jim’: 16}
# b) {‘mike’: 1, ‘sarah’: 20, ‘jim’: 16, ‘val’: 1, ‘val’: 20, ‘val’: 16}
# c) {‘mike’: 1, ‘sarah’: 20, ‘jim’: 16, 0: ‘mike’, 1: ‘sarah’, 2:‘jim’}
# d)Error


