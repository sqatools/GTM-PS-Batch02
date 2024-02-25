#write python program get following output
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

str1= ("Hello Good Morning")

print(str1[-1]+str1[1:17]+str1[0]) #output gello Good MorninH

print("*"*70)

str2 = "Python Programming"
print(str2[::2]) #output Pto rgamn

print("*"*70)

str3 = "Learning Python"

str_1 = str3[-8:-16:-1]
str_2 = str3[-1:-7:-1]
print(str_1+" "+str_2) #output gninraeL nohtyP

print("*"*70)

str4 = "Good Evening"
print(str4[0]*2+str4[1:11]+str4[-1]*2) #output GGood Eveningg


