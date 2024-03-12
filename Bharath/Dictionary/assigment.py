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

school['Students']['12th'][0]['phone']=123456789

print(school['Students']['12th'][0]['phone'])

per_phone = int(input("Please enter mobile the number :"))
new_data = input("Please enter new phone, newphone,767876576 " )
new_key = new_data.split(",")[0]
new_value = new_data.split(",")[1]
print("new_key :", new_key)
print("new_value :", new_value)


for k, v in school.items():
    for data in v:
        if data['phone:'] == per_phone:
            data[new_key] = new_value
        else:
            continue



