from class_file2 import Account

class Teaching(Account):
    def __init__(self, teach_name, acc_name, admin_name):
        super().__init__(acc_name, admin_name)
        self.teach_name = teach_name


    def show_teacher_name(self):
        print("Teacher name :", self.teach_name)
