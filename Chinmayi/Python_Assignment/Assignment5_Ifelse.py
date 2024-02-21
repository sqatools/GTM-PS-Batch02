#21.Python program to check whether the given number is positive or negative and even or odd.
Num1 = int(input("Enter a Number : "))

if Num1 > 0:
    if Num1%2==0:
        print("The given is positive and even")
    else:
        print("The given is positive and odd")
else:
    if Num1 % 2==0:
        print("The given is negative and even")
    else:
        print("The given is negative and odd")

print('*'*70)