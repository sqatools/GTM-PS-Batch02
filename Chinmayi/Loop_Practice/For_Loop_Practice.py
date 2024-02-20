#range(initial value, end value, different value)
#it will print the value till end_value - 1
for i in range(1, 10, 1):
    print(i)
print("*"*70)
# range with two parameter
# range(initial value, end value)
# default difference value is 1 and exclude last value.

for i in range(1, 11):
    print(i)
print("*"*70)

# range with one parameter : range(last value)
# default initial value will 0 and difference value will be 1

for j in range(5):
    print(j)
    print("*" * 5)

print("*"*70)

# write a program to print the table of any given number

num1 = 6
for i in range(1, 11):
    print(num1, "*", i, "=", i*num1)

print("*"*70)

# print values in reverse order

for i in range(10, 0, -1):
    print(i)

print("*"*70)

# check if condition in loop
# get all the even number from 1 to 50

for i in range(1, 50):
    if i%2 == 0:
        print(i)

print("*"*70)

# get factorial of any given number
# factorial of 5 : 5*4*3*2*1 = 120
fact = 1
num = 7

for i in range(num, 0, -1):
    fact = fact*i # 5, 20, 60, 120
    #i=5, 1*5 = 5
    #i=4, 5*4 = 20
    #i=3, 20*3 = 60
    # i=2, 60*2 = 120
    #i=1, 120*1 = 120

print("Factorial output :", fact)


print("*"*70)

### Continue and break condition

for i in range(10):
    if i >= 5 and i <=8:
        continue
    print(i)

# Break statement
print("_"*50)

for i in range(10):
    if i == 6:
        break
    print(i)

