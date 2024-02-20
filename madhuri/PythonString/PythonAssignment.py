"""
write python program get following output

1.str1= "Hello Good Morning"
output = "gello Good MorninH"

2. str2 = "Python Programming"
output2 = "Pto rgamn"


3. str3 = "Learning Python"
output = "gninraeL nohtyP"

4. str4 = "Good Evening"
output4 = "GGood Eveningg"

"""
"""
3. str3 = "Learning Python"
output = "gninraeL nohtyP"
"""

str3 = "Learning Python"
#convert string into list
str3_list = str3.split(" ")
print(str3_list)
result = ''

for word in str3_list:
    result = result + ' '+word[::-1]
print("str3 output: ",result)
