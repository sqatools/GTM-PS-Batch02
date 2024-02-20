"""
Nested loop condition
"""

for i in range(1, 5):
    print("Address:", i)
    for j in range(1, 4):
        print("Delivery:", j)
        for k in range(1, 4):
            print("item:", k)
            for l in range(1, 5):
                print("Handed overed", l)
    print("*" * 50)

"""
# Program to print pattern


loop 1:
# i=1
# j=0, (Here j loop executed only once)

loop 2:
i=2
j=0,1, (Here j loop executed twice )

loop 3:
i=3
j=0,1,2 (Here j loop executed thrice )

loop4:
i=4
j=0,1,2,3 (Here j loop executed 4 times)

loop 5:
i=5
j=0,1,2,3,4 (Here j loop executed 5 times)
"""
for i in range(1, 6):
    for j in range(i):
        print(j, end="  ")
    print()

print("-" * 50)
# program to print pattern with difference value
for i in range(2, 7, 2):
    for j in range(i):
        print(j, end=" ")
    print()

# Program to print pattern with 1,2,3,4 etc
temp = 1
for i in range(1, 6):
    for j in range(i):
        print(temp, end=" ")
        temp = temp + 1
    print()
