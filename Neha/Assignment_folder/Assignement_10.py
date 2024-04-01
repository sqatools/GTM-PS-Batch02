"""
Write a Python  Program using slicing concepts in Strings
1)Slicing
2)Slice from the start
3)Slice to the end
4)Negative Indexing
5)Concatenation of Strings
"""

#fabonacci series
num = 10
x,y = 0,1

for i in range (x,num):
    z = x + y
    x = y
    y = z
    print(z,end=" ")

#
# #factorial
fact = 1
num = 5

for i in range(num, 0 , -1):
    fact = fact * i
print("fact: ", fact)