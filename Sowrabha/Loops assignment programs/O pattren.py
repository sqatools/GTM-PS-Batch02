"""

  ***
*       *
*       *
*       *
*       *
*       *
   ***
"""



for i in range(1,8):
    if i>2 and i<6:
        print("*",end="")
    else:
        print(" ",end="")
print()

for i in range(1, 6):
    for j in range(1, 9):
        if j==1 or j==8:
            print("*", end=" ")
        else:
           print("", end=" ")
    print( )


for i in range(1,8):
    if i>2 and i<6:
        print("*",end="")
    else:
        print(" ",end="")
print()





