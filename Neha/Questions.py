# Write a program to find the first and last digits of a number using python.---???
n = str(input("enter the number:"))

for i in range(len(n)):
    if i==0:
        print ("First digit of number:",n[i])
    elif i==len(n)-1:
        print("Last digit of number:", n[i])


