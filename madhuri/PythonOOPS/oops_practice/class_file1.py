import json
import os


class Admin:
    def __init__(self, admin_name="Mohan"):
        self.admin_name = admin_name


    def show_admin_name(self):
        print("Admin name :", self.admin_name)

    def add_school(self, add_new = None):
        """
        :return:true if data added /updated sucessfully
        :param: school_name, school_address, school_phone, add_new
        """

        print("----- Enter School Details ------- ")
        school_name = str(input("Enter School Name: "))
        school_address = str(input("Enter School Address: "))
        school_phone = int(input("Enter School Phone: "))
        if add_new == 0:
            add_new = int(input("Do you Want to Add/Update School? 1/0: "))

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

    def __write_school_data_file(self, school_dict):
        with open('school_data.json', 'w') as file:
            json_data = json.dumps(school_dict)
            file.write(json_data)

    def show_school_data(self):
        print('_' * 20, 'School Details', '_' * 20)
        filepath = 'school_data.json'

        try:
            filesize = os.path.getsize(filepath)

            if filesize == 0:
                print("----- No School Found ------")
                add_new = int(input("Do you want to add school 1/0? : "))
                if add_new == 1:
                    self.add_school(add_new)
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

