
#Python program to check given number is divided by 3 or not.
a= int(input("Enter value ="))
r= a%3
if r==0:
    print("Given number is divided by 3")
else:
    print("Given value is not divided by 3")

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


print("_"*40)


# program to determine whether a given number is available in the list of numbers or not.
l1 = [25,16,35,8,40,55,8]
print(l1, type(l1))
search = int(input("Enter number from the list: "))

if search in l1:
    print("Given number is present in the list")
else:
    print("Given number is not present in the list")

print("_"*40)

#program to check any person eligible to vote or not

Age = int(input("Enter your age: "))
if Age >= 18:
    print("Eligible to vote casting")
else:
    print("Not eligible to vote cast")


print("_"*40)

#program to print a square or cube if the given number is divided by 2 or 3 respectively.

n = int(input("Enter the number: "))
if n % 2 == 0:
    square_root = n**2
    print("square root of given value: ", square_root)
elif n % 3 == 0:
    cube_root = n**3
    print("cube root of given value: ", cube_root)

print("_"*40)

#Python program to check whether the given number is negative or not.
n1= int(input("Enter number:"))
if n1<0:
    print("Given number is negative ")
elif n1>0:
    print("Given number is positive")

else:
    print("Given number is zero")