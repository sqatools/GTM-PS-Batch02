list1=[45,60,61,90,70,77,80,20]
list1.sort()
l1=len(list1)
print(list1)
print(l1)
middle=int(l1/2)
if l1%2==0:
    medain = (list1[middle]+list1[middle-1])/2
    print("median is :", medain)
else:
    medain=list1[middle]
    print("median is :", medain)
