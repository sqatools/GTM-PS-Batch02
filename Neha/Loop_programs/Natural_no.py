#Python Loops program to print all natural numbers from 1 to n using a while loop in python.

# int_1 = int(input("enter the number:"))
# count=1
# while count<= int_1:
#     print(count,end=" ")
#     count +=1

#Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.

# int_2= int(input("Enter the number:"))
# count= int_2
#
# while count!=0:
#     print (count,end=" ")
#     count -=1

#Python Loops program to find the sum of all natural numbers between 1 to n using python.

# n = int(input("enter the number:"))
# sum=0
# for i in range(1,n+1):
#         sum = sum+i
# print(sum)

#Python Loops program to print all even numbers between 1 to 100 in python.

# for i in range(1,101):
#    if i%2==0:
#        print(i,end=" ")

# Python program to find the sum of all even numbers between 1 to n using python.
# n = int(input("enter the number:"))
# sum = 0
# for i in range(1,n+1):
#     if i%2==0:
#         sum=sum+i
# print(sum,"Total sum")

#Python Loops program to print all odd numbers between 1 to 100 using python.
#
# for i in range(1,101):
#    if i%2!=0:
#        print(i,end=" ")

# Python Loops program to find the sum of all odd numbers between 1 to n using python.

# n = int(input("enter the number:"))
# sum = 0
# for i in range(1,n+1):
#     if i%2!=0:
#         sum=sum+i
# print(sum,"Total sum")

# Write a program to count the number of digits in a number using python.
# n = str(input("enter the number:"))
# count = 0
#
# for ele in n:
#     count=count+1
# print(count)

# Write a program to find the first and last digits of a number using python.---???
# n = str(input("enter the number:"))
#
# for i in range(len(n)):
#     if i==0:
#         print ("First digit of number:",n[i])
#     elif i==len(n)-1:
#         print("Last digit of number:", n[i])

#Write a program to calculate the sum of digits of a number using python.

# n = int(input("enter the number:"))
# total=0
#
# while n > 0:
#     remainder = n%10
#     total = total+remainder
#     n = n//10
# print(total)

#Write a program to calculate the product of digits of a number using python.

# n = int(input("enter the number:"))
# product_total=1
#
#
# while n>0:
#     remainder_1=n%10
#     product_total = product_total*remainder_1
#     n = n//10
# print(product_total)

#Python loops program to enter a number and print its reverse using python.
# num = int(input("enter the number:"))
# num1 = num
# length = len(str(num))
# reverse = 0
#
#
# while num > 0: # 4 > 0 | 0 > 0
#     temp = num%10 # 2, 5, 4
#     reverse = reverse*10 + temp # 2 | 2*10 + 5 = 25 | 25*10+4 = 254
#     num = num//10 # 45, 4, 0
#
# print("Reverse value :", reverse)

#OR

number = int(input("enter the number:"))
reverse_number = str(number)[::-1]
print(reverse_number)
