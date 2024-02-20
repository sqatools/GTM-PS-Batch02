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
