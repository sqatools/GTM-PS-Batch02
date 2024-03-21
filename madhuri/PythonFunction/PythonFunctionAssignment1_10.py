"""
1). Python function program to add two numbers.
"""
def addition(num1, num2):
    addition = num1 + num2
    print('1. addition: ',addition)


addition(5, 6)
print()
print("*"*50)
"""
2). Python function program to print the input string 10 times.
"""


def string_10times():
    print("2. print input string 10 times: ")
    print("string"*10, end=" ")


string_10times()
print()
print("*"*50)

"""
3). Python function program to print a table of a given number.
"""


def print_table(number):
    print("3. table of a given number: ")
    for i in range(1, 11):
        print(i*number, end=" ")


print_table(5)
print()
print("*"*50)

"""
4). Python function program to find the maximum of three numbers.

Input: 17, 21, -9
Output: 21
"""

def maximum_num(num1,num2,num3=-9):
    if num1 > num2 and num1 > num3:
        print("4. Num1 is greater: ", num1)
    elif num2 > num1 and num2 > num3:
        print("4. Num2 is greater: ", num2)
    else:
        print("4. Num3 is greater: ", num3)



maximum_num(17,21,-9)
print()
print("*"*50)

"""
5). Python function program to find the sum of all the numbers in a list.
Input : 

Output: 27
"""

def sum_three_number(listdata):
    addition = 0
    for val in listdata:
        addition = addition + val
    print("5. sum of all the numbers in a list: ", addition)


sum_three_number([6,9,4,5,3])
print()
print("*"*50)


"""
6). Python function program to multiply all the numbers in a list.
Input : [-8, 6, 1, 9, 2]
Output: -864
"""

def multiply_all_numbers(numlist):
    multiplication = 1
    for val in numlist:
        multiplication = val * multiplication
    print("6. Multiply all numbers in a list: ", multiplication)


multiply_all_numbers([-8, 6, 1, 9, 2])
print()
print("*"*50)


"""
7). Python function program to reverse a string.
Input: Python1234
Output: 4321nohtyp
"""

def reverse_string(input_str):
    print("7. To reverse a string: ", input_str[::-1])

reverse_string('Python1234')
print()
print("*"*50)

"""
8). Python function program to check whether a number is in a given range.
Input : num = 7, range = 2 to 20
Output: 7 is in the range
"""


def number_in_range(num,range_start,range_end):
    if num in range(range_start, range_end):
        print("8. ", True)
    else:
        print("8. ", False)


number_in_range(7,2,20)
print()
print("*"*50)

"""
9). Python function program that takes a list and returns a new list with unique elements of the first list.
Input : [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
Output : [2, 3, 1, 4, 6 ]
"""
print()
print("*"*50)