# assignment to design dictionary structure of school institute
# write a program to update student info with phone
# write a program to get any person details with phone
# write a program to update teachers details with email

school = {
    'teacher': {
            'maths': [
                {'name':'Manisha' , 'email':'manisha@gmail.com','degree': 'TGT'},
                {'name':'Vijay' , 'email':'vijay@gmail.com','degree': 'Btech'},
                      ],
            'physics': [
                {'name': 'Jyoti', 'email': 'jyoti@gmail.com', 'degree': 'PGT'},
                {'name': 'Kanchan', 'email': 'kanchan@gmail.com', 'degree': 'TGT'},
                        ],
            'chemistry': [
                {'name': 'Peeyush', 'email': 'peeyush@gmail.com', 'degree': 'Btech'},
                {'name': 'Ajay', 'email': 'ajay@gmail.com', 'degree': 'Btech'},
                        ],
            'english': [
                {'name': 'Smitha', 'email': 'smitha@gmail.com', 'degree': 'TGT'},
                {'name': 'Anu', 'email': 'anu@gmail.com', 'degree': 'MBA'},
            ],
            'Hindi': [
                {'name': 'Deepika', 'email': 'deepika@gmail.com', 'degree': 'TGT'},
                {'name': 'Priyanka', 'email': 'priyanka@gmail.com', 'degree': 'TGT'},
            ],
        },
    'Students': {
            '10th': [
                {'name': 'Ketan', 'email': 'ketan@gmail.com', 'Section':'A','Rollno':'18','phone': 67854322},
                {'name': 'Lakshmipriya', 'email': 'lakshmipriya@gmail.com', 'Section':'B','Rollno':'26','phone':987654},
            ],
            '11th': [
                {'name': 'Divya', 'email': 'divya@gmail.com', 'Section': 'B', 'Rollno': '23','phone':987654},
                {'name': 'Bhumika', 'email': 'bhumika@gmail.com', 'Section': 'C', 'Rollno': '15','phone':1234556}
            ],
            '12th': [
                {'name': 'Perila', 'email': 'perila@gmail.com', 'Section': 'C', 'Rollno': '40','phone':5854368},
                {'name': 'Raju', 'email': 'raju@gmail.com', 'Section': 'B', 'Rollno': '31','phone':987654}
            ],
    },
    'Administrator': {
        'account': [
            {'name': 'Nandi', 'email': 'nandi@gmail.com', 'phone': 98766544, 'department': 'account'},
            {'name': 'Badri', 'email': 'badri@gmail.com', 'phone': 3456782, 'department': 'account'},
        ],
        'registration': [
            {'name': 'Jyotsana', 'email': 'jyotsana@gmail.com', 'phone': 5643219, 'department': 'reg'},
            {'name': 'Sai', 'email': 'sai@gmail.com', 'phone': 67897543, 'department': 'reg'},
        ]

    }
}

print(school)

## write a program to update student info with phone

print(school['Students']['10th'][0]['phone']) #67854322

school['Students']['10th'][0]['phone'] =1234
print(school)

# write a program to update student info with phone
# Get specified person details with mobile number
per_phone = 67854322
for key, values in school.items():
    print(values)
    for key1,values1 in values:
         print(data['name'])
         if data['phone'] == per_phone:
            print(data['name'],data['email'])
    #     else:
    #         continue

# print("#" * 50)
# Add/update person information on the basis of mobile number
# write a program to get any person details with phone
# per_phone = int(input("Please enter mobile the number :"))
# new_data = input("Please enter new details of with this format : email,id@gmail.com :")
# new_key = new_data.split(",")[0]
# new_value = new_data.split(",")[1]
# print("new_key :", new_key)
# print("new_value :", new_value)
#
# for k, v in company.items():
#     for data in v:
#         if data['phone'] == per_phone:
#             data[new_key] = new_value
#         else:
#             continue

# print("company :", company)

# Get details
# for key, values in company.items():
#     # print(values)
#     for data in values:
#         # print(data['name'])
#         if data['phone'] == per_phone:
#             print(data)
#         else:
#             continue