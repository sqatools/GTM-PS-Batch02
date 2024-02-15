#Python program to check given number is a prime number or not.

x=int(input("enter a no:"))
if x==1:
    print("Its not a prime no")
else:
    if x%2==0:
        print("Its not  a prime no")
    else:
           if x%2!=0:
            print("It is a prime no")
