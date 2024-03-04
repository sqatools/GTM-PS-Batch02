# assignment to design dictionary structure of school institute
# write a program to update student info with phone
# write a program to get any person details with phone
# write a program to update teachers details with email
School = {
    'Teacher':
        {
         'Maths': [
             {'Name': 'Aarti', 'Phone': 5656565656, 'Address': 'Lucknow', 'Email_Id': 'aarti1@gmail.com'},
             {'Name': 'Swati', 'Phone': 5456565656, 'Address': 'Jaipur', 'Email_Id': 'swati2@gmail.com'}],
         'Physics': [
             {'Name': 'Sneha', 'Phone': 5656565786, 'Address': 'Lucknow', 'Email_Id': 'sneha3@gmail.com'},
             {'Name': 'Shalini', 'Phone': 7646565656, 'Address': 'New Delhi', 'Email_Id': 'shalini4@gmail.com'}],
         'Chemistry': [
             {'Name': 'Rohit', 'Phone': 8765565656, 'Address': 'Mumbai', 'Email_Id': 'rohit5@gmail.com'},
             {'Name': 'Mohit', 'Phone': 3456565656, 'Address': 'Pune', 'Email_Id': 'mohit6@gmail.com'}],
         'English': [
             {'Name': 'Sobit', 'Phone': 5657654656, 'Address': 'Mumbai', 'Email_Id': 'sobit7@gmail.com'},
             {'Name': 'Raj', 'Phone': 7676765656, 'Address': 'Kolkata',' Email_Id': 'raj8@gmail.com'}],
         'Hindi': [
             {'Name': 'Rahul', 'Phone': 9080565656, 'Address': 'Nagpur','Email_Id': 'rahul9@gmail.com'},
             {'Name': 'Akash', 'Phone': 908765656, 'Address': 'Kanpur', 'Email_Id': 'Akash10@gmail.com'}]
        },
    'Students':
        {
        '10th': [{'Name':'Pooja','Phone':9090898776,'Age':15,'Email_Id':'pooja1@gmail.com','Address':'New Delhi'},
                  {'Name':'Gaurav','Phone':7676564534,'Age':15,'Email_Id':'gaurav2@gmail.com','Address':'Mumbai'}],
        '11th': [{'Name':'Anu','Phone':7654345454,'Age':16,'Email_Id':'anu3@gmail.com','Address':'Nagpur'},
                  {'Name':'Ananya','Phone':6785890878,'Age':16,'Email_Id':'ananya4@gmail.com','Address':'Mumbai'}],
        '12th': [{'Name':'Sambit','Phone':7654321567,'Age':17,'Email_Id':'sambit5@gmail.com','Address':'New Delhi'},
                  {'Name':'Sohil','Phone':9011565656,'Age':17,'Email_Id':'sohil6@gmail.com','Address':'Lucknow'}],
        },
    'Administrator': {
        'Account': [{'Name':'Account1','Phone':8090709656,'Email_Id':'accountadmin1@gmail.com'},
                  {'Name':'Account2','Phone':9876543256,'Email_Id':'accountadmin2@gmail.com'}],
        'Registration': [{'Name':'Reg11','Phone':8767564578,'Email_Id':'Regadmin1@gmail.com'},
                  {'Name':'Reg22','Phone':9087654534,'Email_Id':'Regadmin2@gmail.com'}]
    }
}

print('*'*70)

#write a program to update student info with phone.

User_Phone = int(input("Enter student phone number to search : "))
Stud_Email = input("Enter email id to update : ")
Stud_Address = input("Enter address tp update : ")
Student = School.get('Students')
for Stud_Key,Stud_Value in Student.items():
    for data in Stud_Value:
        if data['Phone'] == User_Phone:
           data['Email_Id'] = Stud_Email
           data['Address'] = Stud_Address
print(School)


# write a program to get any person details with phone
User_Phone = int(input("Enter the Person's phone number to search : "))
for School_keys,School_values in School.items():
    for keys,values in School_values.items():
        for data in values:
            if data['Phone'] == User_Phone:
                print(f"Please find {data['Name']} details")
                print(data)
            else:
                continue



#3.write a program to update teachers details with email.

#Teach_Email = input("Enter Teacher email id to search : ")
Teach_Email = 'shalini4@gmail.com'
Teach_Address = input("Enter address to update : ")
Teach_Phone = int(input("Enter Phone number to update : "))
Teachers = School.get('Teacher')
for Teach_Key,Teach_Value in Teachers.items():
    for data in Teach_Value:
        if data['Email_Id'] == Teach_Email:
            if data['Address'] == Teach_Address and data['Phone'] == Teach_Phone:
                continue
            elif data['Address'] != Teach_Address:
                 data['Address'] = Teach_Address
            elif data['Phone'] != Teach_Phone:
                 data['Phone'] = Teach_Phone
print(School)
