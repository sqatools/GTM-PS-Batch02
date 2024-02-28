"""
NESTED LOOP
"""
for i in range (1, 3):
    print("First Loop :", i)
    for j in range(1, 3):
        print("Second Loop :", j)
        for k in range(1, 4, 1):
            print("Third Loop :",k)

print("*" *50)
"""
Nested Loop Condition
"""

for i in range(1, 5): # i = 1
    print("Address :", i)
    for j in range(1, 4):
        #print("value i :",i, "value j:", j)
        print("Package:", j)
        for k in range(1, 4):
            print(" item :", k)
    print("_"*50)

# write a python program to print * pattern
"""
*
* *
* * * 
* * * *
* * * * * 
"""
for i in range (1, 6):
    for j in range(i):
        print("*", end= " ")
    print()
print("#"*50)
for i in range(1, 6): #  i =1, 2
    for j in range(i): # j = 0, 1
            #print("value of i", i, "value oh j :",j)          # j = 0, 1, 2
            print(j, end=" ")
    print()

"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
"""
temp = 1
for i in range(1, 6):
    for j in range(i):
        print(temp, end=" ")
        temp = temp+1
    print()
print("@"*50)
temp = 1
for i in range(1, 6):
    for j in range(i):
            print(temp, end=" ")
            temp = temp + 1
    print()

print(ord("A"))
# 65
"""
CAPITAL ALPHABATE ASCII
65-90

SMALL CASE ASCII : 97-122
"""
# Get
print(chr(97)) # a


"""
A 
B C 
D E F 
G H I J 
K L M N O 
"""
temp = 65
for i in range(1, 7):
    for j in range(i):
        print(chr(temp), end= " ")
        temp = temp + 1
    print()
print("#"*50)
temp = 65  # ASCII value of A
for i in range(1, 6):
    for j in range(i):
            print(chr(temp), end=" ")
            temp = temp + 1
    print()


print("_"*50)
"""
* * * * *
* * * *
* * *
* *
*
"""
for i in range(7,0,-1):
    for j in range(i):
        print("*", end= " ")
    print()
print("!"*100)
for i in range(5, 0, -1):
    # i = 5, 4, 3, 2, 1
    for j in range(i):
        # j: 0-4, 0-3, 0-2, 0-1, 0
        print("*", end=" ")
    print()



"""
* 
* *
* * * 
* * * *
* * * 
* * 
*
"""

for i in range(1, 7):
    for j in range(i):
            print("*" ,end=" ")
    print()

for i in range(5, 0, -1):
    # i = 5, 4, 3, 2, 1
    for j in range(i):
        # j: 0-4, 0-3, 0-2, 0-1, 0
        print("*", end=" ")
    print()


################ While loop condition #############
# while loop to execute the code
print("_"*50)

temp = 1
while temp <= 10:
    print(temp)
    temp += 1


# write infinite for loop
"""
n = 1
while True:
    n += 1
    print(n)
    if n == 100000:
        break

"""
### Find out the reverse of the any given number without using type casting

num = 153
num1 = num
length = len(str(num))
# 54365
# out = 254
reverse = 0
amst_num = 0

while num > 0: # 4 > 0 | 0 > 0
    temp = num%10 # 2, 5, 4
    reverse = reverse*10 + temp # 2 | 2*10 + 5 = 25 | 25*10+4 = 254
    amst_num = amst_num + temp**length
    num = num//10 # 45, 4, 0

print("Reverse value :", reverse)

if amst_num == num1:
    print("This is armstrong number :", num1)
else:
    print("This is not an armstrong number :", num1)


# 153 = 1 + 125 + 27 = 153
print("@"*50)
### Find out the reverse of the any given number without using type casting
num = 153
num1 = num
rev = 0
while num > 0:
    temp = num % 10
    rev = rev*10 + temp
    num  = num//10
print("Reverse of the given number :",rev)
num =15
num = num**length
print(num)