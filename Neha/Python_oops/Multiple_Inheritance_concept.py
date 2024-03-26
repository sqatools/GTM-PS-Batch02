"""
Inheritance : When one class aquire the property of another class, then it is known as inheritance.
3. Multiple Inheritance : Class A -> Class B, Class C -> Class B

"""
class Mother:

    def __int__(self, mname, mprofession):
        self.mname = mname
        self.mprofession = mprofession

    def show_mother_details(self):
        print(f'Mother name: {self.mname} \n'
        f'Mother profession: {self.mprofession}')
class Father:

    def __init__(self, fname , fprofession, f_property):
        self.fname = fname
        self.fprofession = fprofession
        self.f_property = f_property

    def show_father_name(self):
        print(f"Father name : {self.fname}")

    def show_father_profession(self):
        print(f"Father profession: {self.fprofession}")

    def show_father_property(self):
        print(f"Father property: {self.f_property}")


class son( Mother, Father):

    def __init__(self, sname , sprofession , mname, mprofession, fname ,fprofession , f_property):
        super().__init__(mname, mprofession)
        self.sname = sname
        self.sprofession = sprofession
        super().__init__(fname, fprofession, f_property)

    def show_son_details(self):
        print(f"Son_name: {self.sname}")
        print(f'Son_profession:{self.sprofession}')

    def family_details(self):
        self.show_father_name()
        self.show_father_profession()
        self.show_father_property()
        self.show_son_details()
        self.show_mother_details()

if __name__ == '__main__':
    obj = son('Rahul','engineer','Dindayal','Farmer','Land', 'Jyotsna','Housewife')
    print(obj.family_details())
