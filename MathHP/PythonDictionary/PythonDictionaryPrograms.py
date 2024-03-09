company = {
    'IT': [
        {'name': 'sanjay', 'email': 'sanjay@gmail.com', 'phone': 5654645, 'address': 'mumbai'},
        {'name': 'Neha', 'email': 'neha@gmail.com', 'phone': 434343, 'address': 'Pune'},
        {'name': 'Saumya', 'email': 'Saumya@gmail.com', 'phone': 33333232, 'address': 'Bangalore'},
    ],
    'HR': [
        {'name': 'priya', 'email': 'priya@gmail.com', 'phone': 8767657, 'address': 'Chennai'},
        {'name': 'swamini', 'email': 'swamini@gmail.com', 'phone': 98978998, 'address': 'Indore'},
        {'name': 'Bharath', 'email': 'Bharath@gmail.com', 'phone': 2332423432, 'address': 'Bhopal'},
    ]
}                                            # In company , IT and HR are keys values { } completely

print(company['HR'][2]['email'])            #Bharath@gmail.com

print(company['IT'][1]['email'])           #neha@gmail.com

print(company['IT'][2]['email'])          #Saumya@gmail.com

# update email id of Saumya
company['IT'][2]['email'] = "Saumya2024@gmail.com"

print(company['IT'][2]['email'])

print(company)

# Add new key value to the dictionary

company['IT'][2]['country'] = "India"

dict1 = {'a':[4,5,6],'b':[7,8,9]}          # key and value
print(dict1.items())                       # dict_items([('a', [4, 5, 6]), ('b', [7, 8, 9])]) key,value

print("#"*60)

# Get all keys and values names of the company

for key, val in company.items():
    print(key,val)                        # Printing Keys IT and HR and all its values as well

# Get names of all employees

for key,values in company.items():        # dict
    for data in values:                  # values holding the list
        #print(data)                    # Printing all values only no Keys
        print(data['name'])            # sanjay Neha Saumya priya swamini Bharath

# Get specified person details , person name

per_name = 'Bharath'
for key,values in company.items():
    for data in values:
        if data['name'] == per_name:
            print(data)                      #{'name': 'Bharath', 'email': 'Bharath@gmail.com', 'phone': 2332423432, 'address': 'Bhopal'}
        else:
            continue


# Get specified person details with mobile number

per_phone = 98978998
for key,values in company.items():
    for data in values:
        if data['phone'] == per_phone:
            print(data['name'],data['email'])      #swamini swamini@gmail.com
        else:
            continue

print("#"*60)


######################################

# add/update person information on the basis of mobile number
# Back End code, Real time application

per_phone = int(input("Please enter mobile number:"))                                         # Getting inputs from the user
new_data = input("Please enter new details  with this format: salary,767876576 :")          # Getting inputs from the user like myBonus, 69868960
new_key = new_data.split(",")[0]
new_value = new_data.split(",")[1]
print("new_key:",new_key)
print("new_value:",new_value)

#new_key:  myBonus
#new_value:  69868960

for k,v in company.items():
    for data in v:
        if data['phone'] == per_phone:
            data[new_key] = new_value
        else:
            continue

print("Company:",company)            # {'name': 'Neha', 'email': 'neha@gmail.com', 'phone': 434343, 'address': 'Pune', 'city': 'chennai'}

# Get details

per_phone = 8767657
for key,values in company.items():
    for data in values:
        if data['phone'] == per_phone:  # {'name': 'priya', 'email': 'priya@gmail.com', 'phone': 8767657, 'address': 'Chennai'}
            print(data)
        else:
            continue


# Refer  Homework 3
# Assignment to design dictionary structure of school institute
# write a program to update student info with phone
# write a program to get any person details with phone
# write a program to update teachers details with email








