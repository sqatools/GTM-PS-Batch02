#pending 3,4,8,9,10,13 ascii
"""1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5,
between 1500 and 2700 (both included).

for i in range (1500,2700):
    if i%7==0 and i%5==0:
        print(i,end=" ")
"""

"""2). Python Loops program to construct the following pattern, using a nested for loops.
Output :
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

for i in range(6):
    print(i* " *")
for i in range (4,-1,-1):
    print(i* " *")
"""
"""
3). Python Loops program that will add the word from the user to the empty string using python.
Input: “python”
Output : “python”"""





"""
4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
Output :
Number of even numbers: 4
Number of odd numbers: 5
a=(1, 2, 3, 4, 5, 6, 7, 8, 9)
even =0
odd = 0
for i in a:
    if i%2==0:
        even+=1

    else :
        odd+=1

print("even numbers are ", even)
print("odd numbers are ", odd)
"""

"""5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.

for i in range(0,7):
    if i!=3 and i!=6:
        print(i, end=(" "))
"""

"""6). Write a program to get the Fibonacci series between 0 to 20 using python.
Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
num1=0
num2=1
count =0
while count<20:
    print(num1,end= (" "))
    n2=num1+num2
    num1=num2
    num2=n2
    count +=1
"""

"""7). Write a program that iterates the integers from 1 to 30 using python. 
For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
For numbers that are multiples of both three and five print “FizzBuzz”. 

for i in range(1,31):
    if i%3==0 and i%5==0 :
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0 :
        print("Fizz")
"""

"""10). Python for loop program to print the alphabet pattern ‘O’ using python.
Output:
  ***  
*       *
*       *
*       *
*       *
*       *
   ***  
"""


"""11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.
n=int(input("enter number "))
count=1
while count<=n:
    print(count,end=" ")
    count +=1
"""

"""
12). Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.
n=int(input("enter num"))
count=n
while count != 0:
    print(count,end=(" "))
    count-=1
"""

"""14). Python Loops program to print all even numbers between 1 to 100 in python.

for i in range (1,101):
    if i%2==0:
        print(i,end=" ")
"""
"""15). Python Loops program to print all odd numbers between 1 to 100 using python.
for i in range (1,101):
    if i%2==1:
        print(i,end=(" "))
"""
"""
16). Python Loops program to find the sum of all natural numbers between 1 to n using python.
n=int(input("enter value "))
total=0
for i in range (1,1+n):
    total+=i
print(total)
"""













