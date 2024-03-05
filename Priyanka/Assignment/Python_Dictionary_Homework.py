# Write a python program to get below result
"""# Question1
list1 = [5, 7, 9, 3, 17, 2]
output = {'A' : 5, 'B' : 7, 'C': 9, 'D': 3, 'E' : 17, 'F' : 2}

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
"""
# assignment to design dictionary structure of school institute
# write a program to update student info with phone
# write a program to get any person details with phone
# write a program to update teachers details with email

school = {
    'teacher': {
        'maths': [
                    {'name': 'priya', 'email': 'priya@gmail.com', 'phone': 9873465788, 'address': 'bengaluru'},
                    {'name': 'varun', 'email': 'varun@gmail.com', 'phone': 8734387458, 'address': 'bengaluru'},
                ],
        'physics': [
                    {'name': 'Harika', 'email': 'Harika@gmail.com', 'phone': 756346688, 'address': 'vijayanagar'},
                    {'name': 'Aiswarya', 'email': 'aiswarya@gmail.com', 'phone': 734646688, 'address': 'kerala'},
                ],
        'chemistry': [
                    {'name': 'vishnu', 'email': 'vishnu@gmail.com', 'phone': 887373233, 'address': 'kerala'},
                    {'name': 'divakar', 'email': 'divakar@gmail.com', 'phone': 97373676, 'address': 'bengaluru'},
                ],
        'english': [
                {'name': 'rakesh', 'email': 'rakesh@gmail.com', 'phone': 887373233, 'address': 'pune'}
        ],
        'Hindi': [
                {'name': 'shoaib', 'email': 'shoaib@gmail.com', 'phone': 887373233, 'address': 'chennai'}
        ]
    },
    'Students': {
        '10th': [
                    {'roll_no': 1001 , 'name': 'bumi', 'email': 'bumi@gmail.com', 'phone': 808965653},
                    {'roll_no': 1002 , 'name': 'Swapna', 'email': 'swapna@gmail.com', 'phone': 887373233},
        ],
        '11th': [
                    {'roll_no': 1101 , 'name': 'Sushmitha', 'email': 'suahmitha@gmail.com', 'phone': 796556783},
                    {'roll_no': 1102 , 'name': 'Sujith', 'email': 'Sujith@gmail.com', 'phone': 8765434},
        ],
        '12th': [
                    {'roll_no': 1201 , 'name': 'Teju', 'email': 'Teju@gmail.com', 'phone': 796556783},
                    {'roll_no': 1202 , 'name': 'Raj', 'email': 'Raj@gmail.com', 'phone': 8765434},
                 ],
    },

    'Administrator': {
        'account': [
                    {'name': 'priyanka', 'email': 'priyanka@gmail.com', 'phone': 87326674, 'address': 'bengaluru'}
                ],
        'registration': [
                    {'name': 'Ajith', 'email': 'Ajith@gmail.com', 'phone': 987654354, 'address': 'mumbai'}
        ]

    }

}

# write a program to update student info with phone
phone_no = 808965653
new_Phone_no = 100000
for key, val in school.items():
    for k1, v1 in val.items():
        for data in v1:
            if data['phone'] == phone_no:
                data['phone'] = new_Phone_no
                print(data)

"""
school_keys = school.keys()
for val in school_keys:
    data1 = school.get(val)
    for k1, v1 in data1.items():
        for data in v1:
            if data['phone'] == phone_no:
                data['phone'] = new_Phone_no
                print(data)
"""
# write a program to get any person details with phone
phone_no = 9873465788
for key, val in school.items():
    for k1, v1 in val.items():
        for data in v1:
            if data['phone'] == phone_no:
                print(data)

# write a program to update teachers details with email
email = "varun@gmail.com"
new_email = "newvarun@gmail.com"
for key, val in school.items():
    for k1, v1 in val.items():
        for data in v1:
            if data['email'] == email:
                data['email'] = new_email
                print(data)