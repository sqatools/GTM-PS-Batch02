for i in range(1,5):
    for j in range(1,4):
        print("value of i is:",i)
        print("value of j is:",j)
        for k in range(1,5):
            print("vale of k:",k)


#program for * printing
"""
*
* *
* * * 
* * * *
* * * * * 
"""

for i in range(1,6):
    for j in range(i):
        print("*", end = " ")
    print()
#program to print the below pattren
"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
"""
temp=1
for i in range(1,6): #i=1
    for j in range(i):#i=1
        print(temp, end = " ")
        temp=temp+1
    print()

#program to print
print("_"*50)
for i in range(1, 6): #  i =1, 2
    for j in range(i): # j = 0, 1
            #print("value of i", i, "value oh j :",j)          # j = 0, 1, 2
            print(j, end=" ")
    print()

#program
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

#


temp = 1
while temp <= 10:
    print(temp)
    temp += 1

