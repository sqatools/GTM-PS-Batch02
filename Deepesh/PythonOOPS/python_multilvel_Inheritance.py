"""
Inheritance : When one class aquire the property of another class, then it is known as inheritance.
1. Single Inheritance : Class A -> Class B
2. Multi Level Inheritance : Class A -> Class B -> Class C
3. Multiple Inheritance : Class A -> Class B, Class C -> Class B

"""

# multilevel inheritance  (A -> B -> C)
class GrandFather:
    def __init__(self, GFather_name, gf_property):
        self.gf_name = GFather_name
        self.gf_property = gf_property


    def show_gf_details(self):
        print(f"Grand father name: {self.gf_name} \n"
              f"Grand father property : {self.gf_property}")

class Father(GrandFather):
    def __init__(self, fname, fbusiness, fhouse, gf_name, gf_property):
        super().__init__(gf_name, gf_property)
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


class Son(Father):
    def __init__(self, sname, sjob, fname, fbusiness, fhouse, gf_name, gf_property):
        self.sname = sname
        self.sjob = sjob
        super().__init__(fname, fbusiness, fhouse, gf_name, gf_property)

    def show_son_details(self):
        print(f"Son name : {self.sname}")
        print(f"Son job : {self.sjob}")

    def show_family_details(self):
        self.show_gf_details()
        self.show_father_name()
        self.show_father_business()
        self.show_father_house()
        self.show_son_details()


if __name__ == '__main__':
    obj = Son("Mohit", "Engineer", "Mohan", "Construction", "4 BHK", "Hiralal", "100 Acr")

    # obj.show_father_business()
    # obj.show_son_details()
    # obj.show_father_house()
    obj.show_greeting()
    obj.show_family_details()
    print("_"*50)

    print("son name :", obj.sname)
    obj.sname = "Rohan"
    print("son name :", obj.sname)
    print("_"*50)
    obj.show_family_details()



#obj = Son("Mohit", "Engineer", "Mohan", "Construction", "4 BHK")

# obj.show_father_business()
# obj.show_son_details()
# obj.show_father_house()
#obj.show_family_details()
# this show the module name of the file
#print(__name__)  # __main__
#print("module of file1 :", obj.__module__)  # __main__
