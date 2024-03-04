# dict1 = {'key' : 'value'}

"""
#properties :
 ->  dict store the data in key value formate
 ->  dict is mutable data type, we can modify at any point of time.
 ->  Only immutable data type can be key in the dict e.g int, float, string, tuple, boolean
 ->  All type of data can value in the dict, int, float, string, list, tuple, dict, set, boolean
 ->  dict only contains unique keys, it means duplicate keys are not allowed.
     if we defined duplicate key then latest defined data will be considered.
"""


dict1 = {'a' : 456,
         4: 'Hello',
         4.5 : [4, 7, 8],
         (1, 4, 6) : {'a' : 4567, 'b' : 123},
         True : {5, 7, 9, 2},
         }

print(dict1)
# {'a': 456, 4: 'Hello', 4.5: [4, 7, 8], (1, 4, 6): {'a': 4567, 'b': 123}, True: {9, 2, 5, 7}}

# access data from dict
print(dict1[True])   # {9, 2, 5, 7}
print(dict1[4.5][1]) # 7

# add new data to the dict
dict1[False] = [4, 7, 8, 2, 5]

print(dict1)
# {'a': 456, 4: 'Hello', 4.5: [4, 7, 8], (1, 4, 6): {'a': 4567, 'b': 123}, True: {9, 2, 5, 7}, False: [4, 7, 8, 2, 5]}

# Program : Create a dictionary with the given two lists
list1 = ['a', 'b', 'c', 'd']
list2 = [123, 456, 78, 9]
# output = {'a' : 1234, 'b' : 456, 'c' : 78, 'd' : 9}
output = {}
for i in range(len(list1)):
    output[list1[i]] = list2[i]

print("output :", output)

print("_"*50)
# Program: write a python get below result

str1 = "Python"
list1 = [4, 6, 8, 2, 9, 10]
#output = {'PP' : 4, 'yy' : 6, 'tt' : 8, 'hh': 2, 'oo': 9, 'nn' : 10}

output1 = {}
for i in range(len(str1)):
    output1[str1[i]*2] = list1[i]


print("Result :", output1)
# Result : {'PP': 4, 'yy': 6, 'tt': 8, 'hh': 2, 'oo': 9, 'nn': 10}


print("_"*50)
################## Apply loop on the dictionary ############
dict2 = {'Name' : 'Rahul', 'Age' : 24, 'Address' : 'Mumbai'}

for data in dict2.items():
    print(data)

print("_"*50)

for key, val in dict2.items():
    print(key , " : ", val)


# Methods of dict
print(dir(dict))

#  'clear', 'copy', 'fromkeys', 'get', 'items',
#  'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

# items method : this method return the key value pair in form list of tuples.

print(dict2.items())
# dict_items([('Name', 'Rahul'), ('Age', 24), ('Address', 'Mumbai')])

# Get Method : This method return specific value with the help of keys
dict_a =  {'a' : 456, 'b' : 333, 'c' : 123}
val = dict_a.get('c')
print(val) # 123

print(dict_a['c'])  # 123

# keys() method: this method return list of keys
print(dict_a.keys())  # dict_keys(['a', 'b', 'c'])

# values method : this method return list of values
print(dict_a.values()) # dict_values([456, 333, 123])


print("*"*50)
# update method : this method update the data from dict1 to dict2
dict1 = {'name' : 'John', 'email' : 'john@gmail.com', 'address' : 'Mumbai'}
dict2 = {'phone' : 656456456, 'country' : 'India', 'occupation' : 'Business'}

dict1.update(dict2)

print("dict1 :", dict1)
print("dict2 :", dict2)


# Remove data from dictionary

# pop() method : This method remove data from the dictionary with the help of key
# and return the value

dict_b =  {'name': 'John', 'email': 'john@gmail.com', 'address': 'Mumbai', 'phone': 656456456, 'country': 'India', 'occupation': 'Business'}

val = dict_b.pop('address')
print("remove data :", val)
print("dict_b :", dict_b)
# {'name': 'John', 'email': 'john@gmail.com', 'phone': 656456456, 'country': 'India', 'occupation': 'Business'}

# popitem() method : This method remove data from the dictionary in the combination key and value and return
# it with tuple combination

dict_c = {'name': 'John', 'email': 'john@gmail.com', 'phone': 656456456, 'country': 'India', 'occupation': 'Business'}
output = dict_c.popitem()
print("removed data  : ", output)
# ('occupation', 'Business')
print("dict_C :", dict_c)
# dict_C : {'name': 'John', 'email': 'john@gmail.com', 'phone': 656456456, 'country': 'India'}

###################
# clear() method : this method remove all the data from dict

dict_d = {'name': 'John', 'email': 'john@gmail.com', 'phone': 656456456, 'country': 'India'}
dict_d.clear()
print("dict d:", dict_d)
# dict d: {}

# ############
# remove dict variable from memory using del

dict_e = {'name': 'John', 'email': 'john@gmail.com', 'phone': 656456456, 'country': 'India'}
# del dict_e
# print("dict_e :", dict_e)  # it will completely delete the dict object from memory
# NameError: name 'dict_e' is not defined. Did you mean: 'dict_a'?


del dict_e['phone']
print("dict_e :", dict_e)
# dict_e : {'name': 'John', 'email': 'john@gmail.com', 'country': 'India'}

####################
# setdefault method : This method update the default value for new  key in the dictionary, if the
# key is already available then it will the original value associated with the key.

dict_f = {'name': 'John', 'email': 'john@gmail.com', 'country': 'India'}

