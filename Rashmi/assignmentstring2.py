#1.string first and last 2 char if the string is less than 2
"""
str2 = 'morning'
if len(str2) < 2:
    print(True)
else:
    print(str2[-6:-1])
    print()
"""
#2.list of the string

"""
str1 = ["i", "an", "learning"]
temp = 0
for word in str1:
    a = len(word)
    if a > temp:
        temp = a
        print(temp)
"""
#3.pgm to find last 2 char multiply by 4
"""
str1 = "rashmi"
print(str1[-2:]*4)
"""
#4
"""
str1 = "hi good"
str1.count("goog")

"""

#7
"""
str1 = "we are learning python"
list1 = str1.split(" ")
print("long word", max(list1, key=len))
print("smallest word", min(list1, key=len))
"""
#8.calculate length of the string

str1 = " python programing"
str_len = len(str1)
count = 0
for i in range(str_len):
    print(str1[i], end=" ")
    for char in str1:
        count += 1
print(count)
print(len(str1))



