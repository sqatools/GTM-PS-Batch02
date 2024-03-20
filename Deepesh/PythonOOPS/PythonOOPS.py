"""
class : class is nothing but the blueprint of the object is being is created,
        where we defined all the methods, attributes and property of the object.

object : Object is the entity through which we can access the all the methods and attribute of the class.
constructor : constructor which initialize the memory of the object of class.
        1. Default constructor : default constructor which initialize the memory of the object
           and it calls which creating object of the class.

        2. Parameterize constructor: when we pass parameters to the constructor, then it is known as
          Parameterize constructor.

methods : When we create a function inside the class, then it becomes method.
        1. Instance method : any method that we write self as first parameter then it is known as
                             instance method.
        2. class method : when we defined method with decorator @class_method, then it is know as class
                          class method, class method only deals with class variables
        3. static method : static method is associated with class name, no need to create object of the class
                          while calling the static method.

variables : when we defined a variable inside the class, then it is known as class member
        1. Instance variable : The variable declare with self then it is known as instance variable.
        2. Class variable : The variable declare on the class level, it is known as class variable

self  : self is nothing but the object of the class where all required methods and attributes are created.
inner class
Inheritance
Polymorphism
Encapsulation
Abstraction
"""


# class
class ABC:

    # default constructor
    def __init__(self):
        print("Welcome OOPS concept")

    # method
    def greeting(self):
        print("Good Morning")


# create obj of the class
# obj = ABC()
# calling of the method through the object
# obj.greeting()


class XYZ:
    # class variable
    name = "the class name is XYZ"

    # Parametrize construction
    def __init__(self, num1, num2):
        print("Welcome to XYZ")
        self.n1 = num1  # instance variable
        self.n2 = num2  # instance variable
        num3 = 500  # local variable
        print("addition with num3 :", self.n1 + self.n2 + num3)
        print(self.name)

    # instance method
    def addition(self):
        print("addition :", self.n1 + self.n2)

    # instance method
    def multiplication(self):
        print("multiply :", self.n1 * self.n2)

    @classmethod  # class method
    def show_class_name(cls):
        print(cls.name)

    @staticmethod
    def factorials(num):
        fact = 1
        for i in range(num, 0, -1):
            fact = fact*i
        return fact


# obj = XYZ(40, 50)
# obj.addition()
# obj.multiplication()
# obj.show_class_name()

#print(obj.factorials(5))

#print(XYZ.factorials(7))  # 5040


class Car:
    def __init__(self, car_name, car_company):
        self.car_name = car_name
        self.car_company = car_company

    def show_car_name(self):
        print(f"The car name is : {self.car_name}")

    def show_car_company(self):
        print(f"The car company name is :{self.car_company}")

obj = Car("Harrier", "TATA")
obj.show_car_name()
Car.show_car_company(obj)
