# print(dir(str))

"""
str1= "Hello Good Morning"
output = "gello Good MorninH"

str2 = "Python Programming"
output2 = "Pto rgamn"


str3 = "Learning Python"
output = "gninraeL nohtyP"

str4 = "Good Evening"
output4 = "GGood Eveningg"
"""

str1= "Hello Good Morning"
first_char = str1[0]
last_char = str1[-1]
middle = str1[1:-1]
print(last_char+middle+first_char) # output = "gello Good MorninH"

str2 = "Python Programming"
print(str2[0:-1:2]) # output2 = "Pto rgamn"

str3 = "Learning Python"
first_word = str3[-1:8:-1]
last_word = str3[-8::-1]
print(last_word+first_word) # output = "gninraeL nohtyP" //gninraeLnohtyP

str4 = "Good Evening"
first = str4[0:1]
last = str4[-1:]
middle = str4[1:-1]
print(first+first+middle+last+last) # output4 = "GGood Eveningg"
print(first*2+middle+last*2)
