#12). Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.
n = int(input("Enter the last number: "))
count = n
while count != 0:
    print(count,end=" ")
    count=count-1