

# 26th Feb 2024
# 10. reverse() : This method any given list and modify the original list

list1 = [4, 7, 92, 8, 1, 12]
list1.reverse()

print("list 1:", list1) #  [12, 1, 8, 92, 7, 4]

# reversed() function : this function take list as input and reverse the list values with interator object and
# loop
list2 = [5, 8, 2, 9, 11, 55]
result = reversed(list2)
print("result :", result)
for val in result:
    print(val, end=" ")
# 55 11 9 2 8 5

#### reverse the list with slicing ####
list3 = [5, 7, 8, 92, 3]
print(list3[::-1])
# [3, 92, 8, 7, 5]


# Inbuilt function
# get sum of list value
list4 = [5, 7, 8, 3, 1]

print("sum of list value :", sum(list4))
print("Max value from list :", max(list4))
print("Min value from list :", min(list4))


lista = ["Hello", "Howreterte", "Are", "You", "Hope", "YOu", "doing", "good"]
print("longest word :", max(lista, key=len)) # Howreterte
print("Smallest word :", min(lista, key=len))  # Are

# listc = [5, 7, 8, "H", "W"]
# print(max(listc))
# TypeError: '>' not supported between instances of 'str' and 'int'


print("_"*50)
################################ Deep copy and Shallow Copy ##################
# shallow copy #
# In shallow copy if we change the values in copied list and it will reflect on original list as well

listp = [5, 7, 9, 12]
listq = listp
listr = listq
lists = listr
listr.append(100)

print("listp :", listp, id(listp)) #  [5, 7, 9, 12, 100]
print("listq :", listq, id(listq)) #  [5, 7, 9, 12, 100]

# Deep Copy
# In deep copy if we change the values in the copies list, then changes will not reflect in original list.
listx = [5, 7, 33, 22]
listy = listx.copy()
listy.append(30)

print("listx :", listx, id(listx))
print("listy :", listy, id(listy))

######################## List Comprehension ################################
print("#"*50)

list1 = [5, 7, 8, 2, 3]
#output = [25, 49, 64, 4, 9]

output = []
for val in list1:
    sqr = val**2
    output.append(sqr)
print("output :", output)

# loop with list comprehesion
result = [x**2 for x in list1]
print("result :", result)

str1 = "We are Learning Python Programming"
upper_result = [word.upper() for word in str1.split(" ")]
#upper_result = [word.upper() for word in str1]
print("upper list:", upper_result)
#  ['WE', 'ARE', 'LEARNING', 'PYTHON', 'PROGRAMMING']

output = " ".join(upper_result)
print("output :", output)
# WE ARE LEARNING PYTHON PROGRAMMING

# list comp with if else condition
lista = [5, 7, 8, 2, 1, 6]
#output = [(5, "odd"), (7, "odd"), (8, "even"), (2, "even"), (1, "odd"), (6, "even")]
# if we have if else condition then we have to write in left most position of the loop
output = [(val, "even") if val%2 == 0 else (val, "odd") for val in lista]
print("output :", output)

# get even length word
# if we have only if condition then write it to the right most of the loop
word_list = ['WE', 'ARE', 'LEARNING', 'PYTHON', 'PROGRAMMING']
result = [word for word in word_list if len(word)%2 == 0]
print("result :", result) # ['WE', 'LEARNING', 'PYTHON']


# Python program to print a combination of 2 elements from the list whose sum is 10.
















