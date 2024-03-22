"""
Inheritance : When one class aquire the property of another class, then it is known as inheritance.
1. Single Inheritance : Class A -> Class B
2. Multi Level Inheritance : Class A -> Class B -> Class C
3. Multiple Inheritance : Class A -> Class B, Class C -> Class B
"""


class Father:
    def __init__(self, fname, fbusiness, faddress):
        print("Inside Father Class: ")
        self.fname = fname
        self.fbusiness = fbusiness
        self.faddress = faddress

    def show_father_name(self):
        print("Father Name: ", self.fname)

    def show_father_business_name(self):
        print("Father Name: ", self.fbusiness)

    def show_father_address(self):
        print("Father Name: ", self.faddress)


class Son(Father):
    def __init__(self, fname, fbusiness, faddress, sname, sjob):
        super().__init__(fname, fbusiness, faddress)
        self.sname = sname
        self.sjob = sjob


# company
# tcs
# dept
# multi level

