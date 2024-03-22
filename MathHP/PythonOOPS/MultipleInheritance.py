"""
Inheritance : When one class aquire the property of another class, then it is known as inheritance.
1. Single Inheritance : Class A -> Class B
2. Multi Level Inheritance : Class A -> Class B -> Class C
3. Multiple Inheritance : Class A -> Class B, Class C -> Class B

"""

# Multiple Inheritance (Mother -> Son,  Father -> Son)
class  Mother:
    def __init__(self, m_name, m_business):
        self.m_name = m_name
        self.m_business = m_business


    def show_mother_details(self):
        print(f"Mother name : {self.m_name} \n"
              f"Mother Business : {self.m_business}")

class Father:
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

# MRO : Method Resolution Order
class Son(Father, Mother):
    def __init__(self, sname, sjob, fname, fbusiness, fhouse, m_name, m_business):
        super().__init__(fname, fbusiness, fhouse)
        #super().__init__(m_name, m_business)
        self.sname = sname
        self.sjob = sjob
        self.mobj = Mother(m_name, m_business)

    def show_son_details(self):
        print(f"Son name : {self.sname}")
        print(f"Son job : {self.sjob}")

    def show_family_details(self):
        self.show_father_name()
        self.show_father_business()
        self.show_father_house()
        self.mobj.show_mother_details()
        self.show_son_details()



if __name__ == '__main__':
    obj = Son("Mohit", "Engineer", "Mohan", "Construction", "4 BHK", "Pooja", "Fashion")

    # obj.show_father_business()
    # obj.show_son_details()
    # obj.show_father_house()
    obj.show_greeting()
    obj.show_family_details()
    print("_"*50)

    # print("son name :", obj.sname)
    # obj.sname = "Rohan"
    # print("son name :", obj.sname)
    # print("_"*50)
    # obj.show_family_details()



#obj = Son("Mohit", "Engineer", "Mohan", "Construction", "4 BHK")

# obj.show_father_business()
# obj.show_son_details()
# obj.show_father_house()
#obj.show_family_details()
# this show the module name of the file
#print(__name__)  # __main__
#print("module of file1 :", obj.__module__)  # __main__


# Home Work
# Create a class structure with multi level inheritance
# class1 -> Engineer (project_manager, team_lead, total_resource)
# class2(class1) -> QA (QA_Head, QA_Lead, QA_Engineer)
# Class3(class2) -> company(comp_name, comp_address, comp_worth)
