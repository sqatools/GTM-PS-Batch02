"""
1). Python Program to add two integer values.
2). Python Program to subtract two integer values.
3). Python program to multiply two numbers.
4)Python program to repeat a given string 5 times.
Input :
str1 = “SQATools”
Output :
“SQAToolsSQAToolsSQAToolsSQAToolsSQATools”
5)Python program to get the Average of given numbers.
6). Python program to get the median of given numbers.----???
7). Python program to print the square and cube of a given number.
8). Python program to interchange values between variables.
9). Python program to solve this Pythagorous theorem.
Theorem : (a2 + b2 = c2)
10). Python program to solve the given math formula.
Formula : (a + b)2 = a^2 + b^2 + 2ab

"""
import selenium

## Python Program to add two integer values.

i1=4
i2=5
sum_1 = i1+i2
print(sum_1)

## Python Program to subtract two integer values.

i1=9
i2=5
subtract = i1-i2
print(subtract)

## Python program to multiply two numbers.

i1=5
i2=5
multiply = i1*i2
print(multiply)

## Python program to repeat a given string 5 times.

str1 = "SQATools"
str2 =  str1 * 5

print(str2)

## Python program to get the Average of given numbers.
#Formula: sum of all the number/ total number

a = 40
b = 50
c = 30
output = (a+b+c)/3
print(output)

## Python program to get the median of given numbers.
## Note: all the numbers should be arranged in ascending order
## Formula : (n+1)/2

##numbers = [45, 60, 61, 66, 70, 77, 80]
##add_values= print(sum(numbers))
##median = (add_values+1) / 2
##print(median) ##-Not able to find out the median

##Python program to print the square and cube of a given number.
# a= 40

square = a**2
print(square)
cube = a*a*a
print(cube)

##Python program to interchange values between variables

a = 10
b = 20
a,b = b,a
print (a,b)

##Python program to solve this Pythagorous theorem.
##Theorem : (a2 + b2 = c2)
a = 10
b = 20
Theorem = sqrt((a*a) + (b*b))
print (Theorem)

##Python program to solve the given math formula.
##Formula : (a + b)2 = a^2 + b^2 + 2ab

a=10
b=20

LHS=(a+b)**2
print(LHS)
RHS=((a)**2) + ((b)**2) + (2*a*b)
print(RHS)

if RHS==LHS:
    print ("LHS is equal to RHS'")
else:
    print('LHS is not equal to RHS')
