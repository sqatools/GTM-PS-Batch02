a=int(input('given int is :'))
count=0
for i in range(2, a):
    if a%i==0:
        count+=1
    else:
        continue
if count>0:
    print("It is not prime number")
else:
    print("It is a prime number")



