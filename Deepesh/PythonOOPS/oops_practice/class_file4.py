from class_file3 import Teaching

class School(Teaching):
    def __init__(self, school_name, teach_name, acc_name, admin_name):
        super().__init__(teach_name, acc_name, admin_name)
        self.school_name = school_name


    def show_school_name(self):
        print("School name :", self.school_name)


if __name__ == '__main__':
    obj = School('Emrald', "Sharma Ji", "Bhatiya", "Gujjar")
    obj.show_acc_name()
    obj.show_admin_name()
    obj.show_school_name()
