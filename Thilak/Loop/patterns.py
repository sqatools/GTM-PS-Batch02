# write a python program to print * pattern
"""
*
* *
* * *
* * * *
* * * * *
"""

for i in range(1, 6): #  i =1, 2
    for j in range(i): # j = 0, 1
            #print("value of i", i, "value oh j :",j)          # j = 0, 1, 2
            print(j, end=" ")
    print()

#printing T stucture

for i in range(0, 11):
    for j in range(0, 11):
        if(i==0 and i==1):
            print("*", end=" ")
        elif(j >4 and j <8):
            print("*", end=" ")
        else:
            print(" ", end=' ')
    print()


for i in range(0, 9): # i = 0, 1, 2
    for j in range(0, 9): # j 0-8
        if (i == 0 or i == 1) :
            print("*", end=" ")
        elif (j >2  and j <6 ):
            print("*", end=" ")
        else:
            print(" ", end=' ')

    print()
#Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included).
"""
for i in range(1500, 2701):
    if (i%7 ==0 and i%5 == 0):
        print("i is diisible", i)
    else:
        print("i is not divisible", i)
        
"""
"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
for i in range(1,6):
    print(i*"*")
for i in range(4, -1, -1):
    print(i*"*")