# Question
# Write a python program to get below result
# Question1
"""
list1 = [5, 7, 9, 3, 17, 2]
output = {'A' : 5, 'B' : 7, 'C': 9, 'D': 3, 'E' : 17, 'F' : 2}

# Question2
Str1 = "We are Learning Python Programming"
Output = {"wE" : "2We2", "AE" : "3are3", "lG": "8Learning8", "pN" : "6Python6", "pG" : "11Programming11"}
"""

# Question1
#list1 = [5, 7, 9, 3, 17, 2]
#output = {'A' : 5, 'B' : 7, 'C': 9, 'D': 3, 'E' : 17, 'F' : 2}

lista = ['A','B','C','D','E','F']
list1 = [5, 7, 9, 3, 17, 2]

output = {}
for i in range(len(lista)):
    output[lista[i]] = list1[i]

print("output =", output)

# Question2
#Str1 = "We are Learning Python Programming"
#Output = {"wE" : "2We2", "AE" : "3are3", "lG": "8Learning8", "pN" : "6Python6", "pG" : "11Programming11"}

Str1 = "We are Learning Python Programming"
Str2 = Str1.swapcase()
Str3 = Str2.split(" ")
print('Str3=', Str3)
list1 = []
for word in Str3:
    print(word[0]+word[-1])


