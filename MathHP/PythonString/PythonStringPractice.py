"""
Properties Of String

...> String is immutable datatype, once it is defined we cannot change it
...> String follows the positive and negative indexing for the data
...> Any value enclosed with single/double/triple quotes then it is considered as String
"""

str1 = 'H'
str2 = "Hello Good Morning"
str3 = "We are learning 'Python' Programming"       # Single quotes inside double quotes
str4 = 'Python is very "easy" to learn'             # Double quotes inside single quote
str5 = '''                                          
  
Here we will discuss different ways how             
we can form a matrix using Python within 
this tutorial we will also discuss the 
various operation that can be performed on a matrix. 
we will also cover the external

'''                                                 # Inside single triple quotes

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
"""                                                  # Inside double  triple quotes  , paragraph means

# Special characters , numbers ,alphabets are all allowed inside a String
# For paragraph always its single triple quotes or double triple quotes only

print(str1,type(str1))                              # H <class 'str'> , prints only H no quotes and type is always class
print("&"*60)
print(str2,type(str2))                              # Hello Good Morning <class 'str'>
print("&"*60)
print(str3,type(str3))                              # We are learning 'Python' Programming <class 'str'> , In solution inside double quotes whatever is present
print("&"*60)
print(str4,type(str4))                              # Python is very "easy" to learn <class 'str'>
print("&"*60)
print(str5,type(str5))                              #  <class 'str'>
print("&"*60)
print(str6,type(str6))                              #  <class 'str'>
print("&"*60)

######## String Formatting ####################################
print("&"*60)

# Hello my name is Rahul and my age is 26 and living in Mumbai
name = 'Mala'
age = 76
city = "Mumbai"

### 1)String Concatenation
Output = "Hello my name is " + name + " and my age is " + str(age) + " and living in " + city
print(Output)                                      # age is a number , directly cant add number to a String , so use type  casting

### 2)Format method
Output1 = " Hello my name is {} and my age is {} and living in {}".format(name,age,city)    # .format works in same order respectively
print(Output1)                                     # format method no need for String conversion , only curly braces
                                          # If you use any other () paranthesis or square brackets [] it will print the same symbol rather than taking from formats

### 3) f String Formatting
Output3 = f"Hello my name is {name} and my age is {age} and living in {city}"             # f should be always used in front without space
print(Output3)

# Sequential data type because it follows proper positive and negative indexing
#         0   1    2    3    4    5   6   7   8    9   10
# stra = "P   r    o    g    r    a   m   m   i    n   g"
#       -11 -10   -9   -8   -7   -6  -5  -4  -3   -2   -1

stra = "Programming"
print(stra[5])                                  # a
print(stra[-7])                                 # r  , negative indexing
print("&"*60)

# Apply loop on string values
strb = "Python language"

# Loop without indexing

for val in strb:                               # without indexing means no range required
                                               #print(val)    # Prints each and every character vertically
    print(val, end=" ")                        # prints each and every char in the same line because of end = " "

print("&"*60)

# Loop with indexing

str_len = len(strb)                           # length function len
print(str_len)                                # 15 Total number of characters in the given String, index starts with 0
for i in range(str_len):                      # with indexing means use range
                                              # print(i , strb[i]), prints index and each and every char of the String
    print(strb[i],end = " ")                  # same line

print()
print("&"*60)

########### String slicing ################
###### Substring #########################
# Rule 1: str1[initial index number : last index number]
# In this rule , the output includes the initial index and excludes the last index
# It goes last value -1

strc = "Python Programming"
val = strc[0:6]                             # From 0 to 5 only not 6    Python
print(val)
val1 = strc[7:10]                           # Space also occupies one index
print(val1)                                 # Pro
val2 = strc[7]
print(val2)                                 # P
val3 = strc[7:18]
print(val3)                                 # Programming

print(strc[2:4])                            # th
print(strc[13:17])                          # mmin both positive indexing

#         0   1   2     3     4     5   6    7   8   9   10   11   12   13   14   15   16  17
# strc = "P   y   t     h     o    n         P   r   o   g   r    a    m    m    i    n    g"          length is 15
#        -18  -17  -16 -15   -14   -13  -12 -11  -10 -9  -8 -7  -6    -5   -4   -3   -2   -1

print(strc[-5:-1])                         # mmin both negative indexing
print(strc[-17:-1])                        # ython Programmin  both negative indexing
print(strc[1:-1])                          # ython Programmin , 1 positive 1 negative indexing
print(strc[-1:3])                          # always moves from left to right  , so no output

# can't move from right to left, only left to right

print(strc[-5:])                           # mming , only initial no final index here

# substring from initial index till end


# Rule 2 : str1[ :last index]
# In this default initial index will be zero and as usual last index excluded

str1 = "Learning Python"

#        0    1    2  3 4     5   6    7   8    9   10    11  12   13     14
#str1 = "L    e   a   r   n   i   n    g        P   y    t    h    o      n"
#      -15  -14  -13 -12 -11 -10 -9  -8   -7  -6   -5   -4   -3   -2     -1

print(str1[0:8])                           # Learning
print(str1[:15])                           # Learning Python , default initial value is 0, no need to mention
print(str1[ :-3])                          # Learning Pyt


#### Rule 3 : str1[initial index : ]
# In this rule, the default last index will be the end of the String

str2 = "Good Morning"

#             0   1   2   3    4   5   6   7       8        9     10    11
##### str2 = "G   o   o    d       M   o    r       n        i     n    g"
#            -12 -11  -10  -9  -8  -7  -6  -5      -4       -3    -2   -1

print(str2[5:])                            # Morning
print(str2[2:])                            # od Morning
print(str2[-6:])                           # orning

#### Rule 4: str[initial index : last index : difference of index]  # like range  but with :
# In this rule initial index value will be included and last index value will be excluded

print("&"*60)
stra = "We are learning Python"
print(stra[3:15])             #are learning
print(stra[3:15:2])           # aelann
print(stra[-1:-10:-1])        # nohtyP gn  , right to left so -1
print(stra[-1:-10:-2])        # nhy n

# for 2 values in index then always left to right
# for 3 values then L to R or R to L depends upon positive or negative indexing

print(stra[1:-10:1])          # e are learn , L to R

# default initial index is zero in case of positive difference L to R
# default initial index is -1 in case of negative difference  R to L
# str[ :last index: difference]

strb = "Python Programming"

print(strb[ :6:1])            # Python , default initial index is 0
print(strb[ :6:-1])           # gnimmargorP , default initial index is -1

print(strb[ :6:-2])           # gimroP , default initial index is -1

#### Rule 5: str[::difference]
# default initial index will be 0 with positive difference
# default initial index will be -1 with negative difference
# default last  index will be end of the string positive in case of positive difference
# default last  index will be end of the string negative in case of negative difference

strc = "Good Morning"

print(strc[::1])                   #Good Morning , initial default is 0 , last index is default end of the string

print(strc[::-1])                  # gninroM dooG , R to L , default initial is -1, last index will be end of string from R to L

# Some slicing practice programs

""" HW
1) WAP to get output

