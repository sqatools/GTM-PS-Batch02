##Factorial

num = int(input("enter the input number:"))
factorial = 1

if num < 0:
    print("no factorial")
elif num == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial*i
    print(factorial,"is the factorial for number",num)