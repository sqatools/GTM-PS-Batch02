"""
11). Write a python program to get to swap the last character of a given string.
Input = “SqaTool”
Output = “IqaTooS”

"""
"""
12). Write a python program to exchange the first and last character of each word from the given string.
Input = “Its Online Learning”
Output = “stI enlino gearninL”
"""
input_str1 = "Its Online Learning"
#convert string into list
str_to_list = input_str1.split(" ")
print(str_to_list)

result_str = ''
for val in str_to_list:
    result_str = result_str + ' ' + val[::-1]

print(result_str)

"""
Doubt: 13). Write a python to count vowels from each word in the given string show as dictionary output.
Input = “We are Learning Python Codding”
output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}
"""
input_str2 = "We are Learning Python Codding"
vowels = 'aeiou'

list1 = input_str2.split(" ")

result_dict = dict()

for word in list1:
    count = 0
    for char in word:
        if char in vowels:
            count = count + 1
    result_dict[word] = count

print("Dictionary count of vowels in string is:  ",result_dict)



