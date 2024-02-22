#20). Write a program to find the first and last digits of a number using python.

n=input("enter a number:")
if n[0].isdigit() and n[-1].isdigit():
    print("first no is:",n[0])
    print("last no is:", n[-1])

