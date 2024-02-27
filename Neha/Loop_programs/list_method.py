##print(dir(list))


"""
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', 
'__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
 '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__',
  '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
   '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy',
    'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

"""
'''
1 Python program to calculate the square of each number from the given list.

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
'''

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

list5=[1,2,3,4]
val=1

for i in list5:
    val = val*i
print(val)

#5). Python program to find the minimum and maximum elements from the list.

print(max(list5))
print(min(list5))