"""                    COAPIE
Class:
Class is a blueprint of any object is being created where we define all the methods, attributes and property of the object.
Class is a logical entity

Object:
Object is the physical entity through which we can access all the methods and attribute of the class.
Is the instance of the class

Constructor:
Constructor which initialize the memory of the objectof class
       1) Default Constructor :
          default constructor which initialize the memory of the object and it calls when creating object of the class
       2) parameterized Constructor :
          When we pass parameters to the constructor, then it is known as parametrized constructor

Whenever object is created, constructor is invoked
Same name as the classname


Methods:
When we create a function inside the class, then it become method
     1) instance method :
         Any method that we write self as first para , then it is instance
     2) class method:
          When we define method with decorator @class_method, it is known as class method
          class method deals only with class variables

     3) static method:

Variables:
When we define a variable inside the class, then it is known as class member
   1) Instance variable:
       The variable declare with self then it is known as instance variable
   2) Class variable:
        The variable declared on the class level, is known as class variable


Self:

Inner Class


Inheritance
Polymorphism
Encapsulation
Abstraction

"""

class ABC:                                   # class , no special characters allowed, uppercase ,lowercase, _ allowed

    def __init__(self):                      # Default constructor
        print("Welcome to OOPS Concept")
    def greeting(self):                     # method
        print("Good Morning")

obj = ABC()                                # Create object of the class, ref var is obj ,# Welcome to OOPS Concept
#obj.greeting()

class XYZ:

    name = "the class name is XYZ"                 # class variable, global
    def __init__(self,num1,num2):                # Only one init in a class, this is para constructor
        self.n1 = num1                          # instance variable , across the class in all methods
        self.n2 = num2                         # instance variable
        num3= 500
        print("addition with num3:",self.n1+self.n2+num3)


    def addition(self):                     # instance method
        print("addition:",self.n1+self.n2)
        print(self.name)                    # can call GV using self

    def multiplication(self):
        print("multiply:",self.n1*self.n2)
        print(self.name)

    @classmethod                             # class method
    def show_class_name(cls):
        print(cls.name)                      # can access only class variable, can call GV with only cls

obj = XYZ(40,50)                       # addition with num3: 590 , init is invoked , para constructor
obj.addition()                                     # addition: 90
obj.multiplication()
obj.show_class_name()
