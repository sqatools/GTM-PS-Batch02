#153 = 1*1*1 + 5*5*5 + 3*3*3

n=int(input("value of n:"))
amstrong=n
sum=0
while n>0:
    rem=n%10
    sum=sum+(rem**3)
    n=n//10
if sum==amstrong:
    print ("Amstrong number")
else:
    print("Not Amstrong number")
