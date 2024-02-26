"""
1). Python program to calculate the square of each number from the given list.
"""
list1 = [3, 5, 7, 1, 8]
list2 = []
for val in list1:
    list2.append(val**2)
print("1. square of list is: ", list2)
print("_"*100)

"""
2). Python program to combine two lists.
"""
#Input lists
list3 = [3, 6, 7, 81, 2]
list4 = [11, 15, 17, 13]

list5 = list3 + list4
print("2. Soln1 combine two lists", list5)

#or

list3.extend(list4)
print("2. Soln2 combine two lists", list3)
print("_"*100)

"""
3). Python program to calculate the sum of all elements from a list.
"""
#Input list
list6 = [2,5,8,0,1]
sum = 0

for val in list6:
    sum = sum + val
print("3. Sum of all elemet in the list is: ",sum)
print("_"*100)
"""
4). Python program to find a product of all elements from a given list.
"""
#Input list
list7 = [3,6,9,2]
product = 1

for val in list7:
    product = product * val
print("4. Product of all element from list is: ", product)

#or
product_all_elm = 1
count = 0
while count < len(list7):
    product_all_elm = product_all_elm * list7[count]
    count = count + 1
print("4. Soln1 = Product of all element in the list is: ", product_all_elm)

#or
prod = 1
for i in range(len(list7)):
    prod = prod * list7[i]
print("4. soln2 = Product of all element in the list is: ", prod)
print("_"*100)

"""
5). Python program to find the minimum and maximum elements from the list.
"""
list8 = [23, 560, 12, 89]
#assume first index value is max value
max_num = list8[0]

for i in range(len(list8)):
    if max_num < list8[i]:
        max_num = list8[i]
print("5. Max Value from list is: ", max_num)

min_num = list8[0]
#assume first index value is min

for i in range(len(list8)):
    if min_num > list8[i]:
        min_num = list8[i]
print("5. Minimum Value from the list is: ", min_num)
print("_"*100)

"""
6.Python program to differentiate even and odd elements from the given list.
"""
og_list = [23, 11, 78, 90, 34, 55]
even_list = []
odd_list = []

for i in range(len(og_list)):
    if og_list[i] % 2 == 0:
        even_list.append(og_list[i])
    else:
        odd_list.append(og_list[i])
print("6. Even elements from the list: ", even_list)
print("6. Odd elements from the list: ", odd_list)
print("_"*100)

"""
7.Python program to remove all duplicate elements from the list. 
"""
dup_list = [5, 7, 8, 8, 5, 0, 7, 7]

#Get next duplicate value from the list
new_list = []
for i in range(len(dup_list)-1):
    #print(dup_list[i], '=', dup_list[i+1])
    if dup_list[i] == dup_list[i+1]:
        new_list.append(dup_list[i])
        #add occurance of duplicate value
    else:
        continue
# print("7. New List: ", new_list)

#Remove Duplicate Values from the list

unique_list = []
for val in dup_list:
    if val not in unique_list:
        unique_list.append(val)
print("7. Removed duplicate values from the list is: ", unique_list)
print("_"*100)
"""
Doubt 8. Python program to print a combination of 2 elements from the list whose sum is 10.
"""
comb_list = [2, 5, 8, 5, 1, 9]
output_list = []

for i in range(len(comb_list)):
    for j in range(i+1, len(comb_list)):
        #combination = sum(comb_list[i], comb_list[j])
        combination = comb_list[i] + comb_list[j]
        if combination == 10:
            output_list.append((comb_list[i],comb_list[j]))
            # print(comb_list[i], '=', comb_list[j])
print("8. Combination of 2 elements from the list whose sum is 10 is: ", output_list)
print("_"*100)

"""
9. Python program to print squares of all even numbers in a list.
"""
square_input_list = [2, 4, 7, 8, 5, 1, 6]
square_list = []

for val in square_input_list:
    if val % 2 == 0:
        square_list.append(val**2)
print("9. Square of even numbers in list is: ", square_list)
print("_"*100)

"""
10). Python program to split the list into two-part, the left side all odd values and the right side all even values.
Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
Output = [5, 7, 11, 17, 19, 2, 8, 12, 22]
"""
Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]

