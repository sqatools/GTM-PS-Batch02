# #find max element
#
# """list=[5,8,9,56,98,12]
#
#
# max=list[0]
# n=len(list)
#
# for i in range (1,n):
#     if list[i]>max:
#         max=list[i]
# print(max)"""
#
# #find min values
#
# min=list[0]
# n=len(list)
#
# for i in range(1,n):
#     if list[i]<min:
#         min=list[i]
# print(min,"is the minimum value in the list")  """

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
# input_values = [1, "cat", "dog", True, 10, 6.7, [4, 6, 7]]
# for data in input_values:
#     print(data)
#     if isinstance(data, bool):
#         print("this is bool value :", data)
#     elif isinstance(data, str):
#         print("this is string value :", data)
#     elif isinstance(data, float):
#         print("this is float value :", data)
#     elif isinstance(data, list):
#         print("this is list value :", data)
#     elif isinstance(data, int):
#         print("this is int value :", data)
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

#Python program to print all the numbers from 10-15 except 13

# input_num=int(input("enter number between 10-15:"))
#
# for i in range(10,16):
#     if i != 13:
#         print(i)

#Python program to find the electricity bill. According to the following conditions:
# Up to 50 units rs 0.50/unit
# Up to 100 units rs 0.75/unit
# Up to 250 units rs 1.25/unit
# above 250 rs 1.50/unit
# an additional surcharge of 17% is added to the bill
# Input = 350
# Output = 438.75

unit_consumed = int(input("Enter the unit consumed:"))
total_bill_amount=0

for unit in range (1,unit_consumed+1):
    if unit<=50:
        total_bill_amount = total_bill_amount + (.50)
    elif unit>50 and unit<=100:
        total_bill_amount=total_bill_amount+ .75
    elif unit>100 and unit<=250:
        total_bill_amount = total_bill_amount+1.25
    elif unit>250:
        total_bill_amount = total_bill_amount + 1.50

bill_amount_surcharge= total_bill_amount+total_bill_amount*(17/100)
print("bill_amount_surcharge:",bill_amount_surcharge)




