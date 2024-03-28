"""
Properties :
-> List is mutable data type, we can modify at any point of time.
-> List can contains all type of data.
-> List follows the positive and negative indexing as like string.
"""


"""1 Python program to calculate the square of each number from the given list.

2). Python program to combine two lists.

3). Python program to calculate the sum of all elements from a list.

4). Python program to find a product of all elements from a given list.

5). Python program to find the minimum and maximum elements from the list.

6). Python program to differentiate even and odd elements from the given list.

7). Python program to remove all duplicate elements from the list.

8). Python program to print a combination of 2 elements from the list whose sum is 10.

9). Python program to print squares of all even numbers in a list.

10). Python program to split the list into two-part, the left side all odd values and the right side all even values.
Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
Output = [5, 7, 11, 17, 19, 2, 8, 12, 22]
"""

#1
# list1 = [9,8,7,5,4,4,3,2,2,1]
#
# for val in list1:
#     print( val**2,"Square value of:",val)

# #2
# list2= [9,8,7]
# list3 = [6,5,4,3]
# list2.extend(list3)
# print(list2)

#3). Python program to calculate the sum of all elements from a list.

# list4=[1,2,3,4,5]
# sum=0
#
# for i in range (len(list4)+1):
#     sum = i+sum
# print(sum)
#
# print(sum(list4))

#4). Python program to find a product of all elements from a given list.
#
# list5=[1,2,3,4,9,3,6,7,1]
# val=1
#
# for i in list5:
#     val = val*i
# print(val)
#
# #5). Python program to find the minimum and maximum elements from the list.
#
# print(max(list5))
# print(min(list5))
# print(sorted(list5))
# print(list5)

#write the python code for all the values count
#in the list and then remove the duplicates

# list = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
#
# #count value
# values_count = {value:list.count(value) for value in list}
# #remove duplicates
# unique_list = (set(list))
#
# print(f'Count of all values:{values_count}')
# print(f"Unique list:{unique_list}")

#2). Python program to combine two lists.
# list_a = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
# list_b = [1, 2, 3, 4, 5, 6]
#
# list_a.extend(list_b)
# print(list_a)

#6). Python program to differentiate even and odd elements from the given list.
# list_6 = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4, 1, 2, 3, 4, 5, 6]
# odd_list = [ ]
# even_list = [ ]
#
# for i in list_6:
#     if i%2 == 0:
#         even_list.append(i)
#     else:
#         odd_list.append(i)
#
# print(odd_list)
# print(even_list)

#7). Python program to remove all duplicate elements from the list.
# list_6 = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4, 1, 2, 3, 4, 5, 6]
# list_d2 = []
#
# # list_d = set(list_6)
# # print(list_d)
#
# for i in list_6:
#     if i not in list_d2:
#         list_d2.append(i)
# print(list_d2)

#8). Python program to print a combination of 2 elements from the list whose sum is 10.



