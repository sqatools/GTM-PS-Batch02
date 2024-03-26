from class_file2 import School
import json
import os

class Teacher(School):
    def __init__(self, teach_name):
        super().__init__()
        self.teach_name = teach_name

    def show_teacher_name(self):
        print("Teacher name :", self.teach_name)

    def add_teacher(self):
        print("----- Add New Teacher ------ ")
        teacher_name = str(input("Enter teacher Name: "))
        teacher_class = int(input("Enter teaching class: (1-10th std e.g 1-10: )"))
        teacher_subject = str(input("Enter teaching subject: (e.g math/english): "))
        school_name = str(input("Enter School Name: (st john) : "))
        add_teacher = int(input("Do you want to add/update teacher details? (1/0): "))
        # search school_id by school_name
        admin_id = 1
        school_id = 1
        add_teacher = 1

        if add_teacher == 1:
            teach_dict = {
                'teacher_name': teacher_name,
                'teacher_class': teacher_class,
                'teacher_subject': teacher_subject,
                'school_name': school_name,
                'admin_id': 1,
                'school_id': 1
            }

            #check school_data.json contains any data
            with open("school_data.json", 'r') as file:
                file_data = file.read()
                if not file_data:
                    data = {
                        'teacher':
                            [
                                teach_dict
                            ]
                    }
                else:
                    data = json.loads(file_data)
                    if data.get('teacher') is not None:
                        # print('key exist')
                        teacher_list = data.get('teacher')
                        teacher_list.append(teach_dict)
                        data['teacher'] = teacher_list
                    else:
                        data['teacher'] = [teach_dict]

                self._School__write_school_data_file(data)
                self.show_teachers()
        else:
            print("Update Teacher")

    def show_teachers(self):
        with open('school_data.json', 'r') as file:
            filedata = file.read()
            if not filedata:
                print("----- No Data Found -----")
            else:
                data = json.loads(filedata)
                teacher_list = data.get('teacher')
                if data.get('teacher') is not None:
                    print("-"*50, "Teacher Details", "-"*50)
                    for val in teacher_list:
                        print("Teacher name: ", val['teacher_name'])
                        print("Teacher Class: ", val['teacher_class'])
                        print("Teacher Subject: ", val['teacher_subject'])
                        print("Teacher School Name: ", val['school_name'])
                        print("_" * 20)





