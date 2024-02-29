

"""
# Question
# Write a python program to get below result
# Question1
#list1 = [5, 7, 9, 3, 17, 2]
#output = {'A' : 5, 'B' : 7, 'C': 9, 'D': 3, 'E' : 17, 'F' : 2}

# Question2
# Str1 = "We are Learning Python Programming"
# Output = {"wE" : "2We2", "AE" : "3are3", "lG": "8Learning8", "pN" : "6Python6", "pG" : "11Programming11"}

"""

list1 = [5, 7, 9, 3, 17, 2]
output_dict = {}
for i in range(len(list1)):
    output_dict[chr(65 + i)] = list1[i]

print(output_dict)

Str1 = "We are Learning Python Programming"

words = Str1.split()
output_dict2 = {}
for word in words:
    key = word[0].swapcase() + word[-1].swapcase()
    value = str(len(word)) + word + str(len(word))
    output_dict2[key] = value

print(output_dict2)
