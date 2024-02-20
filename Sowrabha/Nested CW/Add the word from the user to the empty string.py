#3).Python Loops program that will add the word from the user to the empty string using python.

word = input("Enter the word: ")
str1 = ""
for i in range(len(word)):
    str1 += word[i]

print(str1)