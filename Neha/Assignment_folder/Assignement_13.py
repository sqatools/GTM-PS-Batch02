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

# print(school['Students']['10th'][0]['phone']) #67854322
#
# school['Students']['10th'][0]['phone'] =1234
# print(school)

# write a program to update student info with phone
# Get specified person details with mobile number
per_phone = 67854322
Student_details = school.get('Students')['10th'][0]
for key, values in Student_details.items():
    print(values)
    for data in values:
        if data ['phone'] == per_phone:
            input_Name = input("Please enter Name :")
            input_email = input("Please enter new details of with this format : email,id@gmail.com :")
            input_Rollno = input("Enter Student rollno: ")
            input_mobile = input("Enter Student Mobile: ")
            data['student_name'] = input_Name
            data['student_email'] = input_email
            data['Student_add'] = input_Rollno
            data['student_mobile'] = input_mobile
        else:
            continue

print("student details :", school['Students'])


"""
input_phone = int(input('Enter phone number you want to update: '))
flag = 0
flag2 = 0
output = {}

students = school.get('Students')
for key, values in students.items():
    for data in values:
        if data['phone'] == input_phone:
            # flag = 1
            # break
            input_name = input("Enter student Name: ")
            input_email = input("Enter Student Email: ")
            input_address = input("Enter Student Address: ")
            input_mobile = input("Enter Student Mobile: ")
            data['student_name'] = input_name
            data['email'] = input_email
            data['address'] = input_address
            data['phone'] = input_mobile
        else:
            continue

print("student details :", school['Students'])
"""


print("#" * 50)
# # Add/update person information on the basis of mobile number
# # write a program to get any person details with phone

#
# for k, v in company.items():
#     for data in v:
#         if data['phone'] == per_phone:
#             data[new_key] = new_value
#         else:
#             continue
#
# print("company :", company)
#
# #Get details
# for key, values in company.items():
#     # print(values)
#     for data in values:
#         # print(data['name'])
#         if data['phone'] == per_phone:
#             print(data)
#         else:
#             continue