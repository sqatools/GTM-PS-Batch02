
#Python program to check given number is divided by 3 or not.
a= int(input("Enter value ="))
r= a%3
if r==0:
    print("Given number is divided by 3")
else:
    print("Given value is not divided by 3")

print("_"*40)


# If else program to get all the numbers divided by 3 from 1 to 30.
for i in range(1,31):
    print(i)
    if i % 3==0:
        print("this number is divisible by 3")
    else:
        print("This number is not divisible by 3")

print("_"*40)


# Python program to check the given number divided by 3 and 5.
var1= int(input("Enter the var1="))

if var1%3==0 and var1%5==0:
    print("number is divisible by 3 & 5")
else:
    print("number is not divisible by 3 & 5")

print("_"*40)

# Python program to print the square of the number if it is divided by 11.
num= int(input("Enter value="))
v= (num**2)
result= v%11
if result==0:
    print("number is divisible by 11", v, result)
else:
    print('number is not divisible by 11')


print("_"*40)


#If else program to assign grades as per total marks.

marks= int(input("Please enter marks:"))

if marks>=40 and marks<50:
    print("grade C")
elif marks>=50 and marks<60:
    print("grade B")
elif marks>=60 and marks<70:
    print("grade A")
elif marks>=70 and marks<80:
    print("grade A+")

elif marks>=80 and marks<90:
    print("grade A++")

elif marks>=90 and marks<=100:
    print("grade Excellent")

elif marks>100:
   print("invalid marks")

else:
     print("fail")


print("_"*40)

#Python program to check authentication with the given username and password.
username= "yogita_k"
password= "yogita@123"
if username=='yogita_k'and password=='yogita@123':
    print("Authentication is successful.")
else:
    print("Authentication failed.")


print("_"*40)

#Python program to check given number is odd or even.
number= int(input("please enter number:"))
n=number%2
if n==0:
    print("even number")
else:
    print("odd number")