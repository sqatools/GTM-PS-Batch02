# Slicing practice programs

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
# """

print("__"*50)

input_str = "Hello Good Morning"
output_str = (input_str[0].replace('H', 'g') + input_str[1:17] +
             input_str[-1].replace('g', 'H'))

print("Modified output:", output_str)  #"gello Good MorninH"

#             or
word_1="g"
word_2= input_str[1:17]
word_3='H'#
output_str = word_1 + word_2 + word_3#
print("Modified output:", output_str)  #"gello Good MorninH"

print("__"*50)

str2 = "Python Programming"
output_str2=str2[::2]
print("Modified output:", output_str2) #output= "Pto rgamn"

print("__"*50)

str3 = "Learning Python"
word1=str3[8::-1]
word2= str3[-1:-7:-1]
output_str = word1 + " " + word2
print("Modified output:", output_str) # #output = "gninraeL nohtyP"

print("__"*50)

input_str = "Good Evening"
output_str = input_str[0] + input_str[0] + input_str[1:] + input_str[-1]
print("Modified output:", output_str)  # #output4 = "GGood Eveningg"

print("__"*50)

input = 'S@oftwar!e'
output_str = (input[0].replace('S', 'e') + input[1:2] + input[-3:1:-1] +
input[-2:-1]+input[-1].replace('e', 'S'))
print("Modified output:", output_str)  #output = e@rawtfo!S

## or

word1="e"
word2=input[1:2]
word3=input[-3:1:-1]
word4=input[-2:-1]
word5="S"
output_str = word1+word2+word3+word4+word5
print("Modified output:", output_str)  #output = e@rawtfo!S