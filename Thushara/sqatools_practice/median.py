# Program to get the median of the given numbers
# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter the number of elements :"))
# iterating till the range

for i in range(0 , n) :
    element = int(input("Enter number "+ str(i+1)+":"))
    lst . append(element)
print(lst)
lst.sort()
print(lst)
n = len(lst)
m = int((n+1)/2)

print(lst[m-1])








