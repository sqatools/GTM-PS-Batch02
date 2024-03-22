"""
# Inheritance:

# When one class acquiring the properties and behaviour of another class

Single inheritance: Class A ....> Class B                           One parent one child

Multi level inheritance : Class A ..> Class B ....> Class C         One Parent one child one grand child

Multiple Inheritance: Class A ...> Class B, Class C ...> Class B    More than one parent one child

Heirarchical inheritance:  Class A ....> Class B , A ...> C, A...>D  One parent multiple children

Hybrid inheritance:                                                 Combination of heirarchical and multi level inheritance

"""

# Single inheritance:

class father:
    def __init__(self,fname,fbusiness,fhouse):
        self.fname = fname
        self.fbusiness = fbusiness
        self.fhouse = fhouse

    def show_father_name(self):
        print(f"Father name:{self.fname}")

    def show_father_business(self):
        print(f"Fathe Business :{self.fbusiness}")

    def show_father_house(self):
        print(f"Father owns:{self.fhouse}")

    @staticmethod                                                         # Any type of methods can be used , class , instance and static
    def show_greeting():
        print("Welcome to OOPs")

class Son(father):
    def __init__(self, sname, sjob, fname, fbusiness, fhouse):
        self.sname = sname
        self.sjob = sjob
        super().__init__(fname, fbusiness, fhouse)                          # Add super class call

    def show_son_details(self):
        print(f"Son name:{self.sname}")
        print(f"Son job:{self.sjob}")

    def show_family_details(self):

        self.show_father_business()
        self.show_son_details()
        self.show_father_house()
        self.show_son_details()

if __name__ == '__main__':                                                                          # Here it is main module
    obj = Son("Mohit","Engineer","Mohan","Construction","4BHK")  # In Python inheritance, its  Python_Inheritance1

# Inside main module only, create object better
# obj.show_father_business()
# obj.show_son_details()
# obj.show_father_house()

obj.show_family_details()
obj.show_greeting()
print("Son name:",obj.sname)
obj.sname = "Rohan"
print("Son name:",obj.sname)

print("_"*50)
obj.show_family_details()

# This show the module name of the file
#print(__name__)                              #__main__

