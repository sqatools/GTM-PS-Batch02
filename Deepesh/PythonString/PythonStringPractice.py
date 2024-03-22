"""
Properties of string
-> String is immutable datatype, once it is defined we can not change it.
-> String follows the positive and negative indexing for the data.
-> Any value enclosed with single/double/triple quotes then it is consider as string
"""

str1 = 'H'
str2 = "Hello Good Morning"
str3 = "We are learning 'Python' Programming"
str4 = 'Python is very "easy" to learn'
str5 = '''
Here we will discuss different ways how
we can form a matrix using Python within 
this tutorial we will also discuss the 
various operation that can be performed on a matrix. 
we will also cover the external
'''

str6 = """
Here we will discuss
different ways how we
can form a matrix using 
Python within this tutorial
we will also &^&^*&^ fdjdsfjsdkl {'a': 554} discuss the
various operation
that can be performed 
on a matrix. we will 
also cover the external
"""

print(str1, type(str1))
print("_"*50)
print(str2, type(str2))
print("_"*50)
print(str3, type(str3))
print("_"*50)
print(str4, type(str4))
print("_"*50)
print(str5, type(str5))
print("_"*50)
print(str6, type(str6))
print("_"*50)

############## String Formating ###########
print("_"*50)

# Hello my name is Rahul and my age is 25 and Leaving in Mumbai
name = 'Mohit'
age = 26
city = "Pune"
# 1. String Concatenation
output = "Hello my name is " + name +" and my age is "+str(age)+" and Leaving in "+city
print(output)

# 2. Format method:
output2 = "Hello my name is {} and my age is {} and Leaving in {}".format(name, age, city)
print(output2)

# 3. f String Formating
output3 = f"Hello my name is {name} and my age is {age} and Leaving in {city}"
print(output3)

#       0  1   2  3  4  5  6  7  8  9  10
#stra = "P  r  o  g  r  a  m  m  i  n  g"
#     -11 -10 -9 -8 -7 -6 -5 -4  -3 -2 -1

stra= "Programming"

print(stra[5])  # a
print(stra[-7]) # r


# apply loop on string values
strb = "Python Language"

# loop without indexing
for val in strb:
    print(val, end=" ")

print("_"*50)
# loop with indexing

str_len = len(strb)
for i in range(str_len):
    #print(i, strb[i])
    print(strb[i], end=" ")

print()
print("_"*50)
################ String Slicing ##########
# Rule1:  str1[initial index : last index]
# IN this rule the output will always include the initial and exclude the last index

strc = "Python Programming"

val = strc[0:6]
print("output :", val)  # Python

val2 = strc[7:18]
print("output 2:", val2)  # Programming

print(strc[2:4])  # th

print(strc[-5:-1])  # mmin

print(strc[1:-1]) # ython Programmin

print(strc[-1:3])  # No output, can not move from negative to positive

print(strc[-5:]) # mming


# Rule 2 : str1[: last index]
# in this default initial index will be zero and the last index will be excluded.

str1 = "Learning Python"
print(str1[:8])  # Learning
print(str1[:-3])  # Learning Pyt


# Rule 3: str1 [initial index :]
# In this rule , the default last index will be end of the string.
str2 = "Good Morning"

print(str2[2:])  # od Morning
print(str2[-6:])  # orning

print("+"*50)
# Rule 4 : str[initial index : last index : difference of index]
# In this rule initial index value will be included and last index value will be exluded.

stra = "We are learning Python"

print(stra[3: 15: 1])  # are learning

print(stra[3: 15: 2]) # aelann

print(stra[-1: -10: -1]) # nohtyP gn

print(stra[-1: -10: -2]) # nhy n

print(stra[1:-10:1]) # e are learn

# default initial index as zero in case of positive difference
# default initial index as -1  in case of negative difference
# str[:last index: difference]
strb = "Python Programming"

# default initial index is zero
print(strb[:7:1])  # Python

# default initial index is -1
print(strb[:7:-1])  # gnimmargor
print(strb[:7:-2])  # gimro

print(strb[:7:-1])  # gnimmargor

