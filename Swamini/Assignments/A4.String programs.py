#10,28
"""print("Hi this is feature branch ")

write python program get following output

str1= "Hello Good Morning"
output = "gello Good MorninH"

str2 = "Python Programming"
output2 = "Pto rgamn"

print(str2[:7:1])

str3 = "Learning Python"
output = "gninraeL nohtyP"

str4 = "Good Evening"
output4 = "GGood Eveningg"
"""

"""
#assignemnets1#

str1= "Hello Good Morning"
output = "gello Good MorninH"
c=str1[0]
d=str1[-1]

str1=f"{d}ello Good Mornin{c}"
print(str1)

print("*"*50)
#assignemnets2#
str2 = "Python Programming"
output2 = "Pto rgamn"

print(str2[:17:2])

print("*"*50)

#assignemnets4#
str4 = "Good Evening"
output4 = "GGood Eveningg"
a=str4[0]
b=str4[-1]
str4="{}Good Evening{}".format(a,b)
print(str4)

print("*"*50)

#assignemnets3#

str3 = "Learning Python"
output = "gninraeL nohtyP"

print(str3[-8::-1],""+str3[-1:-7:-1])
print("*"*50)
"""
#-website questions-----------------------------
"""
1). Write a Python program to get a string made of the first and the last 2 chars from a given string. 
If the string length is less than 2, return instead of the empty string

stra=input("Enter string: ")
if len(stra)<2:
    print("string empty")
else:
    print(stra[:2] + stra[-2:])
"""

"""2). Python string program that takes a list of strings and returns the length of the longest string.

str_input = "User properties become part of the test reportfdsdfgfdgdsf and are available to the configuredvalues reporters"
longest_word=""
count=0
list=str_input.split()
for word in list:
    length=len(word)
    if length > count:
        count= length
        longest_word=word

print("longest word :",longest_word)
"""
"""
3). Python string program to get a string made of 4 copies of the last two characters of a 
specified string (length must be at least 2).
stra=input("enter string ")
len=len(stra)
a=stra[-2:]

if len<=2:
    print("string length should be 2")
else:
    print("string: ", a*4)"""

"""4). Python string program to reverse a string if it’s length is a multiple of 4.
stra=input("enter string ")
len=len(stra)
a=stra[::-1]
if len%4==0:
    print("string is: ",a)
else:
    print("pls enter string which is multiple by 4")
"""

"""
5). Python string program to count occurrences of a substring in a string.
stra="swaminiswswsw"
count="sw"
print(stra.count("sw"))
"""
"""
6). Python string program to test whether a passed letter is a vowel or consonant.
ch=input("enter charachter")
if ch=="a" or ch=="A" or  ch=="e" or  ch=="E" or ch=="i" or  ch=="I" or ch=="o" or  ch=="O" or ch=="u" or  ch=="U":
    print("this is vowels")
else:
    print("letter are consonant")
#--------2nd solution
ch=input("enter charachter")
char=("a,e,i,o,u,A,E,I,O,U")
for i in ch:
    print(i)
    if i in char:
        print("this is vowels")
    else:
        print("this is consolant")
"""
"""7). Find the longest and smallest word in the input string
string = "we are learning python"
list1 = string.split(" ")

print(list1)
print("longest word : ",max(list1,key=len))
print("smallest word: ",min(list1,key=len))"""

"""8)Print most simultaneously repeated characters in the input string.
stra="sswaamini is my nameeeee"
rep_char=""
rep_count=0
count=1
for i in range(len(stra)-1):
    if stra[i]==stra[i+1]:
        count+=1
        if count > rep_count:
            rep_count=count
            rep_char=stra[i]

    else:
        count=1
print("repeted char",rep_char)
print("repeted count",rep_count)
"""



"""9). Write a Python program to calculate the length of a string with loop logic
stra=input("enter string")
len=len(stra)
count=0
for i in stra:
    count+=1
print("length of string: ",len)
print("length of string using logic loop: ",count)
"""

"""10). Write a Python program to replace the second occurrence of any char with the special character $.
Input = “Programming”
Output = “Prog$am$in$”

sstr1 = "Programming"
result = ''

#checking for repeated char
for char in str1:
    if char in result:
        result = result + "$"
    else:
        result = result + char

#Printing output
print("Result :", result) # how it works
"""


