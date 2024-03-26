"""
Inheritance : When one class aquire the property of another class, then it is known as inheritance.
2. Multi Level Inheritance : Class A -> Class B -> Class C

"""
#1. Multi Level Inheritance : Class A -> Class B -> Class C

class Grandfather:

    def __int__(self, gf_name, gf_profession, gf_property):
        self.gf_name = gf_name
        self.gf_profession = gf_profession
        self.gf_property = gf_property

    def show_grandfather_details(self):
        print(f"Grandfather name: {self.gf_name}")
        print(f"Grandfather profession: {self.gf_profession}")
        print(f"Grandfather_property: {self.gf_property}")


class Father(Grandfather):
    def __init__(self, f_name, f_profession, f_property, gf_name, gf_profession, gf_property):
        super().__init__(gf_name,gf_profession,gf_property)
        self.f_name = f_name
        self.f_profession = f_profession
        self.f_property = f_property

    def show_father_name(self):
        print(f"Father name : {self.f_name}")

    def show_father_profession(self):
        print(f"Father prosfession: {self.f_profession}")

    def show_father_property(self):
        print(f"Father property: {self.f_property}")


class son(Father):

    def __init__(self, s_name , s_profession , f_name , f_profession , f_property,gf_name , gf_profession, gf_property):
        super().__init__(f_name, f_profession, f_property, gf_name, gf_profession, gf_property)
        self.s_name = s_name
        self.s_profession = s_profession

    def show_son_details(self):
        print(f"Son_name: {self.s_name}")
        print(f'Son_profession:{self.s_profession}')

    def family_details(self):
        self.show_grandfather_details()
        self.show_father_name()
        self.show_father_profession()
        self.show_father_property()
        self.show_son_details()

if __name__ == '__main__':
    obj1 = son('Rahul','engineer','Dindayal','Farmer','Land','Motilal','Pilot','Flat')
    print(obj1.family_details())