print("_"*50)
# Rule 5: str[::difference]
# default initial index will be zero with positive difference value
# default initial index will be -1 with negative difference value
# default last index will be end of string positive in case of positive and negative in case of negative difference

strc = "Good Morning"

# initial index zero and last index will end of string
print(strc[::1]) # Good Morning

print(strc[0: len(strc)+1 :1]) # Good Morning

# initial index as -1 and last index will be end of string at negative site
print(strc[::-1])  # gninroM dooG

print(strc[-1:-len(strc)-1:-1])  # gninroM dooG



# Slicing pratice programs

"""
write python program get following output

str1= "Hello Good Morning"
output = "gello Good MorninH"

str2 = "Python Programming"
output2 = "Pto rgamn"


str3 = "Learning Python"
output = "gninraeL nohtyP"

str4 = "Good Evening"
output4 = "GGood Eveningg"
"""

###################### String Methods ####################

print(dir(str))
"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
  'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
'isprintable', 'isspace', 'istitle', 'isupper', 'join', 
'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 
'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex',
'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 
'startswith', 'strip', 'swapcase', 'title', 'translate',
'upper', 
'zfill'
"""

# upper case and lower case method

# 1. upper()
str1 = "Hello We are Learning Python"
print(str1.upper())
# HELLO WE ARE LEARNING PYTHON

# 2. Lower()
print(str1.lower())
# hello we are learning python

# 3. islower() and islower()
str2 = "LearninG"
print("is lower :", str2.islower())  # False
print("is upper :", str2.isupper())  # False
str3 = "python"
print("is lower :", str3, ":", str3.islower()) # True
# is lower : python : True

str4 = "PROGRAMMING"
print("is upper :", str4, ":", str4.isupper()) # True
# is upper : PROGRAMMING : True

print(str3[0].upper()) # P


# 4.  swapcase() : convert upper case to lower and lower case to upper

stra = "India Won 3rd Test"
print(stra.swapcase())
# iNDIA wON 3RD tEST

# 5. Title : this method convert first character of each into capital case.

strb = "India is best country"
print(strb.title())
# India Is Best Country

# 6. istitle() : Check the target string is in title case or not

print("it title :",strb, ":", strb.istitle())
# it title : India is best country : False

strc = "All The Best"
print("strc :", strc, ":", strc.istitle())
# strc : All The Best : True

# 7. split method : This method break the string from given delimenters and return as list
print("_"*50)
str11 = "Today is very sunny day"

output = str11.split(" ")
print(output)
for word in output:
    print(word,":", word[::-1])


str12 = "Python,Programming,Language"
print(list(str12))
# ['P', 'y', 't', 'h', 'o', 'n', ',', 'P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', ',', 'L', 'a', 'n', 'g', 'u', 'a', 'g', 'e']
print(str12.split(","))
# ['Python', 'Programming', 'Language']


url = "https://www.google.co.in"

protocol = url.split(":")[0]
print("protocol :", protocol)

server = url.split(".")[1]
print("server :", server)

www_val = url.split(".")[0].split("//")[1]
print("www :", www_val)


#8. Replace method: replace any substring or character from target string
print("_"*50)
strb = "Hello good morning, Hope you are doing good"

result = strb.replace("good", "bad")
print("result :", result)

result3 = result.replace("Hello", "Hi")
print(result3)

output = strb.replace("good", "bad").replace("Hello", "Hi")
print("output :", output)


print("_"*50)
# program to replace first good with bad and second good with nice
strb = "Hello good morning, Hope you are doing good"

word_list = strb.split(" ")
output = ""
count = 0
for word in word_list:
    if "good" in word and count == 0:
        output = output + "bad" + " "
        count += 1
    elif "good" in word and count == 1:
        output = output + "nice" + " "
    else:
        output = output + word + " "


print("Output :", output)
# Output : Hello bad morning, Hope you are doing nice

# 9. count() method : This method return count of any character/sub-string repeated in given target string.

strc = "Hello good morning, Hope you are doing good"
print("count of good :", strc.count("good")) # 2
print("count of o :", strc.count("o")) # 9


# 10. index() method : this method provide index position of any character/substring
stre = "Good Morning"

print("index of d :", stre.index("d"))  # 3
print("index of d :", stre.index("Mor")) # 5

# if the given char or substring is not found then it gives error.
# print("index of d :", stre.index("D"))
# ValueError: substring not found


# 11. find() method : this method return the index position of the character or substring.

strj = "Python Learning is Fun"
print("check substring Lea :", strj.find("Lea"))  # 7

# if the target character/substring is not available then it return -1
print("check substring Lea :", strj.find("LLea"))  # -1


strj.index("L")


# 12. strip() method : This method remove the trailing space, means space in beginning and end of the string
print("_"*50)
strk = "   India is Best Cricket Team    "
print(strk)
print(strk.strip())

# remove space from left side
print(strk.lstrip())

# remove space from right side
print(strk.rstrip())

# remove all space
print(strk.replace(" ", ""))
# IndiaisBestCricketTeam

# 13. Join() method, we can combine with given delimeters
print("_"*50)
str2 = "Python"
result = "-".join(str2)
print("result :", result)  # P-y-t-h-o-n

# 14. check given has only numbers

str3 = "645654645654"
print(str3.isnumeric()) # True

str4 = "65456 5443543"
print(str4.isnumeric()) # False

# isalnum() method works with three conditions, all numerica, all alphabate and combination alpha and numeric
str5= "hello123"
print(str5.isalnum()) # True
stra = "5434543534"
print("alpha output :", stra.isalnum())

str6 = "Programming"
print(str6.isalpha())  # True

print("_"*50)

# program : find out all the mobile number  and email ids in the given string.

str7 = """
Add 53544 user3@facebook.com extra properties to the calling test.
User properties 8593485908 become part of the test 
report and admin@gmail.com 543453 are available to the 
configured 8883485908 reporters, 25243 like JUnit XML.
The fixture user2@gmail.com is callable with name, 
value. The value is 5593489908 nonadmin@yahoo.com automatically XML-encoded.
"""

word_list = str7.split(" ")
print(word_list)
for word in word_list:
    if word.isnumeric() and len(word) == 10:
        print(word)
    elif "@" in word:
        print(word)
    else:
        continue

print("_"*50)
# Program2 : Write a Python program to find out the longest word in the given string.
print("_"*50)

str_input = "User properties become part of the test reportfdsdfgfdgdsf and are available to the configuredvalues reporters"

longest_word = ''
long_len = 0
word_list = str_input.split()
for word in word_list:  # User,  properties, become
    word_len = len(word) # 4, 10, 5
    #print(word, word_len)
    if word_len > long_len: # 4 > 0 | 10 > 4 | 5 > 10
        long_len = word_len # 4, 10
        longest_word = word # User,  properties
    #print(long_len, longest_word, ":", word)

print("Longest word :", longest_word)



print("_"*50)
#3. Write a Python to get count of vowels from each word.
str1 = "User properties become part of the test"
# output = {"User": 2, "properties": 3, "become" : 2, "part" : 1, "of": 1, "test" : 1}

word_list = str1.split(" ")
vowels = "aeiou"
output = {}  # initiate the dict
for word in word_list: #  User
    count = 0
    for char in vowels: # ae
        if char in word.lower():
            count += 1
        else:
            continue
    output[word] = count


print("Output :", output)


# electricity bill. According to the following conditions:
# # Up to 50 units rs 0.50/unit
# # Up to 100 units rs 0.75/unit
# # Up to 250 units rs 1.25/unit
# # above 250 rs 1.50/unit
# # an additional surcharge of 17% is added to the bill

number_unit = int(input("Please enter total unit comsumption :"))
total_bill = 0
if number_unit <= 50:
    total_bill = total_bill + number_unit*0.50
elif number_unit >50 and number_unit <= 100:
    total_bill = total_bill + number_unit * 0.75
elif number_unit > 100 and number_unit <= 250:
    total_bill = total_bill + number_unit * 1.25
elif number_unit > 250:
    total_bill = total_bill + number_unit * 1.5

total_bill = total_bill + total_bill*0.17
print(" Total bill :", total_bill)



