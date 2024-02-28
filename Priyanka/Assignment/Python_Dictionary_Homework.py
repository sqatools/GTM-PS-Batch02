# Write a python program to get below result
"""# Question1
list1 = [5, 7, 9, 3, 17, 2]
output = {'A' : 5, 'B' : 7, 'C': 9, 'D': 3, 'E' : 17, 'F' : 2}
"""
list1 = [5, 7, 9, 3, 17, 2]
output1 = {}
temp = 65

for i in range(len(list1)):
    output1[chr(temp+i)] = list1[i]

print("output : ",output1) # output :  {'A': 5, 'B': 7, 'C': 9, 'D': 3, 'E': 17, 'F': 2}

"""# Question2
Str1 = "We are Learning Python Programming"
Output = {"wE" : "2We2", "AE" : "3are3", "lG": "8Learning8", "pN" : "6Python6", "pG" : "11Programming11"}
"""
Str1 = "We are Learning Python Programming"
val = Str1.split(" ")
output2 = {}

for i in range(len(val)):
    key = val[i][0].swapcase()+val[i][-1].swapcase()
    value = f"{len(val[i])}{(val[i])}{len(val[i])}"
    output2[key] = value

print("Output : ", output2)
# {'wE': '2We2', 'AE': '3are3', 'lG': '8Learning8', 'pN': '6Python6', 'pG': '11Programming11'}