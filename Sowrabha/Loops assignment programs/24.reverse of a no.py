n = int(input("Enter a number: "))
rev = 0

while n>0:
    r = n%10
    rev=(rev*10)+r
    n=n//10
print("reverse of number",rev)
#without using loop
num=input("enter a no")
print(num[::-1])