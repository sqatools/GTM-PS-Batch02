from class_file1 import Admin
class Account(Admin):
    def __init__(self, acc_name, admin_name):
        super().__init__(admin_name)
        self.acc_name = acc_name


    def show_acc_name(self):
        print("Account name :", self.acc_name)
