#Armstrong number
#123 = 1^3 + 2^3 + 3^3
# If sum of power of the length is same as the original number , then its Armstrong number

# Print T as shown

# 0 1  2 3 4 5 6 7 8
# * * * * * * * * *                                     i is rows and j is columns
# * * * * * * * * *
#       * * *
#       * * *
#       * * *
#       * * *
#       * * *
#       * * *
#       * * *

for i in range(0,9):                                    # 9 stars for 1st 2 lines that is i so i is 0 to 9
    for j in range(0,9):
        if (i==0 or  i==1):                            # i = 1st index and 2nd index it should print all
            print("*", end= " ")
        elif (j>2 and j<6):                            # Middle 3 places * printed
            print("*", end = " ")
        else:
            print(" ", end= " ")                       # When j value is 0,1,2,6,7,8 only empty spaces
    print()                                            # Moves to next line


# Print as shown

# A B C D                    65 to 90 ASCII values A - Z Caps
# E F G H
# I J K L                    97 to 122 ASCII a-z small letters
# M N O P                    4*4 matrix

temp = 65
for i in range(4):
    for j in range(4):                               # 4*4 matrix i =4 and j =4
        print(chr(temp), end = " ")
        temp += 1
    print()


# Matrix structure

"""
1 2 3 
4 5 6
7 8 9
"""

print("_"*60)
temp = 1
for i in range(3):
    for j in range(3):
        print(temp,end=" ")
        temp += 1
    print()




