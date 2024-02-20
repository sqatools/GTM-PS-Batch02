# Slicing pratice programs

"""
write python program get following output

str1= "Hello Good Morning"
output = "gello Good MorninH"

str2 = "Python Programming"
output2 = "Pto rgamn"


str3 = "Learning Python"
output = "gninraeL nohtyP"

str4 = "Good Evening"
output4 = "GGood Eveningg"
"""

str1= "Hello Good Morning"  # "gello Good MorninH"
output = str1[-1] + str1[1:-1] + str1[0]
print(output)

str2 = "Python Programming" #"Pto rgamn"
output2 = str2[0:5:2] + str2[8:-1:2]
print(str2[0::2])
print(output2)

str3 = "Learning Python" #"gninraeL nohtyP"
output3 = str3[-1::-1]
print(output3)

str4 = "Good Evening" #"GGood Eveningg"
output4 = str4[0]*2+str4[1:-1]+str4[-1]*2
print(output4)