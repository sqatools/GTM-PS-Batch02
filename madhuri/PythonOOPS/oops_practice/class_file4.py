import json

from class_file3 import Teacher

class Student(Teacher):
    def __init__(self, school_name, teach_name):
        super().__init__(teach_name)
        self.school_name = school_name

    def add_student(self):
        print("------ Add Student ------")
        student_name = str(input("Enter Name: "))
        student_class = int(input("Enter teaching class: (1-10th std e.g 1-10: )"))
        student_school_name = str(input("Enter School Name: (st john) : "))

        stud_dict = {
            'student_name': student_name,
            'student_class': student_class,
            'student_school_name': student_school_name
        }
        with open('school_data.json', 'r') as file:
            filedata = file.read()
            if not filedata:
                data = {
                    'student':
                        [
                            stud_dict
                        ]
                }

            else:
                data = json.loads(filedata)
                if data.get('student') is not None:
                    student_list = data.get('student')
                    student_list.append(stud_dict)
                    data['student'] = student_list
                else:
                    data['student'] = [stud_dict]
                self._School__write_school_data_file(data)
                self.show_students()
    def show_students(self):
        with open('school_data.json', 'r') as file:
            filedata = file.read()
            if not filedata:
                print("----- No Data Found -----")
            else:
                data = json.loads(filedata)
                teacher_list = data.get('student')
                if data.get('student') is not None:
                    print("-"*50, "Student Details", "-"*50)
                    for val in teacher_list:
                        print("Student name: ", val['student_name'])
                        print("Student Class: ", val['student_class'])
                        print("Student School Name: ", val['student_school_name'])
                        print("_" * 20)


if __name__ == '__main__':
    obj = Student('Emrald', "Sharma Ji")

    # Show Function
    # obj.admin_details()
    obj.show_school()
    obj.show_teachers()
    obj.show_students()

    # Add Function
    # obj.add_school()
    # obj.add_teacher()
    # obj.add_student()








