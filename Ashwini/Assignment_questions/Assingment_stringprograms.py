#1). Write a Python program to get a string made of the first and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string
string = str(input("Enter a string: ")) # ashwini
if len(string)<=2:
    print("string contains less than 2 chars ")
else:
    #output = string[:2] + string[-2] +string[-1]
    output_1= string[:2] + string[-2:]
    print(output_1)
print("-"*50)

#2). Python string program that takes a list of strings and returns the length of the longest string.

list = ["hi", "hello", "good", "morning"]
longest_string = 0
for word in list:
    a = len(word)
    if a > longest_string:
        longest_string = a
print("length of the longest string is : ", longest_string)
print("-"*50)

#3). Python string program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
string_1 = str(input("Enter a string: ")) # ashwini
if len(string)<=2:
    print("string contains less than 2 chars ")
else:
    output_1= string[-2:]*4
    print(output_1)
print("-"*50)

#4). Python string program to reverse a string if it’s length is a multiple of 4
str = "good morning" #["hi", "hello", "good", "morning"]

if len(str) % 4 == 0:
    print(str[::-1])
else:
    print("its not divisible by 4")
print("-"*50)

#5). Python string program to count occurrences of a substring in a string.
str = "hi, good morning. How are you? are you good to start today"

print(str.count("good"))
print("-"*50)

#6). Python string program to test whether a passed letter is a vowel or consonant.
vowel="aeiou"
str="ashwini"
for char in str:
    if char in vowel:
        print("{} its a vowel".format(char))
    else:
        print(f"{char} its constant value")
print("-"*50)

#7). Find the longest and smallest word in the input string.
str = "hello good morning, how are you"
output_1 = str.split(" ")
print("Longest word: ", max(output_1, key = len))
print("Smallest word: ", min(output_1, key = len))
print("-"*50)

#8). Print most simultaneously repeated characters in the input string.
#doubt on this program.


#9). Write a Python program to calculate the length of a string with loop logic.
str= " learning python"
count = 0
for char in str:
    count += 1
print(count)
print(len(str))
print("-"*50)

#10). Write a Python program to replace the second occurrence of any char with the special character $.

str = "good morning"
result = ''
for char in str:
    if char in result:
        result = result + "$"
    else:
        result = result + char
print("Result :", result)
print("-"*50)

#11). Write a python program to get to swap the last character of a given string.

str_2 = "Ashwini"
result = str_2[-1] + str_2[1:-1] + str_2[0]
print(result)
print("-"*50)

#12). Write a python program to exchange the first and last character of each word from the given string.
'''
Input = “Its Online Learning”
Output = “stI enlino gearninL”
'''

Input = "Its Online Learning"
str_3 = Input.split(" ")
output = ""
for word in str_3:
    new_word = word[-1] + word[1: -1] + word[0]
    index = str_3.index(word)
    #print(index)
    str_3[index] = new_word
print(" ".join(str_3))

print("-"*50)

# 13). Write a python to count vowels from each word in the given string show as dictionary output.

#Input = “We are Learning Python Codding”
#output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}

str_4 = "We are Learning Python Codding"
str_5 = str_4.split(" ")
print(str_5)
Vowels="aeiou"
dict={}
count = 0
for word in str_5:
    count = 0
    for char in word:
        if char in Vowels:
            count +=1
        dict[word] = count
print(dict)

print("-"*50)

#14). Write a python to repeat vowels 3 times and consonants 2 times.
#Input = “Sqa Tools Learning”
#Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”

str_6 = "Sqa Tools Learning"
vowels = "aeiou"
for char in str_6:
    if char in vowels:
        result = result + char*3
    else:
        result = result + char*2
print(result)
