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
print('*'*70)
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
#    print(key,values)
    for data in values:
#        print(data['name'])
        if data['phone'] == per_phone:
            print(data['name'], data['email'])
#        else:
#            continue
"""
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
"""
# assignment to design dictionary structure of school institute
# write a program to update student info with phone
# write a program to get any person details with phone
# write a program to update teachers details with email

school = {
    'teacher': {
        'maths': [],
        'physics': [],
        'chemistry': [],
        'english': [],
        'Hindi': []
    },
    'Students': {
        '10th': [],
        '11th': [],
        '12th': [],

    },

    'Administrator': {
        'account': [],
        'registration': []

    }

}
