num=input("enter a number")
dict1={}


for val in num:
    if val in dict1:
        dict1[val]=dict1[val]+1
    else:
        dict1[val]=1
print(dict1)