"""11). Write a python program to get to swap the last character of a given string.
Input = “SqaTool”
Output = “lqaTooS”
stra="SqaTool"
print(stra[-1]+stra[1:-1]+stra[0])\
"""

"""12). Write a python program to exchange the first and last character of each word from the given string.
Input = “Its Online Learning”
Output = “stI enlino gearninL”
stra="Its Online Learning"
print(stra[2]+stra[1]+stra[0],stra[9]+stra[5:9]+stra[4],stra[-1]+stra[-7:-1]+stra[-8])
"""

"""13). Write a python to count vowels from each word in the given string show as dictionary output.
Input = “We are Learning Python Codding”
output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}
str1 = "We Are Learning Python Codding"
word_list=str1.split()
output={}
vowels=("aeiouAEIOU")
for word in word_list:
    count=0
    for char in vowels:
        if char in word:
            count+=1
    output[word]=count
print("output:",output)
"""

"""14). Write a python to repeat vowels 3 times and consonants 2 times.
Input = “Sqa Tools Learning”
Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”
stra="Sqa Tools Learning"
vowels="aeiouAEIOU"
output=""
for i in stra:
    if i in vowels:
        output=output+i*3
    else:
        output=output+i*2
print("output :-",output)
"""

"""15). Write a python program to re-arrange the string.
Input = “Cricket Plays Virat”
Output = “Virat Plays Cricket”
stra="Cricket Plays Virat"
print(stra[14:19],stra[8:13],stra[:7])

"""

"""16). Write a python program to get all the digits from the given string.
Input = “””
Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen
“””
Output = [1112, 5324, 1773, 5324, 555]

""""""stra=Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen""""""
output=[]
list=stra.split(" ")
for i in list:
    if i.isnumeric():
        output.append(i)
    else:
        print(i,end=" ")
print(output)
"""

"""17). Write a python program to replace the words “Java” with “Python” in the given string.
Input = “JAVA is the Best Programming Language in the Market”
Output = “Python is the Best Programming Language in the Market”

stra= "JAVA is the Best Programming Language in the Market"
#print(stra.replace("JAVA","PYTHON")) -easy way
list=stra.split(" ") #2nd way
for i in list:
    if i=="JAVA":
        index=list.index(i)
        list[index]="PYTHON"
print(" ".join(list))
"""

"""18). Write a Python program to get all the palindrome words from the string.
Input = “Python efe language aakaa hellolleh”
output = [“efe”, “aakaa”, “hellolleh”]

stra="Python efe language aakaa hellolleh" #palindrome means reverse word same 
output=[]
list=stra.split(" ")

for i in list:
    if i ==i[::-1]:
        output.append(i)
        print(i)
print(output)
"""
"""19). Write a Python program to create a string with a given list of words.
Input = [“There”, “are”, “Many”, “Programming”, “Language”]
Output = There are many programming languages.
list1 = ["There", "are", "Many", "Programming", "Language"]
print(" ".join(list1))"""

"""20). Write a Python program to remove duplicate words from the string.
Input = “John jany sabi row john sabi”
output = “John jany sabi row”
stra="John jany sabi row john sabi"
output=[]

list=stra.split(" ")
for i in list:
    if i not in output:
        output.append(i)

print(" ".join(output))
"""
"""21). Write a Python to remove unwanted characters from the given string.
Input = “Prog^ra*m#ming”
Output = “Programming”
stra="Prog^ra*m#ming"
for i in stra:
    if i.isalnum():
        print(i,end="")
"""
"""22). Write a Python program to find the longest capital letter word from the string.
Input = “Learning PYTHON programming is FUN”
Output = “PYTHON”
stra="Learning PYTHON programming is FUN"
output=""
list=stra.split()
count = 0
for i in list:
    if i.isupper():
        if len(i)>count:
            count=len(i)
            output=i
print(count,output)
"""
"""23). Write a Python program to get common words from strings.
Input String1 = “Very Good Morning, How are You”
Input String1 = “You are a Good student, keep it up”
Output = “You Good are”

stra="Very Good Morning, How are You"
strb="You are a Good student, keep it up"
strc=[]
list1=stra.split(" ")
list2=strb.split(" ")
for i in list1:
    if i in list2:
        strc.append(i)
print(" ".join(strc))
"""
"""24). Write a Python program to find the smallest and largest word in a given string.
Input = “Learning is a part of life and we strive”
Output = “a”, “Learning”
stra="Learning is a part of life and we strive"
output=[]
output1=[]
list1=stra.split()
count=0
for i in list1:
    if len(i)>count:
       
        count=len(i)
        output=i
for i in list1:
    if len(i) < count:
        count = len(i)
        output1 = i
print(output,output1)
"""
"""25). Check whether the given string is a palindrome (similar) or not.
Input= sqatoolssqatools
Output= Given string is not a palindrome
stra="awawawawa"
stra1=stra[::-1]
if stra==stra1:
    print("given string palindrome")
else:
    print("given string is not palindrome")
"""
"""26). Write a program using python to reverse the words in a string.
Input= sqatools python
Output= slootaqs

stra="sqatools python"
stra1=stra[0:8]
print(stra1[::-1])
"""

