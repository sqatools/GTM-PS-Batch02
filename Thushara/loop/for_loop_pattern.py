"""
# # # # # # # # #
# # # # # # # # #
      # # #
      # # #
      # # #
      # # #
      # # #
      # # #
      # # #

"""

for i in range(0,9):
    for j in range(0,9):
        if i==0 or i==1:
            print("#", end =" ")
        elif ( j>2 and j<6 ) :
            print("#", end = " ")
        else:
            print(" ",end = " ")
    print()
print("*"*50)
"""
A B C D E 
F G H I J 
K L M N O 
P Q R S T 
U V W X Y 
"""
temp=65
for i in range(5):
    for j in range (5):
        print(chr(temp), end=" ")
        temp += 1
    print()
print("&"*50)
"""
 # # #   
#       # 
#       # 
#       # 
#       # 
#       # 
  # # #   

"""

for i in range(1, 8):
    if i > 2 and i < 6:
        print("#", end=" ")
    else:
        print("", end=" ")
print()
for i in range(1, 6):
    for j in range(1, 9):
        if j == 1 or j == 8:
            print("#", end=" ")
        else:
            print("", end=" ")
    print()

for i in range(1, 8):
    if i > 2 and i < 6:
        print("#", end=" ")
    else:
        print("", end=" ")


print()
print("*"*50)
"""
# # # # # # # # #               # 
#               # 
#               # 
#               # 
#               # 
#               # 
#               # 
#               # 
# # # # # # # # # 
"""

for i in range(0, 8):
    print("#", end=" ")
for i in range (0, 8):
    for j in range(0, 9):
        if j==0 or j== 8:
           print("#",end=" ")
        else:
            print(" ",end =" ")
    print()
for i in range(0, 9):
    print("#", end=" ")
