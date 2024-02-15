"""
    1. 1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
        Input1:1500
        Input2:2700
"""
for i in range(1500,2700):
    if ( i%7 == 0 ) and (i%5==0):
        print("i :",i)
        #print(i, end=" ")

print("_"*100)
"""
2). Python Loops program to construct the following pattern, using a nested for loops.
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
"""
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()


"""
    3). Python Loops program that will add the word from the user to the empty string using python.
    Input: “python”
    Output : “python”
"""
user = "python"

output_str = ''
print(len(user))
for i in range(len(user)):
    output_str=output_str+user[i]
    print('user: ',user[i])
print('output: ',output_str)


"""
4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
    Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
    Output :
    Number of even numbers: 4
    Number of odd numbers: 5
"""
tuple_list = (1, 2, 3, 4, 5, 6, 7, 8, 9)

count_even = 0
count_odd = 0

for i in tuple_list:
    if i%2==0:
        #even
        count_even=count_even+1
    else:
        # odd
        count_odd = count_odd + 1
print("Number of even numbers: ",count_even)
print("Number of odd numbers: ",count_odd)

"""
5. Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
"""

for i in range(0,7):
    if i==3 or i==6:
        continue
    print(i)

"""
6). Write a program to get the Fibonacci series between 0 to 20 using python.
Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
"""
fab1 = 0
fab2 = 1
count = 0

while count < 20:
    print(fab1, end=" ")
    n2 = fab1 + fab2
    fab1 = fab2
    fab2 = n2
    count = count + 1

"""
7). Write a program that iterates the integers from 1 to 30 using python. For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
For numbers that are multiples of both three and five print “FizzBuzz”. 
"""
for i in range(1, 30, 1):
    if i % 3 == 0:
        print(i,' = Fizz')

    elif i % 5 == 0:
        print(i, " = Buzz")

    else:
        print(i," = FizzBuzz")

"""
8.Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.
Input : “SqaTOOlS”
Output : “sqatools”
"""

str_input = input("Enter word to convert into upper/lower case: ")
for c in str_input:
    if c.isupper():
        print(c.lower(),end="")
    else:
        print(c,end="")
print()
print("_"*100)
#print("Output of UpperToLower String: ",str_input)

"""
9. Python loops program that accepts a string and calculates the number of digits and letters using python.
Input : “python1234”
Output :
Letters 6
Digits 4
"""
input_str = "python1234"
count_char = 0
count_digit = 0

for i in input_str:
    if i.isalpha():
        count_char = count_char + 1
    elif i.isnumeric():
        count_digit = count_digit + 1
print("Total Char in String : ", count_char)
print("Total Digit in String : ", count_digit)


"""
10. Python for loop program to print the alphabet pattern ‘O’ using python.
Output:
  ***  
*       *
*       *
*       *
*       *
*       *
   ***  
"""
"""
for i in range(0, 7):
    for j in range(0, 7):
        if ( i == 0 or i ==6 ) and (1 < j and j < 5):
            print("*", end="")
        elif (0 < i <= 5) and (j == 1 or j == 5):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
# logic copied
"""

"""
41. Python loops program to print the pattern T using Python Loops.
"""

for i in range(0,9):
    for j in range(0,9):
        if (i == 0 or i == 1):
            print("*", end="")
        elif (i >= 2) and (j >=3  and j <=6 ):
            print("*", end="")
        else:
            print(" ", end=' ')

    print()