"""27). Write a program to calculate the length of a string.
Input= “python”
Output = 6
stra="python"
print(len(stra))
"""

"""28). Write a program to calculate the frequency of each character in a string.
Input = “sqatools”
Output = {‘s’:2, ‘q’:1, ‘a’: 1, ‘t’:1,‘o’:2, ‘l’:1, ‘s’:1}
stra="sqatools"
list1=stra.split()

output={}
for i in list1:
    count=0
    for char in i:
        if char in list1:
            count+= 1


        output[char]=count
print(output)
"""
"""29). Write a program to combine two strings into one.
Input: 
A = ’abc’
B = ’def’
Output = abcdef
a="abc"
b="def"
c=a+b
print(c)
"""

"""30). Write a program to print characters at even places in a string.
Input = ‘sqatools’
Output = saol
stra="sqatools"

for i in range(len(stra)-1):
    if i%2==0:
        print (stra[i],end="")
"""

"""31). Write a program to check if a string has a number or not.
Input = ‘python1’
Output = ‘Given string have a number’
stra="python1"
count=0
for i in stra:
    if i.isnumeric():
        count+=1
if count>0:
    print("given number have a numeric value")
else:
    print("given number have a numeric value")
"""

"""32). Write a python program to count the number of vowels in a string.
Input= ‘I am learning python’
Output= 6
stra="I am learning python"
vowels="aeiouAEIOU"
count=0

for i in stra:

    if i in vowels:
        count+=1
print(count)
"""
""""33). Write a python program to count the number of consonants in a string.
Input= ‘sqltools’
Output= 6
stra="sqltools"
vowels="aeiouAEIOU"
count=0
for i in stra:
    if i not in vowels:
        count+=1
print(count)
"""
"""34). Write a program to print characters at odd places in a string.
Input = ‘abcdefg’
Output = ‘bdf’
stra="abcdefg"
print(stra[1::2])
"""

"""35). Write a program to remove all duplicate characters from a given string in python.
Input = ‘sqatools’
Output = ‘sqatol’

stra="sqatools"
list=list(stra)

output=[]
for i in list:
    if i not in output:
       output.append(i)

print("".join(output))


"""
"""
36). Write a program to check if a string has a special character or not
Input = ‘python$$#sqatools’
Output =  ‘Given string has special characters
stra="python$$#sqatools"
if stra.isalnum():
    print("Given string has not special characters")
else:
    print("Given string has  special characters")
"""
"""37). Write a program to exchange the first and last letters of the string
Input = We are learning python
Output = ne are learning pythoW
stra="We are learning python"
print(stra[-1]+stra[1:-1]+stra[0])
"""

"""38). Write a program to convert all the characters in a string to Upper Case.
Input = ‘I live in pune’
Output = ‘I LIVE IN PUNE’
stra="I live in pune"
print(stra.upper())
"""

"""39). Write a program to remove a new line from a string using python.
Input = ‘objectorientedprogramming\n’
Output = ‘Objectorientedprogramming’
stra="objectorientedprogramming "
print(stra.rstrip())
"""
"""40). Write a python program to split and join a string
Input =‘Hello world’
Output = [‘Hello’, ‘world’]
                 Hello-world
stra="Hello world"

list=stra.split()
print("-".join(list))
print(list)
"""
"""41). Write a program to print floating numbers up to 3 decimal places and convert it to string.
Input = 2.14652
Output= 2.146
stra=2.14652
print(round(stra,3))
"""

"""42). Write a program to convert numeric words to numbers.
Input = ‘five four three two one’
Output = 54321"""
stra="five four three two one"









































































