
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

#12 Python program to reverse a list with for loop.

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

# list_16 = [8, 7, 6, 55,1]
#
# clone_list16 = list_16.copy()
# print(clone_list16)

#17 Python program to return True if two lists have any common member.

# lista = [4, 5, 7, 9, 2, 1]
# listb = [2, 5, 8, 3, 4, 7]
#
# for i in lista:
#     for j in listb:
#         if i == j:
#             print (f"{i} is common value in both list hence printing {True}")

#18). Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.
#Need answers
# list18 = [2, 5, 8, 3, 4, 7,8]
# output_list18 = [ ]
#
# if list18.pop(1) for i in list18:
#     list18.pop()

#19 Python program to remove negative values from the list.
# list19 = [2, 5, -18, 3,0, 4, -7,8]
#
# for i in list19:
#     if i >= 0:
#         print(i, end=" ")

#20). Python program to get a list of all elements which are divided by 3 and 7.
# list20 = [2, 49, 18, 3,21, 4, 7,8]
# output_list20 = []
#
# for i in list20:
#     if i%3 == 0 or i%7==0:
#         output_list20.append(i)
# print(f"print the final list of elements which divisible by 3 and 7: {output_list20}")







