#Python string program to reverse a string if it’s length is a multiple of 4.

# str = "Grateful"
# length = len(str)
# print((length))
#
# if length%4 == 0:
#     print(str[::-1])
# else:
#     print("length of string is not a multiple of 4")


#Python string program to count occurrences of a substring in a string.
# string_1= "Helloo Good morning"
# sub_str="oo"
# final_count= string_1.count("oo")
# print(final_count)

#Python string program to test whether a passed letter is a vowel or consonant.--??

# vowel = "AEIOU aeiou"
# letter= str(input("enter the Letter:"))
#
# if letter == vowel :
#     print(letter,"is vowel ")
# else:
#     print(letter,"is consonant")


#Find the longest and smallest word in the input string.
# enter_str=str(input("Enter the string"))

#string= My name is Neha Kumari


"""
10). Write a Python program to replace the second occurrence of any char with the special character $.
Input = “Programming”
Output = “Prog$am$in$”

Solution
11). Write a python program to get to swap the last character of a given string.
Input = “SqaTool”
Output = “IqaTooS”

Solution
12). Write a python program to exchange the first and last character of each word from the given string.
Input = “Its Online Learning”
Output = “stI enlino gearninL”

Solution
13). Write a python to count vowels from each word in the given string show as dictionary output.
Input = “We are Learning Python Codding”
output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}

Solution
14). Write a python to repeat vowels 3 times and consonants 2 times.
Input = “Sqa Tools Learning”
Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”

Solution
15). Write a python program to re-arrange the string.
Input = “Cricket Plays Virat”
Output = “Virat Plays Cricket”

Solution
16). Write a python program to get all the digits from the given string.
Input = “””
Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen
“””
Output = [1112, 5324, 1773, 5324, 555]

Solution
17). Write a python program to replace the words “Java” with “Python” in the given string.
Input = “JAVA is the Best Programming Language in the Market”
Output = “Python is the Best Programming Language in the Market”

Solution
18). Write a Python program to get all the palindrome words from the string.
Input = “Python efe language aakaa hellolleh”
output = [“efe”, “aakaa”, “hellolleh”]

Solution
19). Write a Python program to create a string with a given list of words.
Input = [“There”, “are”, “Many”, “Programming”, “Language”]
Output = There are many programming languages.

Solution
20). Write a Python program to remove duplicate words from the string.
Input = “John jany sabi row john sabi”
output = “John jany sabi row”
"""

# str ="Programming"
# #Output = “Prog$am$in$”
# result = ''
# count = 0
# for char in str:


Input ="SqaTool"
#Output = “IqaTooS”
output_str = (Input[0].replace('S', 'I') + Input[1:6] + Input[-1].replace('l', 'S'))
print("Modified string:",output_str)

#12). Write a python program to exchange the first and last character of each word from the given string.
Input = "Its Online Learning"
#Output = “stI enlino gearninL”

word1=Input[2::-1] #stI
word2=Input[9:3:-1] #enilnO
word3 = Input[:-9:-1] #gninraeL
output_str = word1 +" "+ word2 +" "+ word3
print("Modified string:",output_str)


Input = "We are Learning Python Codding"
#output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}

list1= Input.split(' ')
print(list1) #['We', 'are', 'Learning', 'Python', 'Codding']

vowel="AEIOUaeiou"
dict1=dict()
count=0
for word in list1:
    count = 0
    for char in word:
        if char in vowel:
            count+=1
    dict1[word]= count
print(dict1)


Input ="Sqa Tools Learning"
# #Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”
#
result=''
vowel = "AEIOUaeiou"
Vowels=list(vowel)
print(Vowels) #['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

for char in Input:
    if char in Vowels:
        result= result+ char*3
    else:
        result= result+ char*2
print(result)

#Write a python program to re-arrange the string.
Input ="Cricket Plays Virat"
#Output = “Virat Plays Cricket”


word1=Input.split(" ")
print(word1) #['Cricket', 'Plays', 'Virat']
word2=word1[::-1]
print(word2) #['Virat', 'Plays', 'Cricket']

output_word = ' '.join(word2)
print("final output:",output_word)



Input ="Sinak’s 1112 aim is to 1773 create a new generation of people who understand 444 that an organization’s 5324 success or failure is based on 555 leadership excellence and not managerial acumen"
#Output = [1112, 5324, 1773, 5324, 555]
words=Input.split(" ")
print(words)

list2=[]

for num in words:
    if num.isnumeric() :
        list2.append(num)
print(list2)

#Write a python program to replace the words “Java” with “Python” in the given string.
Input ="JAVA is the Best Programming Language in the Market"
#Output = “Python is the Best Programming Language in the Market”

output= Input.replace('JAVA',"Python")
print(output)

#Write a Python program to get all the palindrome words from the string.
Input ="Python efe language aakaa hellolleh"
#output = [“efe”, “aakaa”, “hellolleh”]

list1=Input.split(" ")
print(list1)
list2=[ ]

for word in list1:
    if word[::-1]== word in list1:
        list2.append(word)
print(list2)

#Write a Python program to create a string with a given list of words.
Input = ['There','are','Many','Programming','Language']
#Output = There are many programming languages.

str = ' '.join(Input)
print("Modified output:",str)

Input = 'John jany sabi row John sabi'
#output = “John jany sabi row”

list1=Input.split()
print(list1) #['John', 'jany', 'sabi', 'row', 'john', 'sabi']
list2=[ ]

for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

output = ' '.join(list2)
print(output)


# str =' '
# count = 0
# for word in Input:
#     if word in Input:
#         count +=1
#         str = str + word
#     print(str)
# elif count
#



