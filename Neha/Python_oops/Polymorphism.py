"""
Polymorphism : When user provide multiple task to one member then it known as polymorphism
Method Overriding : When parent class and child class has same method name, then child class method
                   will override the parent the method. this concept is known as method overriding.
"""

class Father:

    def __init__(self, fname, fprofession):
        self.fname = fname
        self.fprofession = fprofession

    def show_father_details(self):
        print(f"father Name : {self.fname}")
        print(f"father profession : {self.fprofession}")

    def show_total_worth(self):
        print("Method belongs to father class")
        print("Business :", self.fprofession)


class Son(Father):

    def __init__(self, sname, sprofession, fname, fproffesion):
        self.sname = sname
        self.sprofeesion = sprofession
        super().__init__(fname, fproffesion)

    def show_son_details(self):
        print(f"Son Name : {self.sname}")
        print(f"Son profession : {self.sprofeesion}")

    def show_family_details(self):
        self.show_son_details()
        self.show_father_details()

    def show_total_worth(self):
        print("Method belongs to Son class")
        print("Business :", self.fprofession)
        print("Own profession:" ,self.sprofeesion)


if __name__ == "__main__":
    obj = Son ("Sanjeev", 'IT engineer','Prasad','Defence')
    obj.show_total_worth()

print("_" * 50)

# """
# Method Overloading : If class has two method with same name, but different behavior, then
#                    it is known as method overloading.
# Note : Python Does not support the method overloading, if we defined multiple method with same in
#       a class, then latest defined method will priority.
#
# """
#
class Calculator:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def addition(self, num1, num2):
        print("Addition of two parameter :", num1+ num2)

    def addition(self, num1, num2, num3):
        print("Addition of three parameter :", num1 + num2 + num3)

if __name__ == '__main__':
    obj = Calculator(50, 60, 70)
    obj.addition(5, 6)

print("_" * 50)
"""
Operator overloading : When one operator perform multiple task then it is know operator overloading.
e.g                   +, *,
"""

#### Operator overloading ######

# plus operator overloading +
# var1 = 40
# var2 = 60
# print(var1+var2)
# print(var1.__add__(var2))

# mul overloading
n1 = 6
n2 = 5

print("multiply :", n1*n2)
print("multiply :", n1.__mul__(n2))
print(dir(int))