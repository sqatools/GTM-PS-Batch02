# 19). Write a program to count the number of digits in a number using python.
count=0
n=(input("enter a number:"))
for i in n:
    if n.isdigit():
        count=count+1
print(count)

