"""13). Python Loops program to print all alphabets from a to z using for loop
        Take chr method help to print characters with ASCII values
        chr(65) = ‘A’
        A-Z ASCII Range  65-90
        a-z ASCII Range  97-122
"""

alpha1 = chr(65)
for i in range(26):
    print(alpha1)
    alpha1 = chr(ord(alpha1) + 1)

alpha2=chr(97)
for i in range(26):
    print(alpha2)
    alpha2=chr(ord(alpha2)+1)