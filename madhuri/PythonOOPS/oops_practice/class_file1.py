import json


class Admin:
    def __init__(self, admin_name="Mohan"):
        self.admin_name = admin_name


    def show_admin_name(self):
        print("Admin name :", self.admin_name)

    def add_school(self):
        print("----- Enter School Details ------- ")
        school_name = input("Enter School Name: ")
        school_address = input("Enter School Address: ")
        school_phone = input("Enter School Phone: ")

        sc_dict = {
                        'name': school_name,
                        'address': school_address,
                        'phone': school_phone
                  }

        school_dict = {
            'school':
                [
                    sc_dict
                ]
        }

        with open('school_data.json','w') as file:
            json_data = json.dumps(school_dict)
            file.write(json_data)

        print("Data Saved Successfully.")
        print('_'*20, 'School Details', '_'*20)
        print(school_dict)