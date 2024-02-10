
import math


#Find id address for variables
x = 45
y = 98
z = 27654
print("Id of x : ", id(x))                                  #140706982346552
print("Id of y : ", id(y))                                  #140706982348248
print("Id of z : ", id(z))                                  #2638706459088
                                                            #id() takes exactly one argument (3 given), only one at a time , not possible more than one

#Assign single value to multiple variables
p=q=r = 5
print(p,q,r)

#Assign multiple values to multiple variables at a time
a,b,c = 2,3,4
print(a)
print(b)
print(c)
print(a,b,c)                                               #Can print multiple values at a time, no concatenation required

#Add two integer values
a = 25
b = 5
c=a+b
print("Addition : ",c)

#Subtract two numbers
num1 = 687
num2 = 546
num3 = num1-num2
print("Subtraction : ",num3)

#Multiply two numbers
x1 = 34
x2 = 54.6
x3 = x1*x2
print("Multiplication : ",x3)

#Division of two numbers
firstNumber = 43.89
secondNumber = 26
result = firstNumber/secondNumber
print("Division : ",result)

#Division of two numbers, getting result as whole number or integer not decimal using //
firstNumber = 43.89
secondNumber = 26
result1 = firstNumber//secondNumber
print("Division : ",result1)

#Repeat given String 5 times
string1 = "python"
solution = string1*5
print("Printing Five times of String: ",solution)                        #pythonpythonpythonpythonpython


#Repeat given String 4 times with space
str2 = " java "
solution1 = str2*4
print("Printing four  times of String: ",solution1)                     #java  java  java  java

#Repeat $% special characters for 9 times
str1 = "$%"
print("Printing 9 times :", str1*9)

#Average of given three numbers
p = 6
q = 7
r = 2
average = (p+q+r)/3
print("Average :",average)

#Print square and cube of a number
n1 = 100
squareOfn1 = n1**2                                                       #Power ^ 2 , square
cubeOfn1 = n1**3
print("Square of number : ",squareOfn1)
print("Cube of number : ",cubeOfn1)

#Assign two variables and input and equate all
r = 26
s = 87
equate = r=s                                                             #87 final value is s
print("Equate :", equate)

#Interchange or swap values between variables                            #a,b = b,a
m = 43
n = 24
m,n = n,m
print("value of m : ", m)                                               #value of m :  24
print("value of n : ", n)                                               #value of n :  43

#Pythagoras theorem
#Square on the hypotenuse = Sum of the squares of other two sides
#c^2 = (a+b)^2
side1 = 6
side2 = 5
squareOfTwoSmallerSides =  (side1**2)+(side2**2)
squareOnHypotenuse = squareOfTwoSmallerSides
print("Hypotenuse : ",squareOnHypotenuse)
print("Hypotenuse : ",math.sqrt(squareOnHypotenuse))                     #math.sqrt

#To get the median of given numbers
list = [3,4,2,1,8,9,7]
#Arrange in ascending order
ascendingOrder = list.sort()                                            #1,2,3,4,7,8,9

middlePosition = (len(list))/2                                          #(7+1)/2 = 4th element = middle position ,(n+1)/2
print("Median :",list[int(middlePosition)])










