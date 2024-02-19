"""
1. Write a Python program to get a string made of the first and the last 2 chars from a given string.
 If the string length is less than 2, return instead of the empty string
"""
input_string = 'M'
if len(input_string) < 2:
    print(True)
else:
    start_str = input_string[:2]
    end_str = input_string[-2:]
    combined_str = start_str + end_str
    print("first and last two char of string is : ",combined_str)
print("_"*100)

"""
2. Python string program that takes a list of strings and returns the length of the longest string.
"""

list_str = ['python', 'programming', 'is', 'easy', 'understand']
count = 0

for val in list_str:
    #print(val,'val =',len(val))
    if len(val) > count:
        count = len(val)
print("length of the largest string in list is: ", count)
print("_"*100)

"""
3. Python string program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
"""

# define input string
# get last 2 char of string
# 4 copies of last 2 char of string (multiply last_two_char * 4 ) and print str

input_str1 = "Python"
last_two_char = input_str1[-2:]
print(last_two_char*4)


"""
4) Python string program to reverse a string if it’s length is a multiple of 4.
"""
input_str3 = "sqatools"

if len(input_str3) % 4 ==0:
    #reverse string
    print("reverse string",input_str3[::-1])

else:
    print()

"""
5). Python string program to count occurrences of a substring in a string.
"""
input_str4 = "python program program"
sub_str = "program"
count_sub_str = input_str4.count(sub_str)
print("occurance of substring is: ", count_sub_str)

"""
6. Python string program to test whether a passed letter is a vowel or consonant.
"""
s1 = 'vocal'
s2 = 'aeiou'
for val in s1:
    if val=='a' or val == 'e' or val =='i' or val == 'o' or val =='u':
        print(f"{val} is vowel")
    else:
        print(f"{val} is consonant")
print("_"*100)

"""
7.Find the longest and smallest word in the input string.
"""
input_str5 = 'python is easy programming language'

str_to_list = input_str5.split(" ")
#print(str_to_list)

long_str_count = 0
small_str_count = len(str_to_list[0])

for val in str_to_list:
    if len(val) > long_str_count:
        long_str_count = len(val)

    if len(val) < small_str_count:
        print(f"{val} : {small_str_count}")
        small_str_count = len(val)

print("Longest String Count: ", long_str_count)
print("Small String Count: ", small_str_count)
print("_"*100)

"""
Doubt: 8.Print most simultaneously repeated characters in the input string.
"""
input_str6 = "programming Hello madam "
max_repeat_char = ''
max_repeat_count = 0
temp = 1


for char in range(len(input_str6) - 1):
    if input_str6[char] == input_str6[char+1]:
        temp = temp + 1
        if temp > max_repeat_count:
            max_repeat_count = temp
            max_repeat_char = input_str6[char]
        else:
            temp = 1
print(f" Max char: {max_repeat_char} \n Max Count: {max_repeat_count}")
print("_"*100)

"""
9. Write a Python program to calculate the length of a string with loop logic.
"""
input_str7 = "madhuri rahane"
count = 0
for i in input_str7:
    count = count + 1
print(f"Length of string is: {count}")

"""
10). Write a Python program to replace the second occurrence of any char with the special character $.
Input = “Programming”
Output = “Prog$am$in$”
"""

input_str8 = "Programming"
repeat_count = 0
result_str = ''

for char in input_str8:
    if char in result_str:
        result_str = result_str + '$'
    else:
        result_str = result_str + char
print("Result of string to replace the second occurrence of any char with $ is: ",result_str)



