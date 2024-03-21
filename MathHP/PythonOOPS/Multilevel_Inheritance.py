
class GrandFather:
    def __init__(self,gFather_Name,gFather_property):
        self.gFather_Name = gFather_Name
        self.gFather_property = gFather_property

    def show_gf_details(self):
        print(f"Grand father name:{self.gFather_Name} \n"
              f"Grand father property:{self.gFather_property} ")


class father(GrandFather):
    def __init__(self, fname, fbusiness, fhouse, gFather_Name, gFather_property):
        super().__init__(gFather_Name, gFather_property)
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
    def __init__(self, sname, sjob, fname, fbusiness, fhouse,gFather_Name,gFather_property):

        self.sname = sname
        self.sjob = sjob
        super().__init__(fname, fbusiness, fhouse,gFather_Name,gFather_property)                          # Add super class call

    def show_son_details(self):
        print(f"Son name:{self.sname}")
        print(f"Son job:{self.sjob}")

    def show_family_details(self):

        self.show_gf_details()
        self.show_father_business()
        self.show_son_details()
        self.show_father_house()
        self.show_son_details()

if __name__ == '__main__':                                                                          # Here it is main module
    obj = Son("Mohit","Engineer","Mohan","Construction","4BHK","Hiralal","100 Acr")
                                                                                  # In Python inheritance, its  Python_Inheritance1

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

