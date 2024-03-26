import json
import os


class Admin:
    def __init__(self, admin_name="Madhuri", admin_username="madhuri", admin_password='1234'):
        self.admin_name = admin_name
        self.username = admin_username
        self.password = admin_password

    def admin_details(self):
        print("username: ", self.username)
        print("password: ", self.password)


    def add_school(self, add_new=None):
        """
        :return:true if data added /updated sucessfully
        :param: school_name, school_address, school_phone, add_new
        """

        print("----- Enter School Details ------- ")
        try:
            school_name = str(input("Enter School Name: "))
            school_address = str(input("Enter School Address: "))
            school_phone = int(input("Enter School Phone: "))

            if add_new == 0:
                add_new = int(input("Do you Want to Replace/Add New School? 1/0: "))

            filepath = 'school_data.json'
            filesize = os.path.getsize(filepath)

            if filesize == 0:
                add_new = 1
            else:
                add_new = 0

            sc_dict = {
                'name': school_name,
                'address': school_address,
                'phone': school_phone
            }

            if add_new == 1:
                school_dict = {
                    'school':
                        [
                            sc_dict
                        ]
                }
                self.__write_school_data_file(school_dict)
            else:
                # get file data and append new
                filepath = 'school_data.json'
                filesize = os.path.getsize(filepath)
                print('filesize: ', filesize)
                with open(str(filepath), 'r') as file:
                    file_data = file.read()
                    data = json.loads(file_data)
                    data['school'].append(sc_dict)

                self.__write_school_data_file(data)

            print("Data Saved Successfully.")
            self.show_school_data()
            # print(json.dumps(data))

        except Exception as e:
            print("Input Error: ", e)



    def __write_school_data_file(self, school_dict):
        try:

            with open('school_data.json', 'w') as file:
                json_data = json.dumps(school_dict)
                file.write(json_data)
        except Exception as e:
            print("Failed to write into file school_data.json: ", e)

    def show_school_data(self):
        print('_' * 20, 'School Details', '_' * 20)
        filepath = 'school_data.json'

        try:
            filesize = os.path.getsize(filepath)

            if filesize == 0:
                print("----- No School Found ------")

                add_new = int(input("Do you want to add new school 1/0? : "))
                print(add_new)
                if add_new == 1:
                    self.add_school(add_new=1)
                    print("")
                else:
                    print("----- Thank You -------")
            else:
                with open('school_data.json', 'r') as file:
                    file_data = file.read()
                    data = json.loads(file_data)
                    print(data)

        except FileNotFoundError as e:
            print("File not found", e)

