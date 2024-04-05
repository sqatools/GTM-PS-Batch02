##Python program to check given number is a prime number or not
num = int(input("enter the input number:"))
count = 0

if num > 1:
    for i in range(1, num+1):
        if (num % i) == 0:
            count += 1
    if count == 2:
        print("prime")
    else:
        print("not prime")