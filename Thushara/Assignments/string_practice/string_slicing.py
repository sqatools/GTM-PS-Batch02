"""
write python program to get the following output

str1= "Hello Good Morning"
output = "gello Good MorninH"

str2 = "Python Programming"
output2 = "Pto rgamn"


str3 = "Learning Python"
output = "gninraeL nohtyP"

str4 = "Good Evening"
output4 = "GGood Eveningg"
"""

str1 = "Hello Good Morning"
new_str1 = str1[-1]+str1[1:17]+str1[0]
print(new_str1)
print("#"*50)

str2 = "Python Programming"
new_str2 = str2[0:18:2]
print(new_str2)
print("#"*50)
str3 = "Learning Python"
new_str3 = str3[7::-1] +" "+str3[:7:-1]
print(new_str3)
print("#"*50)
str4 = "Good Evening"
new_str4 = str4[0]*2+ str4[1:10]+ str4[-1]*2
print(new_str4)
