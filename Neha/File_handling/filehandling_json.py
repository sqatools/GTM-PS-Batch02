import json


def write_content(filename,content):
    with open(filename,"w") as file:
        #convert the json string into dictionary
        data = json.dumps(content)
        file.write(data)

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


write_content("Test_2_json_concept",school)
