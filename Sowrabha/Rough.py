# # #1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
# #
# #
# # for i in range(1500,2701):
# #     if i%7==0 and i%5==0:
# #         print(i)
# #
# # #2)2). Python Loops program to construct the following pattern, using a nested for loops.
# #
# # """
# # *
# # * *
# # * * *
# # * * * *
# # * * * * *
# # * * * *
# # * * *
# # * *
# # *
# #
# # """
# # #
# # # for i in range(1,6):
# # #     for j in range(i):
# # #         print("*", end= " ")
# # #     print( )
# # # for i in range(5,0,-1):
# # #     for j in range(i):
# # #         print("*", end=" ")
# # #     print( )
# # #3). Python Loops program that will add the word from the user to the empty string using python.
# #
# # n=input("enter a string:")
# # str1=""
# # for i in range(len(n)):
# #     str1 =str1+n[i]
# # print(str1)
# #
# # #4)4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
# #
# # even_count=0
# # odd_count=0
# # for i in range(1,11):
# #     if i%2==0:
# #         even_count=even_count+1
# #     elif i!=0:
# #         odd_count!=0
# #         odd_count=odd_count+1
# # print("even count:",even_count)
# # print("odd count:",odd_count)
#
# # #5)5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
# #
# # for i in range(0,7):
# #     if i!=3 and i!=6:
# #         print(i)
#
# #6). Write a program to get the Fibonacci series between 0 to 20 using python.
# #Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
#
# # num1=0
# # count=0
# # num2=1
# # while(count<20):
# #     print(num1)
# #     n2 = num1+num2
# #     num1=num2
# #     num2=n2
# #     count=count+1
#
# #7). Write a program that iterates the integers from 1 to 30 using python. For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
# #For numbers that are multiples of both three and five print “FizzBuzz”.
#
# for i in range(1,30):
#     if i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0 and i % 5 == 0:
#         print("FizzBUzz")
#     else:
#         print(i)
#
# # #8). Write a program that accepts a word from the user and converts all uppercases in the word to lowercase using python.
# # #Input : “SqaTOOlS”
# # #Output : “sqatools”
# #
# # n=input("enter a word:")
# # for i in n:
# #     n=n.upper()
# # print(n)
# #
# # # #9)9). Python loops program that accepts a string and calculates the number of digits and letters using python.
# # # Input : “python1234”
# # # Output :
# # # Letters 6
# # # Digits 4

# digits=0
# letters=0
# str=input("enter a word:")
# for i in str:
#     if i.isdigit():
#        digits=digits+1
#     if i.isalpha():
#         letters=letters+1
# print("no of digits:",digits)
# print("no of letters:",letters)

#10). Python for loop program to print the alphabet pattern ‘O’ using python.
#Output:
"""
  ***
*       *
*       *
*       *
*       *
*       *
   ***

"""
# for i in range(1,8):
#     if i>2 and i<6:
#         print("*",end="")
#     else:
#         print(" ",end="")
# print()
#
# for i in range(1, 6):
#     for j in range(1, 9):
#         if j==1 or j==8:
#             print("*", end=" ")
#         else:
#            print("", end=" ")
#     print( )
#
#
# for i in range(1,8):
#     if i>2 and i<6:
#         print("*",end="")
#     else:
#         print(" ",end="")
# print()

#11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.
#
# n=0
# while(n<10):
#     n=n+1
#     print(n)
#
# #12)12). Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.
# n=int(input("enter the last no:"))
# count=n
# while count!=0:
#      print(count)
#      count=count-1
# #13). Python Loops program to print all alphabets from a to z using for loop
#         Take chr method help to print characters with ASCII values
#         chr(65) = ‘A’
#         A-Z ASCII Range  65-90
#         a-z ASCII Range  97-122

# alpha=chr(65)
# for i in range(65,91):
#     print(alpha)
#     alpha=chr(ord(alpha)+1)
# alpha1=chr(97)
# for i in range(97,123):
#     print(alpha1)
#     alpha1=chr(ord(alpha1)+1)

#
# #14). Python Loops program to print all even numbers between 1 to 100 in python.
# for i in range(0,101):
#     if i%2==0:
#         print(i)

#15) Python Loops program to print all odd numbers between 1 to 100 using python.
# for i in range(0,100):
#     if i%2!=0:
#         print(i)

#17). Python program to find the sum of all even numbers between 1 to n using python.
#
# even_sum=0
# for i in range(0,11):
#     if i%2==0:
#        even_sum=even_sum+i
# print(even_sum)

#18)18). Python Loops program to find the sum of all odd numbers between 1 to n using python.

odd_sum=0
for i in range(1,10):
    if i%2!=0:
        odd_sum=odd_sum+i
print(odd_sum)

# #19). Write a program to count the number of digits in a number using python.
#
# count=0
# num=input("enter a no: ")
# for i in num:
#     if i.isdigit():
#         count=count+1
# print(count)
#
# #20). Write a program to find the first and last digits of a number using python.
#
# num = int(input("Enter a number: "))
# num_str = str(num)
# first_digit = num_str[0]
# last_digit = num_str[-1]
# print("First digit:", first_digit)
# print("Last digit:", last_digit)
#

#21)Write a program to find the sum of the first and last digits of a number using python.


num = int(input("Enter a number: "))
sum=0
str = str(num)
for i in range(len(str)):
    if i==0:
        sum=sum+int(str[i])
    elif i == len(str) - 1:
        sum = sum + int(str[i])
print(sum)
