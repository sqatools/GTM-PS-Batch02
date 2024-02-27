# # Write a program to find the first and last digits of a number using python.---???
# n = str(input("enter the number:"))
#
# for i in range(len(n)):
#     if i==0:
#         print ("First digit of number:",n[i])
#     elif i == len(n)-1:
#         print("Last digit of number:", n[i])

#
# # Python string program to test whether a passed letter is a vowel or consonant.--??
#
# vowel = "AEIOU aeiou"
# letter = input("enter the Letter:")
#
# if letter in vowel:
#     print(letter, "is vowel ")
# else:
#     print(letter, "is consonant")



# Usage
str1 = "listen"
str2 = "sileno"
if sorted(str1) == sorted(str2):
    print("The two strings are anagrams of each other")
else:
    print("The two strings are not anagrams")

#Questions need to ask
10). Write a Python program to replace the second occurrence of any char with the special character $.
Input = “Programming”
Output = “Prog$am$in$”

21. Write a Python to remove unwanted characters from the given string.
Input = “Prog^ra*m#ming”
Output = “Programming”

# output = ''.join(i for i in Input_21 if i.isalnum())
# print(output)

##Write a Python program to find the longest capital letter word from the string.
Input = "Learning PYTHON programming is FUN"
#Output = “PYTHON”