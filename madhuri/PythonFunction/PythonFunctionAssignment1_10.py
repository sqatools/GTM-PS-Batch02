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
"""