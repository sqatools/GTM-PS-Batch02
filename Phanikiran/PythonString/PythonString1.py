# ####### 16/02/24 ###########
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
print("_" * 50)
print(str2, type(str2))
print("_" * 50)
print(str3, type(str3))
print("_" * 50)
print(str4, type(str4))
print("_" * 50)
print(str5, type(str5))
print("_" * 50)
print(str6, type(str6))
print("_" * 50)

# #################### String formating ######################
print("-" * 300)
# Hello my name is Rahul and my age is 25 and living in Mumbai
name = 'Phanikiran'
age = 34
city = "Bangalore"

# 1. String concatenation
output = "Hello my name is " + name + "and my age is " + str(age) + "and living in" + city
print(output)

# 2. String formatting.
output2 = "Hello my name is {} and my age is {} and living in {}".format(name, city, age)

# 3. f String formatting.
output3 = f"Hello my name is {name} and my age is {age} and living in {city}"
print(output3)

print("-" * 50 + "Searching elements with indexing" + "-" * 50)
#        0  1   2  3  4  5  6  7  8  9  10
# stra= "P  r   o  g  r  a  m  m  i  n  g"
#      -11 -10 -9 -8 -7 -6 -5 -4  -3 -2 -1

# Searching elements with indexing
stra = "Programming"
print(stra[7])
print(stra[-5])

# Loop without indexing
for i in stra:
    print(i, end="")

# Loop with indexing.
print("-" * 50 + "Loop with indexing" + "-" * 50)
strb = "Programming Loop with indexing"
str_len = len(strb)
for i in range(str_len):
    print(strb[i], end="")

print("-" * 50 + "String slicing" + "-" * 50)

# ############### String Slicing #########################
# Case 1:  str1[initial index : last index]
# IN this rule the output will always include the initial and exclude the last index
#         0    1   2    3   4    5    6    7    8   9   10  11  12  13  14 15  16
#         p    y   t    h   o    n    p    r    o   g   r   a   m   m   i  n  g
#        -17  -16 -15  -14 -13  -12  -11  -10  -9  -8  -7  -6  -5  -4  -3 -2 -1
strc = "PythonProgramming"
print(strc[0:6])  # It exclude the ending index element
print("Output 2:", strc[7:18])
print("Output3:", strc[2:4])  # Here it is excluding the 4th index value so output is: th
print("Output 4:", strc[-4:-1])  # Here it is considering values from left to right so output is : min (-1 index is
# excluded)
print("Output 5:", strc[1:-1])  # It prints from 1st index to till last index except -1 so output is:ythonProgrammin
print("Output 6:", strc[-1:-2])  # No output since we cannot move from right to left.

print("-" * 50)
# Case 2: Str1[:Last index]: In case of no last  index value given then default is last index value. .
str1 = "Learning python"
print(str1[:8])
print(str1[:-4])  # Learning py
print(str1[:-3])  # Learning pyt

print("-" * 50)
# Case 3: Str1[Initial index: ] In case of no initial index default is 0.
str2 = "Good morning"
print(str2[2:])  # od morning
print(str2[-6:])  # orning
print(str2[-6:-2])  # orni

print("-" * 50)
# Case 4: Str[initial index:last index: Difference of index]
stra="We are learning python"
print(stra[3:15:1])
print(stra[5:15:2])  # elar
print(stra[-1:-10:-2])  # output:nhyn Here cursor goes from right to left because the difference value has negative "-"
print(stra[1:-5:-2]) # Here its creating ambiguity situation that 1 is positive and difference is in negative.

# Default initial index is zero for positive difference.
# Default initial index is -1 for negative difference.

strb = "Python Programming"

# default initial index is zero
print(strb[:7:1])  # Python

# default initial index is -1
print(strb[:7:-1])  # gnimmargor
print(strb[:7:-2])  # gimro

print(strb[:7:-1])  # gnimmargor

#  ############### Program 1: Print g in first and h in for given string ###############.
print("-" * 20, "gello Good MorninH", "-" * 20)
# Method 1:
str1 = "Hello Good Morning"
print(str1[-1] + str1[1:17] + str1[0])

# Method 2:
val = str1[-1] + str1[1:17] + str1[0]
print(val)

print("-" * 20, "Pto rgamn", "-" * 20)
# ############### Program 2: Print following output for given string#######################################
str2 = "Python Programming"
# output2 = "Pto rgamn"

#  Method 1:
print(str2[0:17:2])

# Method 2:
val2 = str2[0:17:2]
print(val2)

# #################### Program 3 : Print "gninraeL nohtyP" in the output for given string ###############
print("-" * 20, "gninraeL nohtyP", "-" * 20)
str3 = "Learning Python"
# Method 1:
print(str3[-7:-16:-1] + str3[8] + str3[-1:-8:-1])

# Method 2:
val3 = str3[-7:-16:-1] + str3[8] + str3[-1:-8:-1]
print(val3)

# #################### Program 4 : Print "GGood Eveningg" in the output for given string ###############
print("-" * 20, "gninraeL nohtyP", "-" * 20)
str4 = "Good Evening"

# Method 1:
print(str4[0]+str4[0:13]+str4[11])

# Method 2:
print(str4[0]*2+str4[1:11]+str4[11]*2)


###################### String Methods ####################

#print(dir(str))
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

# 2. Lower()
print(str1.lower())

# 3. islower() and isupper()
print("is lower or not: ", str1.islower())

print("is upper or not:", str1.isupper())

# 4.  swapcase() : convert upper case to lower and lower case to upper
print(str1.swapcase())

# 5. Title : this method convert first character of each into capital case.
strb = "India is best country"
print(strb.title())

# 6. istitle() : Check the target string is in title case or not.
print(strb.istitle())

