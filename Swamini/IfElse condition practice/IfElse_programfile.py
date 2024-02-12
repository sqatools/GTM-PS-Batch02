#1). Python program to check given number is divided by 3 or not.
"""
a=10
b=5

if a%3==0:
    print("value is divide by 3",a)
elif b%3==0:
    print("value is divide by 3", b)
else :
    print("value is not divide by 3")

# 2. If else program to get all the numbers divided by 3 from 1 to 30.
lower = int(input("Enter lower range limit:"))
upper = int(input("Enter upper range limit:"))
for i in range(lower, upper+1):
    if i%3==0:
        print(i)



#3). If else program to assign grades as per total marks.
Marks= float(input("please enter you mark"))

if Marks > 41 and Marks<=50:
    print("You have C Grade")
elif Marks > 51 and Marks<=60:
    print("You have B Grade")
elif Marks >61 and Marks <=70:
    print("You have A Grade")
elif Marks >71 and Marks <=80 :
    print("You have A+ Grade")
elif Marks >81 and Marks <=90 :
    print("You have A++ Grade")
elif Marks >91 and Marks <=100 :
    print("You have Excellent Grade")
elif 100 < Marks:
    print("Invalid marks")
else:
    print("you are failed")


#4 Python program to check the given number divided by 3 and 5.

a=int(input("pls enter number"))

if a%3==0 and a%5==0:
    print("number is divide by 3 and 5")
else :
    print("number is not divide by 3 and 5")


#5). Python program to print the square of the number if it is divided by 11.
a=int(input("enter number"))
if a**2 and a%11==0:
    print("this is divide by 11 :",a)
else:
    print("number is not divide by 11 :",a)



#6). Python program to check given number is a prime number or not.
a=int(input("enter number"))
if 1%a==0:
    print("number is prime")
else:
    print("number is not prime")

  #2|correct
num=int(input("enter number"))
flag = 0
if num<2:
  flag = 1
else:
  for i in range(2,int((num/2)+1)):
    if num%i==0:
      flag = 1
      break

if flag == 1:
  print('Not Prime')
else:
  print("Prime")


#7). Python program to check given number is odd or even.
a=int(input("enter number"))
if a%2==0 :
    print("number is even",a)
else:
    print("number is odd")

    """

#8)Check a number is part of the Fibonacci series
#taken from internet
num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()

