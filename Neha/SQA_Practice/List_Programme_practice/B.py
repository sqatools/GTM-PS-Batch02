"""
11).  Python program to get common elements from two lists.
Input =
list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
Outputt : [4, 5, 7, 2]

12). Python program to reverse a list with for loop.

13). Python program to reverse a list with a while loop.

14). Python program to reverse a list using index slicing.

15). Python program to reverse a list with reversed and reverse methods.

16). Python program to copy or clone one list to another list.

17). Python program to return True if two lists have any common member.

18). Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.

Solution
19). Python program to remove negative values from the list.

Solution
20). Python program to get a list of all elements which are divided by 3 and 7.

Solution
21). Python program to check whether the given list is palindrome or not. (should be equal from both sides).

Solution
"""

#11 Python program to get common elements from two lists.

# list1 = [4, 5, 7, 9, 2, 1]
# list2 = [2, 5, 8, 3, 4, 7]
# # Output : [4, 5, 7, 2]
#
# list3 = [ ]
#
# for i in list1:
#     if i in list2:
#         list3.append(i)
#
# print(list3)

#Python program to reverse a list with for loop.

# list12 = [2, 5, 8, 3, 4, 7]
#
# for i in range(len(list12)-1,-1,-1):
#     print(list12[i] , end = " ")

# list12.reverse()
# print(list12)

#13). Python program to reverse a list with a while loop.

# list13 = [2, 5, 8, 3, 4, 7]
# count = len(list13)-1
#
# while count >= 0:
#     for value in list13:
#         print (value[count],end=" ")
#         count -= 1

#14 Python program to reverse a list using index slicing.

# list14 = [1,2,3,4,5,6,7,8]
# rev_list14 = list14[-1::-1]
#
# print(rev_list14)
#15-Python program to reverse a list with reversed and reverse methods.
#
# list_15 = [8, 7, 6, 5, 4, 3, 2, 11,16,91]
#
# list_15.reverse()
# print(list_15)
#print("Reversed List:",list(reversed(list_15)))

#16). Python program to copy or clone one list to another list.

list_16 = [8, 7, 6, 55,1]

clone_list16 = list_16.copy()
print(clone_list16)




