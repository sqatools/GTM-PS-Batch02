########################## Assignment 1
import math

############# 1) Python Program to add two integer values

a = 608
b = 5436
add = a+b
print("Addition of two integers :" ,add)

############# 2)Python Program to subtract two integer values

var1 = 7654
var2 = 76546
sub = var1-var2
print("Subtraction of two integers :" ,sub)


############## 3)Python program to multiply two numbers

num1 = 987.6
num2 = 96
mul = num1*num2
print("Multiplication of two numbers: ",mul)

############## 4)Python program to repeat a given string 5 times.
# Input :
# str1 = “SQATools”
# Output :
# “SQAToolsSQAToolsSQAToolsSQAToolsSQATools”

str1 = "SQATools"
fiveTimesOfStr = str1*5
print("Printing five times of given String: " ,fiveTimesOfStr)


################# 5)Python program to get the Average of given numbers
x = 67
y = 564
z = 4325
average = (x+y+z)/3
print("Average of given numbers: ", average)

################ 6)Python program to get the median of given numbers if length is odd

Input = [78,98,34,23,67,45,54]
AscendingOrder = sorted(Input)                                       # Arrange in ascending order
print("List in ascending order :" ,AscendingOrder)
n = (len(AscendingOrder))
print("Total number of values in the list :",n)
Median_n = n//2                                                     # // Gives the quotient only that is integer format, so no need to convert to int
print("Median:" ,AscendingOrder[(Median_n)])

################# 6a) Python program to get the median of given numbers if length is even

print("&" *60)
Input1 = [56,23,87,95,34,46]                                        # length is 6 , index from 0 to 5
AscendingOrder = sorted(Input1)
print("Sorted in Ascending Order : " ,AscendingOrder)
n1 = len(AscendingOrder)
print("Length: ", n1)
### calculate the indices of two middle elements
# n1 is length which is 6, 87 is 3rd element which is if index 2 , 95 is 4th element which is of index 3
firstMiddle_n1 = n1//2                                                             # Index of first middle element
secondMiddle_n2 = (n1//2)-1                                                       # Index of second middle element
Median = (AscendingOrder[firstMiddle_n1]+AscendingOrder[secondMiddle_n2])/2
print("Median : ",Median)
print("&"*60)


################## 7)Python program to print the square and cube of a given number

num7 = 7
SquareOfAGivenNumber = num7**2
print("Square of a given number :" ,SquareOfAGivenNumber)           # ** is power
CubeOfAGivenNumber = num7**3
print("Cube of a given number: ", CubeOfAGivenNumber)

################# 8)Python program to interchange values between variables

p = 10
q = 20
p,q = q,p                                                           # swap
print("p:" ,p)
print("q:" ,q)

################ 9)Python program to solve this Pythagorous theorem

side1 = 6
side2 = 5
hypotenuse = math.sqrt((side1**2)+(side2**2))
print("Hypotenuse - bigger side of the triangle : ", hypotenuse)

################ 10)Python program to solve the given math formula
### Formula : (a + b)2 = a^2 + b^2 + 2ab

a = 8
b = 2
LHS = (a+b)**2
RHS = (a**2)+(b**2)+2*a*b
print(LHS)
print(RHS)
print("LHS = RHS")







