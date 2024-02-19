"""
Nested loop condition
loop inside loop
for loop inside for loop

"""

# Delivery boy delivers to 4 different houses /addressess
# And in each address he delivers 3 packages

for i in range(1,5):                                          # i =1,2,3,4 last value is excluded
    print("Address :", i )
    for j in range(1,4):
       print("Package:" , j )
       # print("Value i :" ,i , "Value j:" ,j)                # i is 1 but j is 1,2,3 when i is 2 j is 1,2,3 .. j is inside i
       for k in range(1,4):
           print("Item :",k)                                  # finishes inner inside to outermost
print("&"*60)

# i 1,2,3,4
# j 1,2,3
# k 1,2,3

# i = 1 ...> j 1  ....> k 1
#                 .....>k 2
#                 .....>k 3


#              2
#              3

##### WAP to print * pattern

"""
*                                                       
* *
* *  *
* *  *  *
* *  *  *  *

"""

# initial starts with 1 * and final ends with 5* so 6, default difference is 1

for i in range(1,6):                                    # One loop helping to move from one line to another line, number of lines
    for j in range(i):                                  # fix as i automatically value of j will be increased as i
        print("Value of i :", i ,"Value of j: ",j)
print("_"*60)

for i in range(1,5):
    for j in range(i):                                  # Only one value means end value so initial value is 0 by default
       print(j,end=" ")
    print()                                             # Under i only then only increasing format can be achieved
print("_" * 60)

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()                                             # not under j , it is under i only, look onto the intendation

"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
"""

temp = 1
for i in range(1,6):
    for j in range(i):
        print(temp,end = " ")                               # will print in the same line
        temp += 1
    print()                                                # will follow the pattern

print(ord("A"))                                            # Ordinance of A is 65

"""
ASCII values 65-90 , 26 alphabets
Capital Alphabets

Small Case ASCII : 97 -122
"""

print(chr(97))                                            # a

"""
A
B C
D E  F
G H  I J
K L  M N O
P Q  R S T U
V W  X Y Z 
"""
temp = 65
for i in range(1,8):
    for j in range(i):
        print(chr(temp),end = " ")
        temp +=1
    print()

"""
A
B C
D E  F
G H  I J
K L  M N O
"""

temp = 65
for i in range(1,6):
    for j in range(i):
        print(chr(temp),end = " ")
        temp += 1
    print()

print(ord("z"))
print("_"*60)

"""
* * * * *
* * * *
* * *
* *
*
"""

for i in range(5,0,-1):                            # i = 5,4,3,2,1  initial 5 , end 0-1 = -1 and difference is -1
    for j in range(i):
        print("*" ,end = " ")
    print()
print("_"*60)

"""
* 
* *
* * * 
* * * *
* * * 
* * 
*
"""

for i in range(1,5):
    for j in range(i):
        print("*", end = " ")
    print()

for i in range(3,0,-1):
    for j in range(i):
        print("*", end = " ")
    print()


########## While loop condition is in separate file check out