str1 = "Hello Good Morning"
output = gello Good MorninH

str2 = "Python Programming"
output = Pto rgamn

str3 = "Learning Python"
output = gninraeL nohtyP

str4 = "Good Evening"
output = "GGood Eveningg"

"""
str1 = "Hello Good Morning"
print(str1[-1]+str1[1:16]+str1[0])

str2 = "Python Programming"
print(str2[0:18:2])

str3 = "Learning Python"
print(str3[-8:-16:-1]+"  "+str3[-1:-7:-1])

str4 = "Good Evening"
print(str4[0]+str4[0:12]+str4[11])

################### String Methods

print(dir(str))         # solution in the console
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
# '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index',
# 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join',
# 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
# 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# Upper case and Lower case method

#1) upper case - Conversion

str1 = "Python Programming"
print(str1.upper())                               # PYTHON PROGRAMMING , All Upper

#2)Lower case

str1 = "Python Programming"
print(str1.lower())                              # python programming


#3)islower() - Checking
str2 = "LearninG"
print(str2.islower())                            # False , all cases are not lower

#4)isupper()
print(str2.isupper())                           # False , all cases are not upper

str5 = "python"
print(str5[0].upper())                          # P

#5) swapcase : Convert upper to lower and lower to upper

stra = "India Won 3rd Test"
print(stra.swapcase())

#6)Title : This method converts first character of each  word into capital case , Pascal case

strb = "India is best country"
print(strb.title())

#7) istitle() : Check the target string is in title case or not

print(strb.istitle())              # India is best country , so false

strc = "All The Best"
print(strc.istitle())

#8)split method: This method breaks the string from delimenters and return as list

str11 = "Today is very sunny day"
output = str11.split(" ")          #['Today', 'is', 'very', 'sunny', 'day'] converts to list of words
print(output)
for word in output:
    print(word,":",word[::-1])     # Each word in reverse order

str12 = "Python,Programming,Language"
print(str12.split("g"))            # ['Python,Pro', 'rammin', ',Lan', 'ua', 'e']

url = "https://www.google.co.in"   # http -protocol , co.in - domain

protocol = url.split(":")
print("protocol:",protocol)         # ['https', '//www.google.co.in']      , splits into list of words

server = url.split(".")
print("server:",server)             #['https://www', 'google', 'co', 'in']

server = url.split(".")[1]
print("server:",server)             #google

www_val= url.split(".")[0].split("//")[1]
print("www:",www_val)                   #www

#9) Replace method:Replace any substring or character from target string

strb = "Hello good Morning, Hope you are doing good"

result = strb.replace("good","bad")
print("result:",result)

result1 = strb.replace("Hello","Hi")
print("result:",result1)

result2 = strb.replace("good","bad").replace("Hello","Hi")
print("result:",result2)

#Program to replace first good with bad and second good with nice
strb = "Hello good Morning, Hope you are doing good"

print("_"*60)
word_list = strb.split(" ")
output = " "
count =0
for word in word_list:
    if "good" in word and count==0:
        output = output+"bad"+" "
        count += 1
    elif "good" in word and count ==1:
        output=output+"nice"+" "                                    #########
    else:
        output= output+word+" "
print("Output:",output)

## 9) Count method: This method return count of any character/sub-string repeated in given target string

str12="Good Morning Girl"
print("Count of o:",str12.count("o"))                       # 3
print("Count of Good:",str12.count("Good"))                 # 1

## 10) index method: This method provide index position of any character or substring

stre="Good Morning"
print("index of d:",stre.index("d"))                        # 3
print("index of Mor:",stre.index("Mor"))                      # 5

# print("index of d:",stre.index("D"))                        # ValueError: substring not found, D not available

## 11)find() method- this method return the index position of the character or substring

strj = "Python Learning is Fun"
print("Check substring Lea:",strj.find("Lea"))                # 7

#if the target character/substring is not available then it return -1
print("Check substring LLea:",strj.find("LLea"))              # -1

## For index if its not available then it will throw the error and stops the program
## For find() if its not available then it will not  throw the error , returns value -1 , for smooth running of the program


#12) strip() method : This method remove the leading and trailing spaces, beginning and end
print("_"*60)
strk = "    India is the best in Cricket    "
print(strk)
print(strk.strip())

# Remove space from left side
print(strk.lstrip())

# Remove space from right side
print(strk.rstrip())

# Remove all  spaces
print(strk.replace(" ",""))                    # IndiaisthebestinCricket, in between spaces

#13) Join() method , we can combine with given delimiters, Any string with any delimiters like , _ . ;

print("_"*60)
str2 = "Python"
result ="_".join(str2)
print("result:",result)                                    # result: P_y_t_h_o_n

# 14) Check given string has only numbers

str3 = "64565465455456"
print("is numeric method of string:", str3.isnumeric())   #True      # Only numbers not even space should be present orelse False

str4 = "8656759 69876"
print("is numeric check with space:",str4.isnumeric())    # False

str5a = "6721AB%78689"
print("Check with alpha and num and special char mixed:",str5.isnumeric())  # False

# isalnum() method works with three conditions, all numerics, all alphabets and combination of alphabets and numerics

str5 = "hello123"
print("is alphanumeric :",str5.isalnum())                 #True

str5b = "5978587987"
print("is alphanumeric:",str5b.isalnum())                 # True , only numbers

str5c ="fkjgfvjhv"                                        # True ,only alphabets
print("isalphanumeric:",str5c.isalnum())

str5d = "fkuhg 85795"
print("isalphanum with space:",str5d.isalnum())          # False

str5e = "65865jklghkjlhg@"
print("isalphanum with @",str5e.isalnum())              # False

print("_"*60)

# Program to find out all the mobile numbers and email ids in the given string

str7 = """
Add 53544 user3@facebook.com extra properties to the calling test.
User properties 8593485908 become part of the test 
report and admin@gmail.com 543453 are available to the 
configured 8883485908 reporters, 25243 like JUnit XML.
The fixture user2@gmail.com is callable with name, 
value. The value is 5593489908 nonadmin@yahoo.com automatically XML-encoded.
"""

# Only 10 digits are mobile numbers

word_list = str7.split(" ")                   # space so will get word list, each word is separated
print(word_list)
for word in word_list:
    if word.isnumeric() and len(word)== 10:   # only numbers and length is 10
        print(word)
    elif "@" in word:
        print(word)
    else:
        continue

# Program2: WAP to find out the longest word in the given string

print("_"*60)
str_input = " User properties become part of the test reportfuygfuhgvdsxdfgxfxdgh and are available to the configuredvalues reporters"

longest_word = ''
long_len = 0                                  # initially
word_list = str_input.split(" ")             # split all words,by default split is by space (" ")
for word in word_list:
    word_len = len(word)
    if word_len>long_len:                  #print(word,word_len)
      long_len=word_len                   # Now setting long_len as 4 ,User which is word len
      longest_word = word

print("Longest word:",longest_word)

#3) WAP to get count of vowels from each word

str1= " User properties become part of the test"
#output = {"User":2,"properties":3,"become":2,"part":1,"of":1,"test":1}

word_list = str1.split(" ")
vowels = "aeiou"
output ={}              # initiate dict
for word in word_list:
    count = 0
    for char in vowels:    # ae  char in word means properties 4 vowels
        if char in word.lower():     # char.lower() in vowels
            count +=1
        else:
            continue
    output[word] = count

print("Output:",output)

# electricity bill. According to the following conditions:
# # Up to 50 units rs 0.50/unit
# # Up to 100 units rs 0.75/unit
# # Up to 250 units rs 1.25/unit
# # above 250 rs 1.50/unit
# # an additional surcharge of 17% is added to the bill

number_unit = int(input("Please enter total unit consumption"))
total_bill=0
if number_unit<=50:
    total_bill=total_bill+(number_unit*0.50)
elif number_unit>50 and number_unit<=100:
    total_bill=total_bill+(number_unit*0.75)
elif number_unit>100 and number_unit<=250:
    total_bill=total_bill+(number_unit*1.25)
elif number_unit>250:
    total_bill=total_bill+(number_unit*1.5)
total_bill=total_bill+total_bill*0.17
print("Total bill:",total_bill)                                      # 614.25










