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

print("Modified output:", output_str)

print("__"*50)

str2 = "Python Programming"
#output= "Pto rgamn"
output_str2=str2[::2]
print("Modified output:", output_str2)


print("__"*50)

str3 = "Learning Python"
#output = "gninraeL nohtyP"
word= str3[-1: -18: -1] # nohtyP gninraeL
print(word)
x = word.split()
print(x) #['nohtyP', 'gninraeL']
y = x[-1::-1]
print(y) #['gninraeL', 'nohtyP']
reverse_str = ' '.join(y)

print("Modified output:", reverse_str)

print("__"*50)

input_str = "Good Evening"
#output4 = "GGood Eveningg"
output_str = input_str[0] + input_str[0] + input_str[1:] + input_str[-1]
print("Modified output:", output_str)

print("__"*50)

input = 'S@oftwar!e'
#output = e@rawtfo!S

output_str = (input[0].replace('S', 'e') + input[1:2] + input[-3:1:-1] +
              input[-2:-1]+input[-1].replace('e', 'S'))

print("Modified output:", output_str)