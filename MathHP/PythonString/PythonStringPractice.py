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






