# n=input("enter a no:")
# sum=0
# for i in n:
#     sum=int(n[0])+int(n[-1])
# print(sum)

n=input("enter a no:")
str=str(n)
sum=0
for i in range(len(str)):
    if i==0:
        sum=sum+int(str[i])
    elif i == len(str)-1:
        sum=sum+int(str[i])
print(sum)
"""
num = 2665
str1 = str(num)
total= 0

for i in range(len(str1)):
    if i == 0:
        total += int(str1[i])
    elif i == len(str1)-1:
        total += int(str1[i])

print("Sum of first and last number: ",total)
"""