odd_list = []
even_list = []

for val in Input:
    if val%2 != 0:
        odd_list.append(val)
    else:
        even_list.append(val)
odd_list.extend(even_list)
print("10. left side all odd values and the right side all even values: ", odd_list)
print("_"*100)


"""
Doubt 11).  Python program to get common elements from two lists.
Input =
list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
Outputt : [4, 5, 7, 2]
"""
list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
output_list = []

#solution1
for i in range(len(list1)):
    for j in range(len(list2)):
       if list1[i] == list2[j]:
            if list1[i] not in output_list:
                output_list.append(list1[i])

print("11. Get common elements from two lists: ", output_list)

#solution2
common_list = []
for val in list1:
    if val in list2:
        common_list.append(val)
print("11. Get common elements from two lists: ", common_list)
print("_"*100)

"""
12. Python program to reverse a list with for loop.
input = [1, 2, 3, 4, 55]
output = [55, 4, 3, 2, 1]
"""
list1 = [1, 2, 3, 4, 55]
new_list = []
#print(list1[::-1])

for i in range(len(list1)-1,-1,-1):
    new_list.append(list1[i])
print("12. program to reverse a list with for loop: ", new_list)
print("_"*100)

"""
13.Problem to print the list in reverse order using while loop
"""
list1 = [1, 2, 3, 4, 55]
count = len(list1) - 1
new_list = []
while count >= 0:
    new_list.append(list1[count])
    count = count - 1
print("13. Print the list in reverse order using while loop: ", new_list)
print("_"*100)

"""
14. Python program to reverse a list using index slicing.
"""
list1 = [1, 2, 3, 4, 55]
print("14. Reverse a list using index slicing: ",list1[::-1])

"""
15). Python program to reverse a list with reversed and reverse methods.
"""
list1 = [1, 2, 3, 4, 55]
print('15. Reverse list with reverse methods: ', list(reversed(list1)))

#solution2
print('15. Reverse list with reverse methods: ', list1.reverse())
print("_"*100)

"""
16.Python program to copy or clone one list to another list.
"""

listp = [1, 50, 70, 15, 20]
listq = listp.copy()
print('16. Copy or clone one list to another list: ', listq)
print("_"*100)

"""
17. Python program to return True if two lists have any common member.
"""
list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
result = False

for val in list1:
    if val in list2:
        result = True
print("17. Return True if two lists have any common member: ", result)
print("_"*100)

"""
Doubt 18. Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.
"""
#list1 = [2, 5, 8, 3, 4, 7, 10, 17, 29]
list1 = [3, 4, 8, 7, 0, 1, 6, 9]
result_list = []

for i in range(len(list1)):
    if i!=3 and i!=1 and i !=6:
        #print(list1[i], end=" ")
        result_list.append(list1[i])
    else:
        continue
print("18. list after removing the 1st, 3rd, and 6th elements", result_list)
print("_"*100)

#Solurion2

list1 = [3, 4, 8, 7, 0, 1, 6, 9]

list1 = [element for (value, element) in enumerate(list1)
    if value not in (1, 3, 6)]

print("18. list after removing the 1st, 3rd, and 6th elements", list1)
print("_"*100)

"""
19. Python program to remove negative values from the list.
"""
list1 = [3, 5, -8, 0, -20, -55]

print("19. remove negative values from the list: ")
for val in list1:
    if val >= 0:
        print(val, end=" ")
print()
print("_"*100)

"""
20. Python program to get a list of all elements which are divided by 3 and 7.
"""
list1 = [3, 7, 0, 2, 6, 14, 88, 21]
result = []

for val in list1:
    if val % 3 == 0 or val % 7 == 0:
        #print(val, end=" ")
        result.append(val)
print("20. list of all elements which are divided by 3 and 7: ", result)
print("_"*100)

"""
21. Python program to check whether the given list is palindrome or not. (should be equal from both sides).
"""
num = [1, 2, 1]

num2 = num[::-1]

if num == num2:
    print("21. list is palindrome", num)
else:
    print("21. list is not palindrome", num)
print("_"*100)


