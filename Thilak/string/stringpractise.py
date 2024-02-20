st1 = "Hi "
st2 = "Good morning"
print(st1 + st2)

# out

str1 = "Hello Good Morning"

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
#print(dir(str))
print("-"*40)
str1 = "Hello Good Morning"
print("g",str1[1:17],"H")
print(str1[:-2:-1],str1[1:17],str1[:1:1])
print("_"*40)
#str2 = "Python Programming"-output2 = "Pto rgamn"
str2 = "Python Programming"
print(str2[0:18:2])
print("_"*40)
str3 = "Learning Python"
#output = "gninraeL nohtyP"
print(str3[-8:0:-1], str3[-1:8:-1])

str4 = "Good Evening"
#output4 = "GGood Eveningg"
print(str4[0:1], str4[1:12], str4[:-2:-1])
