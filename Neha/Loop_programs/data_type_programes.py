# Python program to check whether the given number is an integer or not.

#
# number = input("enter the number:")
# if type(number) == int:
#     print("True")
# else:
#     print("False")
#
# # Python program to check whether the given number is float or not.
# number_2 = input("enter the float number:")
# if type(number_2) == float:
#     print("True")
# else:
#     print("False")
#
# # Python program to check whether the given input is a string or not.
# number_3 = input("enter the string:")
# if type(number_3) == str:
#     print("True")
# else:
#     print("False")

#Write a program for find the type of all input values
input_values = [1, "cat", "dog", True, 10, 6.7, [4, 6, 7]]
for data in input_values:
    print(data)
    if isinstance(data, bool):
        print("this is bool value :", data)
    elif isinstance(data, str):
        print("this is string value :", data)
    elif isinstance(data, float):
        print("this is float value :", data)
    elif isinstance(data, list):
        print("this is list value :", data)
    elif isinstance(data, int):
        print("this is int value :", data)
#
# #Python program to check whether the given input is a string or not.
# #Input = ‘sqatools’
# #Output = True
#
# input = input("Enter the string:")
#
# if isinstance(input,str):
#     print("True")
# else:
#     print("Other datatype")