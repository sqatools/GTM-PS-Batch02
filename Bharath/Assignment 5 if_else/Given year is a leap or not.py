n=int(input("Enter number:"))
if (n%100 != 0 or n%400 == 0) and n%4 == 0:
    print("Leap year")
else:
    print("Not a leap year")