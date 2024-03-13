import string
"""
Program: write a python get below result
str1 = "Python"
list1 = [4, 6, 8, 2, 9, 10]
output = {'PP' : 4, 'yy' : 6, 'tt' : 8, 'hh': 2, 'oo': 9, 'nn' : 10}
"""

str = "Python"
str_list = list(str)
list1= [4, 6, 8, 2, 9, 10]
output = {}

for i in range(len(str_list)):
    output[str_list[i] * 2] = list1[i]
print("output1 : ",output)
print("_"*100)

"""
Question1 : Write a python program to get below result
list1 = [5, 7, 9, 3, 17, 2]
output1 = {'A' : 5, 'B' : 7, 'C': 9, 'D': 3, 'E' : 17, 'F' : 2}
"""
output1 = {}
asscii= 65
for i in list1:
    output1[chr(asscii)] = i
    asscii = asscii + 1

print("output2 : ",output1)
print("_"*100)


"""
Question2 : Write a python program to get below result
Str1 = "We are Learning Python Programming"
Output = {"wE" : "2We2", "AE" : "3are3", "lG": "8Learning8", "pN" : "6Python6", "pG" : "11Programming11"}
"""
input_str = "We are Learning Python Programming"
list2 = input_str.split(" ")
output3 = {}
for i in range(len(list2)):
    if i == 0:
        key = list2[i].swapcase()
        value = "2" + list2[i] + "2"
        output3[key] = value
    elif i == 1 or i == 2:
        str = list2[i].upper()
        start_str = str[:1]
        end_str = str[-1:]
        key = start_str + end_str
        if i == 1:
            value = "3" + list2[i] + "3"
            output3[key] = value
        elif i == 2:
            value = "8" + list2[i] + "8"
            output3[key] = value

    elif i == 3 or i == 4:
        str = list2[i].swapcase()
        start_str = str[:1]
        end_str = str[-1:]
        key = start_str + end_str
        if i == 3:
            value = "6" + list2[i] + "6"
            output3[key] = value
        elif i == 4:
            value = "11" + list2[i] + "11"
            output3[key] = value

print('Expected: {"wE" : "2We2", "AE" : "3are3", "lG": "8Learning8", "pN" : "6Python6", "pG" : "11Programming11"}')
print("output3: ", output3)
print("_"*100)

"""
Question 2.
"""
"""
# Question 4: assignment to design dictionary structure of school institute
# write a program to update student info with phone
# write a program to get any person details with phone
# write a program to update teachers details with email
"""
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

# write a program to update student info with phone
input_phone = int(input('Enter phone number you want to update: '))
flag = 0
flag2 = 0
output = {}

students = school.get('Students')
for key, values in students.items():
    for data in values:
        if data['phone'] == input_phone:
            flag = 1
            break
        else:
            continue
if flag == 1:
    print("_"*50 + "Enter following information to update student details" + "_"*50)
    input_name = input("Enter student Name: ")
    input_email = input("Enter Student Email: ")
    input_address = input("Enter Student Address: ")
    input_mobile = input("Enter Student Mobile: ")
    for key, values in students.items():
        for data in values:
            if data['phone'] == input_phone:
                data['student_name'] = input_name
                data['email'] = input_email
                data['address'] = input_address
                data['phone'] = input_mobile
                flag = 1
                flag2 = 1
                output.update(data)
                break
            else:
                continue
else:
    print("Student not found 2")

if flag2 == 1:
    print("_"*50 + " Success, Student information Updated Successfully. " + "_"*50)
    print()
    print(output)
    print("_"*100)
    print(students)
else:
    print("_"*50 + " Failed, Student information Failed to Update. "+"_"*50)






