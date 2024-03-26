from class_file1 import Admin
from class_file1 import filepath
import json
import os


class School(Admin):
    def __init__(self):
        super().__init__()
        print("School Class: ")

    def add_school(self, add_new=None):
        """
        :return:true if data added /updated sucessfully
        :param: school_name, school_address, school_phone, add_new
        """

        print("----- Enter School Details ------- ")
        school_name = str(input("Enter School Name: "))
        school_address = str(input("Enter School Address: "))
        school_phone = int(input("Enter School Phone: "))

        sc_dict = {
            'name': school_name,
            'address': school_address,
            'phone': school_phone,
            'admin_id': 1
        }

        with open(filepath, 'r') as file:
            file_data = file.read()
            if not file_data:
                data = {
                    'school':

                        [
                            sc_dict
                        ]
                }
            else:
                data = json.loads(file_data)
                if data.get('school') is not None:
                    school_list = data.get('school')
                    school_list.append(sc_dict)
                    data['school'] = school_list
                else:
                    data['school'] = [sc_dict]
            self.__write_school_data_file(data)
            self.show_school()

    def __write_school_data_file(self, school_dict):
        try:

            with open(filepath, 'w') as file:
                print(school_dict)
                json_data = json.dumps(school_dict)
                file.write(json_data)
        except Exception as e:
            print("Failed to write into file school_data.json: ", e)

    def show_school(self):
        print('_' * 20, 'School Details', '_' * 20)
        try:
            filesize = os.path.getsize(filepath)
            if filesize == 0:
                print("----- No School Found ------")
                add_new = int(input("Do you want to add new school 1/0? : "))
                if add_new == 1:
                    self.add_school(add_new=1)
                else:
                    print("----- Thank You -------")
            else:
                with open(filepath, 'r') as file:
                    file_data = file.read()
                    data = json.loads(file_data)
                    if data.get('school') is not None:
                        school_list = data.get('school')
                        print("-"*50, "School Details", "-"*50)
                        for val in school_list:
                            print("Name: ", val['name'])
                            print("Address: ", val['address'])
                            print("Phone: ", val['phone'])
                            print("_"*20)

        except FileNotFoundError as e:
            print("File not found", e)
