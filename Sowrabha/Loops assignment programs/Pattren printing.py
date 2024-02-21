#2). Python Loops program to construct the following pattern, using a nested for loops.


for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(5,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()
