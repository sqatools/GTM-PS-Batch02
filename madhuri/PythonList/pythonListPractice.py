"""
1). Python program to calculate the square of each number from the given list.
"""
list1 = [3, 5, 7, 1, 8]
list2 = []
for val in list1:
    list2.append(val**2)
print("square of list is: ",list2)
print("_"*100)

"""
2). Python program to combine two lists.
"""
#Input lists
list3 = [3, 6, 7, 81, 2]
list4 = [11, 15, 17, 13]

list5 = list3 + list4
print(list5)

#or

list3.extend(list4)
print(list3)
print("_"*100)

"""
3). Python program to calculate the sum of all elements from a list.
"""
#Input list
list6 = [2,5,8,0,1]
sum = 0

for val in list6:
    sum = sum + val
print("Sum of all elemet in the list is: ",sum)
print("_"*100
      )
"""
4). Python program to find a product of all elements from a given list.
"""
#Input list
list7 = [3,6,9,2]
product = 1

for val in list7:
    product = product * val
print("Product of all element from list is: ", product)

#or
product_all_elm = 1
count = 0
while count < len(list7):
    product_all_elm = product_all_elm * list7[count]
    count = count + 1
print("Product of all element in the list is: ", product_all_elm)

#or
prod = 1
for i in range(len(list7)):
    prod = prod * list7[i]
print("Product of all element in the list is: ", prod)
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
print("Max Value from list is: ", max_num)

min_num = list8[0]
#assume first index value is min

for i in range(len(list8)):
    if min_num > list8[i]:
        min_num = list8[i]
print("Minimum Value from the list is: ", min_num)


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
print("Even elements from the list: ", even_list)
print("Odd elements from the list: ", odd_list)
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
#print("New List: ", new_list)

#Remove Duplicate Values from the list

unique_list = []
for val in dup_list:
    if val not in unique_list:
        unique_list.append(val)
print("Removed duplicate values from the list is: ", unique_list)
print("_"*100)
"""
Doubt 8. Python program to print a combination of 2 elements from the list whose sum is 10.
"""
comb_list= [2,5,8,5,1,9]
result = tuple()
for i in range(len(comb_list)):
    for j in range(i+1, len(comb_list)):
        #combination = sum(comb_list[i],comb_list[j])
        combination = comb_list[i] + comb_list[j]
        if combination == 10:
            print(comb_list[i], '=', comb_list[j])
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

for i in range(len(list1)):
    for j in range(len(list2)):
       if list1[i] == list2[j]:
            #if list1[i] not in output_list:
            output_list.append(list1)
#print("11. Get common elements from two lists: ",output_list)

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
print("Print the list in reverse order using while loop: ", new_list)
print("_"*100)

"""
14. Python program to reverse a list using index slicing.
"""
list1 = [1, 2, 3, 4, 55]
print("Reverse a list using index slicing: ",list1[::-1])

"""
15). Python program to reverse a list with reversed and reverse methods.
"""
list1 = [1, 2, 3, 4, 55]
