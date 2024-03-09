# Assignment to design dictionary structure of school institute
# write a program to update student info with phone
# write a program to get any person details with phone
# write a program to update teachers details with email

school = {
    'Teacher' : {
       'Maths': [
            {'name' : 'Usha' ,'email' :'usha@gmail.com','phone' : 785698769,'state' : 'Kerala' },
            {'name' : 'Rani' ,'email' : 'rani@gmail.com','phone' : 8755897 , 'state' : 'TamilNadu'}
       ],
        'Physics':[
                    {'name' : 'Uma' ,'email' :'uma@gmail.com','phone' : 658796986,'state' : 'Karnataka'},
                    {'name' : 'Magi' ,'email' :'magi@gmail.com','phone' : 234543245,'state' : 'Maharashtra'}
               ],
        'Chemistry':[],
        'English':[],
        'Biology':[]
    },
    'Students': {
        '10th': [
            {'roll no' : 45,'marks' : 98,'fav_sub': 'Maths' ,'lang': 'Hindi','phone': 7896543221},
            {'roll no' : 46,'marks' : 73,'fav_sub': 'Chemistry' ,'lang': 'Sanskrit','phone': 56985698689}
        ],
        '11th': [
            {'roll no' : 26,'marks' : 79,'fav_sub': 'Physics' ,'lang': 'Tamil','phone': 67785785875 },
            {'roll no' : 27,'marks' : 52,'fav_sub': 'Biology' ,'lang': 'French','phone' : 6908609867896 }
        ],
        '12th': [                                                                               ]
    },
    'Administrator': {
        'Accounts': [
            {'dept': 'cash' ,'file': 'office' ,'amount': 786987 ,'phone': 766098698},
            {'dept': 'sale' ,'file': 'admin' ,'amount': 225435 ,'phone': 76876896}
        ],
        'Registration':[
            {'reg_no': 898 ,'details': 'new admission','fee': 6900},
            {'reg_no': 435 ,'details': 'detention','fee': 2500}
        ]
    }
}

print(school)                   # prints entire school data

school['Students']['10th'][0]['lang'] = 'Chinese'
print(school)                  # Updated the lang from Hindi to Chinese
print(school['Administrator']['Registration'][0]['fee'])               #6900

print(school['Teacher']['English'])               #[]

# write a program to update student info with phone

school['Students']['11th'][1]['phone'] = 56565656

print(school['Students']['11th'][1])              # {'roll no': 27, 'marks': 52, 'fav_sub': 'Biology', 'lang': 'French', 'phone': 56565656}


for key,values in school.items():
    for data in values:
        print(data)

# Maths
# Physics
# Chemistry
# English
# Biology
# 10th
# 11th
# 12th
# Accounts
# Registration

# write a program to get any person details with phone

per_phone = 785698769
teachers = school.get('Teacher')
for key,values in teachers.items():
    for data in values:
        if data['phone'] == per_phone:
            print(data['name'],data['email'])                  # Usha usha@gmail.com
        else:
            continue


# write a program to update teachers details with email

school['Teacher']['Maths'][0]['email'] = 'usha3000@gmail.com'
print(school['Teacher']['Maths'][0])                #{'name': 'Usha', 'email': 'usha3000@gmail.com', 'phone': 785698769, 'state': 'Kerala'}

