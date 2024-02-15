"""
    1. 1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
        Input1:1500
        Input2:2700
"""
for i in range(1500,2700):
    if ( i%7 == 0 ) and (i%5==0):
        print("i :",i)
        #print(i, end=" ")

print("_"*100)
"""
2.
"""

"""
    3). Python Loops program that will add the word from the user to the empty string using python.
    Input: “python”
    Output : “python”
"""
user = "python"

output_str = ''
print(len(user))
for i in range(len(user)):
    output_str=output_str+user[i]
    print('user: ',user[i])
print('output: ',output_str)


"""
4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
    Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
    Output :
    Number of even numbers: 4
    Number of odd numbers: 5
"""
tuple_list = (1, 2, 3, 4, 5, 6, 7, 8, 9)

count_even = 0
count_odd = 0

for i in tuple_list:
    if i%2==0:
        #even
        count_even=count_even+1
    else:
        # odd
        count_odd = count_odd + 1
print("Number of even numbers: ",count_even)
print("Number of odd numbers: ",count_odd)

"""
5. Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
"""

for i in range(0,7):
    if i==3 or i==6:
        continue
    print(i)

"""
6.
"""
