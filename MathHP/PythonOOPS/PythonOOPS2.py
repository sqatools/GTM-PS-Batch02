"""
 Inner Class:
     Class declared inside another class   is the inner class



Polymorphism
Encapsulation
Abstraction


"""
class Sport:                                                         # separate class outside the class
    def __init__(self,sport_name,sport_head):
        self.sport_name = sport_name
        self.sport_head = sport_head

    def show_sport_name(self):
        print("Sport name:",self.sport_name)

    def show_sport_head(self):
        print("sport head name:",self.sport_head)

class School:
    def __init__(self,school_name,admin_head,account_head,sp_name,sp_head):
        self.school_name = school_name                             # this.GV = LV
        self.admin_obj = self.Administrator(admin_head)           # creating obj for inner classes, accessing with Administrator class
        self.account_obj= self.Account(account_head)             # accessing with Account class
        self.sport_obj = Sport(sp_name,sp_head)


    def show_school_name(self):
        print("School name:",self.school_name)

    class Administrator:                                          # Create an inner class
        def __init__(self,depart_head_name):
            self.d_head = depart_head_name                       # LV same like parameter inside , GV can be different

        def show_admin_depart_head(self):
            print("Admin Dept head name :" ,self.d_head)

    class Account:                                                            # Create an inner class
        def __init__(self, account_head):
            self.acc_head = account_head                                             # LV same like parameter inside , GV can be different

        def show_account_head(self):
            print("accounthead name :", self.acc_head)

if __name__ == "__main__":                                             # default python file is main
    obj = School("Emrald Heights","Mohan Sharma","Udit Narayan","Cricket","Akshay Sir")
    obj.admin_obj.show_admin_depart_head()
    obj.account_obj.show_account_head()                             # AttributeError: 'Administrator' object has no attribute 'show_account_head'
    obj.show_school_name()
    obj.sport_obj.show_sport_name()
    obj.sport_obj.show_sport_head()

    print("__"*50)
    obj1 = School.Account("Ajay")                             # child class object
    obj1.show_account_head()

    print(__name__)                                         # __main__

