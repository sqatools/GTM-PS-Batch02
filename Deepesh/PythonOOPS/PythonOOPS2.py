"""
inner class : The class which declare inside the another class, then it is known as inner class.
Inheritance : When one class aquire the property of another class, then it is known as inheritance.

Polymorphism
Encapsulation
Abstraction
"""
class Sport:
    def __init__(self, sport_name, sport_head):
        self.sport_name = sport_name
        self.sport_head = sport_head

    def show_sport_name(self):
        print("Sport name :", self.sport_name)

    def show_sport_head(self):
        print("Sport head name :", self.sport_head)


class School:
    def __init__(self, school_name, admin_head, account_head, sp_name, sp_head):
        self.school_name = school_name
        self.admin_obj = self.Administrator(admin_head)
        self.account_obj = self.Account(account_head)
        self.sport_obj = Sport(sp_name, sp_head)

    def show_school_name(self):
        print("School name :", self.school_name)

    # create a inner class
    class Administrator:
        def __init__(self, depart_head_name):
            self.d_head = depart_head_name

        def show_admin_depart_head(self):
            print("Admin Department Head name :", self.d_head)


    class Account:
        def __init__(self, account_head):
            self.acc_head = account_head

        def show_account_head(self):
            print("Account Head Name :",self.acc_head)


if __name__ == "__main__":
    obj = School("Emrald Heights", "Mohan Sharma", "Udit Narayan", "Cricket", "Akshay Sir")
    obj.admin_obj.show_admin_depart_head()
    obj.account_obj.show_account_head()
    obj.show_school_name()
    obj.sport_obj.show_sport_name()
    obj.sport_obj.show_sport_head()

    print("_"*40)
    # child class object
    obj1 = School.Account("Ajay")
    obj1.show_account_head()

    print(__name__)  # __main__
