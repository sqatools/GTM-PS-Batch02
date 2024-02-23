#9). Python loops program that accepts a string and calculates the number of digits and letters using python.
#Input : “python1234”

count=0
letters=0
digits=0

str1=str(input("enter a string"))
for character in str1:
    if character.isalpha():
        letters = letters + 1
    elif character.isdigit():
       digits=digits+1
print("letters is:",letters)
print("digits)
