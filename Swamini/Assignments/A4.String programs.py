"""print("Hi this is feature branch ")

write python program get following output

str1= "Hello Good Morning"
output = "gello Good MorninH"

str2 = "Python Programming"
output2 = "Pto rgamn"

print(str2[:7:1])

str3 = "Learning Python"
output = "gninraeL nohtyP"

str4 = "Good Evening"
output4 = "GGood Eveningg"
"""


#assignemnets1#

str1= "Hello Good Morning"
output = "gello Good MorninH"
c=str1[0]
d=str1[-1]

str1=f"{d}ello Good Mornin{c}"
print(str1)

print("*"*50)
#assignemnets2#
str2 = "Python Programming"
output2 = "Pto rgamn"

print(str2[:17:2])

print("*"*50)

#assignemnets4#
str4 = "Good Evening"
output4 = "GGood Eveningg"
a=str4[0]
b=str4[-1]
str4="{}Good Evening{}".format(a,b)
print(str4)

print("*"*50)

#assignemnets3#

str3 = "Learning Python"
output = "gninraeL nohtyP"

print(str3[-8::-1],""+str3[-1:-7:-1])




