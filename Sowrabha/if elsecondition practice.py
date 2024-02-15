#Python program to check given number is divided by 3 or not.

a= int(input("enter a value"))

if a%3==0:
    print("yes it is divisable")
else:
    print("Not divisable")

#If else program to get all the numbers divided by 3 from 1 to 30.

num=1
for i in range(1,30,3):
    div=num%3==0
    print(div)
    continue

# If-else program to assign grades as per total marks

marks= int(input("enter a marks"))
if marks<40:
    print("result fail")
else:
    if marks>40 and marks<50:
        print("grade c")
    else:
        if marks>50 and marks<60:
            print("grade B")
        else:
            if marks>60 and marks<70:
                print("grade A")
            else:
                if marks>70 and marks<80:
                    print("grade A+")
                else:
                    if marks>80 and marks<100:
                        print("grade A++")
                    else:
                        if marks>100:
                            print("invalid marks")

#Python program to check the given number divided by 3 and 5.

Number=int(input("enter number"))
if Number%3==0 and Number%5==0:
    print("yes both are divisable")
else:
    print("both are not divisable")

#Python program to print the square of the number if it is divided by 11.

B=int(input("enter a number"))
if(B**2)%11==0:
    print("Yes it can be divided by 11")
else:
    print("It cannot be divided by 11")


#Python program to check given number is a prime number or not.

x=int(input("enter a no:"))
if x%x==0 and x%1==0:
    print("It is a prime no")
else:
    if x%x!=0 and x%1!=0:
        print("It is not a prime no")

#number is odd or even

value=int(input("enter a value:"))
if value%2==0:
    print("Its an even number")
else:
     if value%2==1:
        print("Its an odd number")
