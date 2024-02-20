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