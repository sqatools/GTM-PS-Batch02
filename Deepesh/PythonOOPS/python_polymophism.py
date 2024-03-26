"""
Polymorphism : When user provide multiple task to one member then it known as polymorphism
Method Overriding : When parent class and child class has same method name, then child class method
                   will override the parent the method. this concept is known as method overriding.
Method Overloading :
"""

# single inheritance
class father:
    def __init__(self, fname, fbusiness, fhouse):
        self.fname = fname
        self.fbusiness = fbusiness
        self.fhouse = fhouse

    def show_father_name(self):
        print(f"Father name : {self.fname}")

    def show_father_business(self):
        print(f"Father Business : {self.fbusiness}")

    def show_father_house(self):
        print(f"Father owns : {self.fhouse}")


    @staticmethod
    def show_greeting():
        print("Welcome to the OOPS Concept")

    def show_total_worth(self):
        print("Method belongs to father class")
        print("Business :", self.fbusiness)
        print("House :", self.fhouse)


class Son(father):
    def __init__(self, sname, sjob, fname, fbusiness, fhouse):
        self.sname = sname
        self.sjob = sjob
        super().__init__(fname, fbusiness, fhouse)

    def show_son_details(self):
        print(f"Son name : {self.sname}")
        print(f"Son job : {self.sjob}")

    def show_family_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_house()
        self.show_son_details()

    def show_total_worth(self):
        print("This method belongs to Son class")
        print("Business :", self.fbusiness)
        print("House :", self.fhouse)
        print("Son Job :", self.sjob)


if __name__ == '__main__':
    obj = Son("Mohit", "Engineer", "Mohan", "Construction", "4 BHK")
    obj.show_total_worth()
