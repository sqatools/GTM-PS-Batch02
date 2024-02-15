#Python program to check a given number is part of the Fibonacci series from 1 to 10.

#Write a program to get the Fibonacci series between 0 to 20 using python.
# --change the "End value" in range function
#Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
n1=0
n2=1
print(n1)
print(n2)

for i in range (2,20):
    sum = n1+n2
    print(sum)
    n1=n2
    n2=sum

