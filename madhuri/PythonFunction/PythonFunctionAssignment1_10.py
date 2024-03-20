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
    print(listdata)


sum_three_number([6,9,4,5,3])