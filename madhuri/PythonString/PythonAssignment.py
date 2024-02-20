"""
write python program get following output

1.str1= "Hello Good Morning"
output = "gello Good MorninH"

str1.split(" ")
temp = ''
for val in str1:
    temp = val[0]
    val[0] = val[-1]
    val[-1] = val[0]
print("Answer1 After: ",str1)
print("_"*100)


"""
str1= "Hello Good Morning"

start_letter = str1[0]
end_letter = str1[-1]

# print( str1[1:-1]) # start from 1 end at -ve index -1

result_string = end_letter + str1[1:-1] + start_letter
print("Question 1: ", result_string)
print("_"*100)

"""
2. str2 = "Python Programming"
output2 = "Pto rgamn"
"""
str2 = "Python Programming"
print("Question 2 :", str2[0:18:2])


"""
3. str3 = "Learning Python"
output = "gninraeL nohtyP"

4. str4 = "Good Evening"
output4 = "GGood Eveningg"
"""
str4 = "Good Evening"
start_char = str4[0]
end_char = str4[-1]

result_str4 = start_char + str4 + end_char
print("Question 4 : ", result_str4)

print("_"*100)

"""
3. str3 = "Learning Python"
output = "gninraeL nohtyP"
"""

str3 = "Learning Python"
# convert string into list
str3_list = str3.split(" ")
# print(str3_list)
result = ''

for word in str3_list:
    result = result + " " + word[::-1]
print("Question 3 : ",result)
print("_"*100)
