print("welcome to the pycharm")

# average of 2 numbers
int1 = 10
int2 = 20
avg = int1 + int2
print ("Average of Two no is",avg/2)
print ("Average of Two no is",(int1+int2)/2)
print("-"*40)
"""
#finding the biggest no
x = int(input("Please enter the value of x:"))
y = int(input("please enter the value of y:"))
z = int(input("please enter the value of z:"))
if x>y and x>z:
    print("x is greater:", x)
elif y>x and y>z:
    print("Y is greater:",y)
elif z>x and z>y:
    print("z is greater:",z)
else:
    print("please enter the valid no")
"""
# finding the median of given numbers.
list1 = [4, 6, 99, 5, 9]
"""
#list1.sort()
n = len(list1)
#print(list1, n)
print("the median no is :", (n+1)//2)
"""
n = len(list1)
n =n//2
print(list1[n])