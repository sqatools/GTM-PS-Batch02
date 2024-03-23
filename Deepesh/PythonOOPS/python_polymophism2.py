"""
Polymorphism : When user provide multiple task to one member then it known as polymorphism
Method Overriding : When parent class and child class has same method name, then child class method
                   will override the parent the method. this concept is known as method overriding.
Method Overloading : If class has two method with same name, but different behavior, then
                   it is known as method overloading.
Note : Python Does not support the method overloading, if we defined multiple method with same in
      a class, then latest defined method will priority.

Operator overloading : When one operator perform multiple task then it is know operator overloading.
e.g                   +, *,
"""

class Calculator:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def addition(self, num1, num2):
        print("Addition of two parameter :", num1+ num2)

    def addition(self, num1, num2, num3):
        print("Addition of three parameter :", num1 + num2 + num3)

# if __name__ == '__main__':
#     obj = Calculator(50, 60, 70)
#     obj.addition(5, 6)



#### Operator overloading ######

# plus operator overloading +
var1 = 40
var2 = 60
print(var1+var2)
print(var1.__add__(var2))

str1 = "Hello"
str2 = "Good Morning"
print(str1 + str2)
print(str1.__add__(str2))


# mul overloading *

n1 = 6
n2 = 5

print("multiply :", n1*n2)
print("multiply :", n1.__mul__(n2))
print(dir(int))

s1 = "Hello"
print(s1*2)
print(s1.__mul__(2))
print(dir(str))
