# Write a program to find the first and last digits of a number using python.---???
n = str(input("enter the number:"))

for i in range(len(n)):
    if i==0:
        print ("First digit of number:",n[i])
    elif i==len(n)-1:
        print("Last digit of number:", n[i])


# 6). Python program to check given number is a prime number or not.---??


#
# ##Python program to check any person eligible to vote or not
# vote=int(input("enter the age:"))
# if age< 18 :
#     print("Not Eligible for Vote")
# else:
#     print("Eligible for Vote")
