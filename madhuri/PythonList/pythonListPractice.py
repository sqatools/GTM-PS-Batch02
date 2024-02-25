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

print(len(dup_list)-1)
print(dup_list[7])

"""new_list = []

for i in range(len(dup_list)-1):
    if dup_list[i] == dup_list[i+1]:
        new_list = dup_list[i]
print(new_list)"""

new_list = []
for i in range(len(dup_list)-1):
    print(dup_list[i], '=', dup_list[i+1])
    if dup_list[i] == dup_list[i+1]:
        new_list.append(dup_list[i])
        #add occurance of duplicate value
    else:
        continue
print("New List: ", new_list)


