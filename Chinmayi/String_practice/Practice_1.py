#write python program get following output
"""
str1= "Hello Good Morning"
output = "gello Good MorninH"

str2 = "Python Programming"
output2 = "Pto rgamn"


str3 = "Learning Python"
output = "gninraeL nohtyP"

str4 = "Good Evening"
output4 = "GGood Eveningg"
"""
"""
str1= ("Hello Good Morning")

print(str1[-1]+str1[1:17]+str1[0]) #output gello Good MorninH

print("*"*70)

str2 = "Python Programming"
print(str2[::2]) #output Pto rgamn

print("*"*70)

str3 = "Learning Python"

str_1 = str3[-8:-16:-1]
str_2 = str3[-1:-7:-1]
print(str_1+" "+str_2) #output gninraeL nohtyP

print("*"*70)

str4 = "Good Evening"
print(str4[0]*2+str4[1:11]+str4[-1]*2) #output GGood Eveningg


#1). Write a Python program to get a string made of the first and the last 2 chars from a
# given string. If the string length is less than 2, return instead of the empty string

stra = input("Enter a String : ")
len1 = len(stra)
if len1 < 2:
    print("True ")
else:
    print(stra[:2]+stra[-2:])
print('*'* 70)

#2). Python string program that takes a list of strings and returns the length
# of the longest string.

input1 = ['Hi','Hello','Programs','Character','Python']
temp = 0

for word in input1:
    a = len(word)
    if a > temp:
        temp = a
print("longest string : ",temp)
print('*'* 70)

#3). Python string program to get a string made of 4 copies of the last two characters of
# a specified string (length must be at least 2).

stra = 'Morning'
print('String : ',stra[-2:]*4)

print('*'* 70)

#4). Python string program to reverse a string if it’s length is a multiple of 4.

Str1=input('Enter a string : ')
if len(Str1)%4 == 0:
    print(Str1[::-1])
print('*'* 70)

#5). Python string program to count occurrences of a substring in a string.

string2 = 'Pythonandprogramandlearning'
sub2 = 'and'

print(string2.count('and'))

print('*'* 70)


#6). Python string program to test whether a passed letter is a vowel or consonant.

string3 = 'learning'

for i in string3:
    if (i=='a' or i=='i' or i=='e' or i=='o' or i=='u'):
            print(f'{i} is a vowel')
    else:
        print(f'{i} is a consonant')


print('*'* 70)

#7). Find the longest and smallest word in the input string.

str3 = 'I am an indian and live in India'

list1 = str3.split(" ")

print("longest word : ",max(list1,key=len))
print("Smallest word : ",min(list1,key=len))

print('*'* 70)

#8). Print most simultaneously repeated characters in the input string.
str1 = 'Hello Goood Morningg'

Repeat1_count = 0
Repeat1_Char = ""

temp = 1
for i in range (len(str1)-1):
    if str1[i]==str1[i+1]:
        temp = temp + 1
        if temp > Repeat1_count:
          Repeat1_count = temp
          Repeat1_Char = str1[i]
    else:
         Repeat1_count = 1

print("Repeat char & count :",Repeat1_count,Repeat1_Char)
print('*'* 70)
#9). Write a Python program to calculate the length of a string with loop logic.

stra = 'I am a python programmer'
count = 0

for n in stra:
    count+=1

print("length of the string with loop: ",count)
print("length of the string without loop :",len(stra))
print('*'* 70)
#10.Write a Python program to replace the second occurrence of any char with the special character $.
#Input = “Programming”
#Output = “Prog$am$in$”

Input1 = "Programming"
result = ' '

for char in Input1:#pr
    if char in result:
        result = result + '$'
    else:
        result = result + char

print("Output = ",result)
print('*'* 70)
#11). Write a python program to get to swap the last character of a given string.
#Input = “SqaTool”

str4 = 'SqaTool'
print(str4[-1]+str4[1:6]+str4[0])

print('*'* 70)

#12). Write a python program to exchange the first and last character of each word from the given string.
#Input = “Its Online Learning”
#Output = “stI enlino gearninL”

str5 = 'Its Online Learning'
str6 =str5.split(" ")
val1 = str6[0]
val2 = str6[1]
val3 = str6[2] 
print(val1[::-1]+" "+val2[::-1]+" "+val3[::-1])

print('*'* 70)

#13). Write a python to count vowels from each word in the given string show as dictionary output.
#Input = “We are Learning Python Codding”
#output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”:2}

str7 ='We are Learning Python Codding'
word_list = str7.split(" ")
vowels = "aeiou"
output = {}
for word in word_list:
    count = 0
    for char in vowels: # ar
        if char in word.lower():
            count += 1
        else:
            continue
    output[word] = count

print("Output :", output)
print('*'* 70)

#14). Write a python to repeat vowels 3 times and consonants 2 times.
#Input = “Sqa Tools Learning”
#Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”

Input1 = "Sqa Tools Learning"
result = ' '

for char in Input1:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        result = result+(char * 3)
    else:
        result = result+(char * 2)

print("Output =",result)
print('*'* 70)

#15. Write a python program to re-arrange the string.
#Input = “Cricket Plays Virat”
#Output = “Virat Plays Cricket”

Input = "Cricket Plays Virat"
Result = Input.split(" ")
Result.reverse()

print(" ".join(Result))
print('*'* 70)
"""
#16. Write a python program to get all the digits from the given string.
#Input = “””
#Sinak’s 1112 aim is to 1773 create a new generation of people who
#understand 444 that an organization’s 5324 success or failure is
#based on 555 leadership excellence and not managerial
#acumen
#“””
#Output = [1112, 5324, 1773, 5324, 555]

Input ="""
Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen
"""
"""
result=Input.split(" ")

print(result.numeric(input))

"""
str1 = "Python"
list1 = [4, 6, 8, 2, 9, 10]
#output = {'PP' : 4, 'yy' : 6, 'tt' : 8, 'hh': 2, 'oo': 9, 'nn' : 10}
output = {}
for i in range (len(str1)):
    output[str1[i]*2] = list1[i]

print("output =",output

# Question
# Write a python program to get below result
# Question1
list1 = [5, 7, 9, 3, 17, 2]
output = {'A' : 5, 'B' : 7, 'C': 9, 'D': 3, 'E' : 17, 'F' : 2}

# Question2
Str1 = "We are Learning Python Programming"
Output = {"wE" : "2We2", "AE" : "3are3", "lG": "8Learning8", "pN" : "6Python6", "pG" : "11Programming11"}




