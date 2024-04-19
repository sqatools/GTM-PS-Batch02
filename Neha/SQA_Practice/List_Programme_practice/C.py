#21). Python program to check whether the given list is palindrome or not. (should be equal from both sides).
# list20 = [1,2,3,4,32,2,1]
#
# rev_list20 = list20[-1::-1]
#
# if list20 == rev_list20:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#22). Python Program to get a list of words which has vowels in the given string.
# Input = "www Student ppp are qqqq learning Python vvv"
# #Output : [‘Student’, ‘are’, ‘learning’, ‘Python’]
#
# output_list22 = [ ]
# list_22 = Input.split(" ")
# print (list_22)
#
# for  words in list_22:
#     for char in words:
#         if char == 'a'or char == 'e'or char == 'i'or char == 'o'or char == 'u':
#             output_list22.append(words)
#             break
# print(output_list22)
#
# #23). Python program to add 2 lists with extend method.
# lista = [4, 5, 7, 9, 2, 1]
# listb = [2, 5, 8, 3, 4, 7]
#
# lista.extend(listb)
# print(f"Extended list: {lista}")

#24 Python program to sort list data, with the sort and sorted method.

# list24 = [9,23,4,5,6,7,21]
#
# list24.sort()
# print(list24)
# list24.sort(reverse=True)
# print(list24)
#
# #Sorted
# out_list24 = sorted(list24)
# output_list24 = sorted(list24,reverse=True)
# print(output_list24)
# print(out_list24)

#25 Python program to remove data from the list from a specific index using the pop method.
#
# list25 = [9,23,4,5,6,7,21]
#
# list25.pop(-2)
# print(list25) #removed value is 7
#
# #26). Python program to get the max, min, and sum of the list using in-built functions.
#
# list26 = [9,23,4,5,6,7,21]
# out_max = max(list26)
# out_min = min(list26)
# out_sum = sum(list26)
# print(f"Max value: {out_max} \n"f"Min Value : {out_min}\n"f"Sum Value: {out_sum}")

#27). Python program to check whether a list contains a sublist.

list27 = [9,23,4,5,6,7,21]

sub_list27 = [21,23]
count = 0

for i in list27:
    for j in sub_list27:
        if i == j:
            count+=1

if count == len(sub_list27):
    print ("Sublist existed")
else:
    print("Sublist not existed")

#29). Python program to find the second largest number from the list.
#30). Python program to find the second smallest number from the list.
list_29 = [9,23,4,9,99,111,5,6,7,21]
list_29.sort()
print(list_29)
final_output_largestno = list_29.pop(-2)

final_output_smallestno = list_29.pop(2)

print(f"second largest no:{final_output_largestno}\n"f"second smallest no:{final_output_smallestno}")