#output = dict_f.setdefault('email', 'Hello')  # output : john@gmail.com
output = dict_f.setdefault('Phone', 'Hello')  # output : Hello

print("output :", output) # # output : Hello
print("dict_f:", dict_f)
# dict_f: {'name': 'John', 'email': 'john@gmail.com', 'country': 'India', 'Phone': 'Hello'}

print("_"*40)
###########################################

list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [123, 456, 78, 9]
# output = {'a' : 1234, 'b' : 456, 'c' : 78, 'd' : 9}
output = {}
for i in range(len(list1)):
    if i < len(list2):
        output[list1[i]] = list2[i]
    else:
        output[list1[i]] = None

print("output :", output)

#################################################
# Question
# Write a python program to get below result
# Question1
list1 = [5, 7, 9, 3, 17, 2]
output = {'A' : 5, 'B' : 7, 'C': 9, 'D': 3, 'E' : 17, 'F' : 2}

# Question2
Str1 = "We are Learning Python Programming"
Output = {"wE" : "2We2", "AE" : "3are3", "lG": "8Learning8", "pN" : "6Python6", "pG" : "11Programming11"}

word_list = Str1.split(" ")
output2 = {}
for word in word_list:
    key = word[0].swapcase() + word[-1].swapcase()
    value = f"{len(word)}{(word)}{len(word)}"
    output2[key] = value

print(output2)
# {'wE': '2We2', 'AE': '3are3', 'lG': '8Learning8', 'pN': '6Python6', 'pG': '11Programming11'}




company = {
    'IT': [
        {'name': 'sanjay', 'email': 'sanjay@gmail.com', 'phone': 5654645, 'address': 'mumbai'},
        {'name': 'Neha', 'email': 'neha@gmail.com', 'phone': 434343, 'address': 'Pune'},
        {'name': 'Saumya', 'email': 'Saumya@gmail.com', 'phone': 33333232, 'address': 'Bangalore'},
    ],
    'HR': [
        {'name': 'priyanka', 'email': 'priyanka@gmail.com', 'phone': 8767657, 'address': 'Chennai'},
        {'name': 'swamini', 'email': 'swamini@gmail.com', 'phone': 98978998, 'address': 'Indore'},
        {'name': 'Bharath', 'email': 'Bharath@gmail.com', 'phone': 2332423432, 'address': 'Bhopal'},
    ]
}

print(company['HR'][2]['email'])  # Bharath@gmail.com

print(company['IT'][1]['email'])  # neha@gmail.com

print(company['IT'][2]['email'])  # Saumya@gmail.com

# update email id
company['IT'][2]['email'] = "Saumya2024@gmail.com"
# add new key value to the dictionary
company['IT'][2]['Country'] = "India"

print(company['IT'][2]['email'])

print(company)

dict1 = {'a': [4, 5, 6], 'b': [7, 8, 9]}
print(dict1.items())

print("#" * 60)

# Get specified person details with mobile number
per_phone = 98978998
for key, values in company.items():
    # print(values)
    for data in values:
        # print(data['name'])
        if data['phone'] == per_phone:
            print(data['name'], data['email'])
        else:
            continue

print("#" * 50)
# add/update person information on the basis of mobile number
per_phone = int(input("Please enter mobile the number :"))
new_data = input("Please enter new details of with this format : salary,767876576 :")
new_key = new_data.split(",")[0]
new_value = new_data.split(",")[1]
print("new_key :", new_key)
print("new_value :", new_value)

for k, v in company.items():
    for data in v:
        if data['phone'] == per_phone:
            data[new_key] = new_value
        else:
            continue

# print("company :", company)

# Get details
for key, values in company.items():
    # print(values)
    for data in values:
        # print(data['name'])
        if data['phone'] == per_phone:
            print(data)
        else:
            continue

# assignment to design dictionary structure of school institute
# write a program to update student info with phone
# write a program to get any person details with phone
# write a program to update teachers details with email

school = {
    'teacher': {
        'maths': [{'name': 'Bharath','email': 'sanjay@gmail.com', 'phone': 5654645, 'address': 'mumbai'}],
        'physics': [{'name': 'Rajiv','email': 'rajiv@gmail.com', 'phone': 5654645, 'address': 'mumbai'}],
        'chemistry': [{'name': 'Rakul','email': 'rakul@gmail.com', 'phone': 5654645, 'address': 'mumbai'}],
        'english': [{'name': 'Rahul','email': 'rahul@gmail.com', 'phone': 5654645, 'address': 'mumbai'}],
        'Hindi': [{'name': 'Krishna','email': 'krishna@gmail.com', 'phone': 5654645, 'address': 'mumbai'}]
    },
    'Students': {
        '10th': [{'name': 'Kiran','email': 'kiran@gmail.com', 'phone': 5654645, 'address': 'mumbai'}],
        '11th': [{'name': 'Chethan','email': 'chetan@gmail.com', 'phone': 5654645, 'address': 'mumbai'}],
        '12th': [{'name': 'Das','email': 'das@gmail.com', 'phone': 5654645, 'address': 'mumbai'}],

    },

    'Administrator': {
        'account': [{'name': 'Sandy','email': 'sandy@gmail.com', 'phone': 5654645, 'address': 'mumbai'}],
        'registration': [{'name': 'Rakesh', 'email': 'rakesh@gmail.com', 'phone': 5654645, 'address': 'mumbai'}]

    }

}

# write a program to update student info with phone

#company['IT'][2]['email'] = "Saumya2024@gmail.com"

print(school['Students']['10th'][0]['phone']) == 1234567879
print(school['Students']['10th'][0])