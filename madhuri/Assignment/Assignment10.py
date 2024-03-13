"""
WAP -Write a Python  Program using slicing concepts in Strings
1)Slicing
2)Slice from the start
3)Slice to the end
4)Negative Indexing
5)Concatenation of Strings
"""

#factorial
fact = 1
num = 3

for i in range(num, 0 , -1):
    fact = fact * i
print("fact: ", fact)



#fabonacci series
num = 10
a,b = 0, 1
print(a,b,end=" " )

for i in range(0,num):
    c = a + b
    a = b
    b = c
    print(c,end=" ")

#prime no or not

num = 120

count = 0
for i in range(2,num):
    if num% i == 0:
        count = count + 1

if count > 0:
    print("is prime")
else:
    print("not prime")

print("_"*50)

str = 'madhuri'
revstr = ''

for i in str:
    #print(i)
    revstr =  i + revstr
    #print("Rev string: ",revstr)
if revstr == str:
    print("String palindrom")
else:
    print("String not palindrom")
print("_"*50)
