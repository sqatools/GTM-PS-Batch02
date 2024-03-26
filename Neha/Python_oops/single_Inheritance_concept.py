"""
Inheritance : When one class aquire the property of another class, then it is known as inheritance.
1. Single Inheritance : Class A -> Class B
2. Multi Level Inheritance : Class A -> Class B -> Class C
3. Multiple Inheritance : Class A -> Class B, Class C -> Class B

"""
#1. Single Inheritance : Class A -> Class B
class Father:

    def __init__(self, fname, fprofession, fproperty):
        self.fname = fname
        self.fprofession = fprofession
        self.fproperty = fproperty

    def show_father_name(self):
        print(f"Father name : {self.fname}")

    def show_father_profession(self):
        print(f"Father prosfession: {self.fprofession}")

    def show_father_property(self):
        print(f"Father property: {self.fproperty}")


class son(Father):

    def __init__(self, sname , sprofession , fname , fprofession , fproperty):
        self.sname = sname
        self.sprofession = sprofession
        super().__init__(fname, fprofession, fproperty)


    def show_son_details(self):
        print(f"Son_name: {self.sname}")
        print(f'Son_profession:{self.sprofession}')

    def family_details(self):
        self.show_father_name()
        self.show_father_profession()
        self.show_father_property()
        self.show_son_details()

if __name__ == '__main__':
    obj = son('Rahul','engineer','Dindayal','Farmer','Land')
    print(obj.family_details())
