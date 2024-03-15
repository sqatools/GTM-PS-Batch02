import json

def read_json_data(filename):
    with open(filename, "r") as file:
        file_data = file.read()
        # convert the json string into dictionary
        data = json.loads(file_data)
        #print(data)
        return data


output = read_json_data("test_data.json")
print("name :", output["name"])
print("email :", output["email"])

def write_content_json_file(filename, content):
    with open(filename, "w") as file:
        # dumps method convert the dictionary data into json string
        json_data = json.dumps(content)
        file.write(json_data)

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

print(company['IT'])
# write_content_json_file("new_json_content.json", company)

#result = read_json_data("new_json_content.json")
#print(result["IT"])

