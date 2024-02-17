#123 = 1^3 + 2^3 + 3^3 == 123
#
"""
for i in range(0, 9):
    for j in range(0, 9):
        if (i == 0 or i == 1) :
            print("*", end="")
        elif (i >= 2) and (j >=3  and j <=6 ):
            print("*", end="")
        else:
            print(" ", end=' ')

    print()
"""
########################
"""
* * * * * * * * *
* * * * * * * * *
      * * *
      * * *
      * * *
      * * *
      * * *
      * * *
      * * *  
"""
for i in range(0, 9): # i = 0, 1, 2
    for j in range(0, 9): # j 0-8
        if (i == 0 or i == 1) :
            print("*", end=" ")
        elif (j >2  and j <6 ):
            print("*", end=" ")
        else:
            print(" ", end=' ')

    print()


"""
1 2 3 
4 5 6
7 8 9
"""
print("_"*50)
temp = 65
for i in range(4):
    for j in range(4):
        print(chr(temp), end=' ')
        temp += 1
    print()