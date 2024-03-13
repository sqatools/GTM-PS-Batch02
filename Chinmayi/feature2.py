"""

print("Created second feature")
for i in range(5):
    print(i)
    print("*"*5)

num1 = 6
for i in range(1, 11):
    print(num1, "*", i, "=", i*num1)



fact = 1
num = 8

for i in range(num, 0, -1):
    fact = fact * i
print(fact)



for i in range(10):
    if i >= 5 and i <=8:
        continue
    print(i)

for i in range(10):
    if i == 6:
        break
    print(i)

num1 = 565
rev_num = str(num1)[::-1]
print("rev_num :", rev_num)

if num1 == int(rev_num):
    print("This number is palimdrome")
else:
    print("This number is not a palimdrome")

str1 = "Hello, Good MOrning 567"
vowels = ['a','i','e','o','u','A','E','I','O','U']

result = ""
for char in str1: # Hel
    print(char)
    if char in vowels:
        continue
    else:
        result = result + char # ""+H = H | H + l = Hl

print("result :", result)

tup1 = (5, 7, 'Hello', (4, 7, 9), 7, 9)
addition = 0
for a in tup1:
    if isinstance(a, int):
        print(a)
        addition = addition + a
    else:
        continue

print("addition output :", addition)



for i in range(1, 5): # i = 1
    print("Address :", i)
    for j in range(1, 4):
        #print("value i :",i, "value j:", j)
        print("Package:", j)
        for k in range(1, 4):
            print(" item :", k)



for i in range(1, 6):#12
    for j in range(i):
           print("*", end=" ")
    print()

temp = 1
for i in range(1, 6):
    for j in range(i):
            print(temp, end=" ")
            temp = temp + 1
    print()


temp = 65

for i in range(1,8):
    for j in range(i):
        print(chr(temp),end=" ")
        temp = temp + 1
    print()



* * * * *
* * * *
* * *
* *
*



for i in range(6,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

temp = 1
while temp <= 10:
    print(temp)
    temp += 1

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
    print("This is amstong number :", num1)
else:
    print("This is not an amstong number :", num1)

num1 = 8765
rev = 0

while num1 > 0:
    temp = num1 % 10
    rev = rev * 10 + temp
    num1 = num1//10

print(rev)
"""
strb = "Python Language"

# loop without indexing
for i in strb:
    print(i, end=" ")

str_len = len(strb)
for i in range(str_len):
    #print(i, strb[i])
    print(strb[i], end=" ")