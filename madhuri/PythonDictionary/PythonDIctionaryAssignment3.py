#2. write a program to get any person details with phone
school = {
    'teacher': {
        'maths': [
            {'teacher_id': 1, 'teacher_name': 'harsh mehta', 'email': 'harsh@gmail.com', 'phone': 9870675645, 'status': True, 'DOB': '1990-03-01', 'last_login': '2024-03-01 10:22:38.698449'},
            {'teacher_id': 2, 'teacher_name': 'teacher two', 'email': 'teachertwo@gmail.com', 'phone': 8877665544, 'status': True, 'DOB': '1993-09-09', 'last_login': '2024-03-01 18:12:08.698449'}
        ],
        'physics': [
            {'teacher_id': 1, 'teacher_name': 'aditya', 'email': 'adita@gmail.com', 'phone': 5645342313, 'status': True, 'DOB': '1999-03-01', 'last_login': '2023-12-30 13:22:38.698449'},
        ],
        'chemistry': [],
        'english': [],
        'Hindi': []
    },
    'Students': {
        '10th': [
            {'roll_no': 100, 'student_name': 'madhuri', 'email': 'madhuri@gmail.com', 'phone': 9860138618, 'address': 'pune'},
            {'roll_no': 101, 'student_name': 'pooja', 'email': 'pooja@gmail.com', 'phone': 9988776655, 'address': 'mumbai'},
        ],
        '11th': [
            {'roll_no': 200, 'student_name': 'rahul', 'email': 'rahul@gmail.com', 'phone': 9405003651, 'address': 'mumbai'},
        ],
        '12th': [
            {'roll_no': 300, 'student_name': 'dev', 'email': 'dev@gmail.com', 'phone': 9049929339, 'address': 'nasik'},
        ],
    },
    'Administrator': {
        'account': [
            {'acc_id': 1, 'acc_ref': '10th', 'acc_ref_id': 100, 'due_amount': 40000, 'phone': 1122334455},
            {'acc_id': 2, 'acc_ref': '11th', 'acc_ref_id': 200, 'due_amount': 10000,'phone': 6677889900}
        ],
        'registration': [
            {'reg_id': 1, 'registration_for_class': 10, 'reg_status': 'incomplete','reg_date': '2024-01-01', 'reg_fees': 10000, 'phone': 3456789090},
            {'reg_id': 2, 'registration_for_class': 11, 'reg_status': 'complete', 'reg_date': '2024-02-10', 'reg_fees': 15000, 'phone': 6655119988},
            {'reg_id': 3, 'registration_for_class': 10, 'reg_status': 'hold', 'reg_date': '2024-02-17', 'reg_fees': 20000, 'phone': 8967564534},
        ]
    }
}
print("_"*500)
input_phone = int(input('Enter phone number you want to search: '))
flag = 0
output = {}
department = ''

school_keys = school.keys()
# print(school_keys)
for skey in school_keys:
   # print(skey)
   innerdata = school.get(skey)
   for key, values in innerdata.items():
       # print(key, '- ', values)
       for data in values:
           # print('data---', data)
           if data['phone'] == input_phone:
               output.update(data)
               flag = 1
               department = skey
               break
           else:
               continue
if flag == 1:
    print("_" * 50 + " Success, Record Found in " + department +" Department " + "_" * 50)
    print(output)
else:
    print("_" * 50 + " Failed, Record Not Found " + "_" * 50)






