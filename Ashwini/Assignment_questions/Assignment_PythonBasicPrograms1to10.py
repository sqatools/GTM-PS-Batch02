# Program to add two integer values
a = 2
b = 5
c = a + b
print("addition of two integer value is: ", c)

# Program to subtract two integer values
x = 200
y = 50
sub = x - y
print("suntraction of two integer value is: ", sub)

#program to multiply two numbers.

mul = a * b
print("Multiplication of two integer value is: ", mul)

#program to repeat a given string 5 times

str1 = "SQATools"
res = str1 * 5
print(res)

#program to get the Average of given numbers.
#Formula: sum of all the number/ total number

a = 40
b = 50
c = 30

Total = a + b + c
avg = Total // 3
print("Average of given numbers is: ", avg)

#program to print the square and cube of a given number.

num1 = 9
square_root = 9 ** 2
cube_root = 9 ** 3
print("Square root of 9 is: ", square_root)
print("cube root of 9 is: ", cube_root)

#program to get the median of given numbers.
'''
Note: all the numbers should be arranged in ascending order
Formula : (n+1)/2
n = Number of values
Input : [45, 60, 61, 66, 70, 77, 80]
Output:  66
'''
list = [45, 60, 61, 66, 70, 77, 80, 90]
list.sort()
l1= list[3] + list[4]
res = l1//2
print("median value is: ", res)


#program to interchange values between variables.

a = 10
b = 20
a, b = b, a
print(a, b)

#program to solve the given math formula.
#Formula : (a + b)2 = a^2 + b^2 + 2ab


a = 2
b = 3
#LHS
LHS = (a + b)**2
print("LHS: ", LHS)

#RHS
RHS = (a**2) + (b**2) +(2 * a * b)
print("RHS: ", RHS)


l1 = [1, 2, 3,4,7]
l1.sort()
n = len(l1) # length of the list
m = n // 2 # middle index
print("middle index", m)
# Check if the length is even or odd
if n % 2 == 0:
    res = (l1[m - 1] + l1[m]) / 2 # l1[3-1] + l1[3] = l1[2] + l1[3] = 7/2
    print(res)
else:
    res_1= (n + 1) / 2
    print(res_1)



num = int(input("enter a number: "))
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag == True:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")


#
