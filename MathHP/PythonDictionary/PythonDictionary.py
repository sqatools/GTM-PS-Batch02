




























##################################
# clear() method: This method remove all data


###########
# Remove dict variable from memory using del

dict_e = {'name':'John','email':'john@gmail.com','phone':6567890,'country':'India'}
#del dict_e
#print("dict_e:",dict_e)         # It will completely delete dict from memory
#NameError: name 'dict_e' is not defined. Did you mean: 'dict'?

del dict_e['phone']
print("dict_e:",dict_e)
#dict_e: {'name': 'John', 'email': 'john@gmail.com', 'country': 'India'}

##### setdefault method
# If value is there for a key, then same value printed
# If key is not available , then it will take new key and new value

dict_f={'name':'John','email':'john@gmail.com','phone':6567890,'country':'India'}
output=dict_f.setdefault('email','Hello')  #john@gmail.com
print("output:",output)
output=dict_f.setdefault('phone','Hello')  #output: 6567890
print("output:",output)
output=dict_f.setdefault('phone',None)    #output: 6567890
print("output:",output)
output=dict_f.setdefault('DOB',None)  #dict_f: {'name': 'John', 'email': 'john@gmail.com', 'phone': 6567890, 'country': 'India', 'DOB': None}
print("dict_f:",dict_f)

#################################################
# Questions
# WAP to get below result
#Q1)
# list1 =[5,7,9,3,7,2]
# output={'A':5,'B':7,'C':9,'D':3,'E':17,'F':2}

list1 = [5, 7, 9, 3, 7, 2]

# Define alphabets to assign to elements
alphabets = ['A', 'B', 'C', 'D', 'E', 'F']

# Calculate the sum of list1 along with alphabets
output = {}
for i in range(len(list1)):
    output[alphabets[i]] = list1[i]

# Adding the sum of the list to the output dictionary
output['E'] = sum(list1)

print(output)
print("_"*60)

###################################################

# Question2
Str1 = "We are Learning Python Programming"
Output = {"wE" : "2We2", "AE" : "3are3", "lG": "8Learning8", "pN" : "6Python6", "pG" : "11Programming11"}

Str1 = "We are Learning Python Programming"

# Initialize an empty dictionary to store the output
output = {}

# Iterate through the string Str1
for char in Str1:
    # Check if the character is an alphabet
    if char.isalpha():
        # Count the occurrences of the character in Str1
        count = Str1.count(char)
        # Construct the output string as per the format specified
        output[char.upper() + char.lower()] = str(count) + char.upper() + str(count)

print(output)
print("_"*60)


