"""
class : class is nothing but the blueprint of the object is being is created,
        where we defined all the methods, attributes and property of the object.

object : Object is the entity through which we can access the all the methods and attribute of the class.
constructor :  A constructor is a special method that is automatically invoked when an object of a class is created.
               constructor which initialize the memory of the object of class.
               They do not have a return type.
               Constructors are invoked at the time of object creation.
               They can be defined inside or outside the class declaration.


        1. Default constructor : classes can have constructors, which are special methods called __init__ methods.
         These constructors are used to initialize new objects created from the class.
        If you don't explicitly define a constructor in your class, Python provides a default constructor.

        2. Parameterize constructor: when we pass parameters to the constructor, then it is known as
          Parameterize constructor.

methods : When we create a function inside the class, then it becomes method.
        1. Instance method : any method that we write self as first parameter then it is known as
                             instance method.
        2. class method :  Class methods are associated with the class itself as first arguments,
                           when we defined method with decorator @class_method, then it is know as class
                          class method, class method only deals with class variables
        3. static method :A static method does not receive any special first argument.
                        It behaves like a regular function but is defined within the scope of a class.
                        static method is associated with class name, no need to create object of the class
                          while calling the static method.

        eg:
        Both class methods and static methods can be called on the class itself,
        without needing an instance of the class.

MyClass.class_method()  # Calling a class method
MyClass.static_method()  # Calling a static method
In summary, class methods are used to work with the class itself and can access class-level variables,
 while static methods are used for methods that don't depend on class or instance state.

variables : when we defined a variable inside the class, then it is known as class member
        1. Instance variable : The variable declare with self then it is known as instance variable.
        2. Class variable : The variable declare on the class level, it is known as class variable

self
inner class
Inheritance-->> overriding
Polymorphism
Encapsulation
Abstraction

__main__ is a special variable and a concept related to how Python scripts are executed.
When a Python script is run directly as the main program, the interpreter sets the special variable
__name__ to "__main__". This allows you to distinguish between when a script is run directly versus

 when it is imported as a module into another script.

"""

# class IRIS():
#
#     def __init__(self):
#         print("Welcome OOPS concept")
#
#     def company_entity(self):
#         print("Company entity created")
#
#     def Buisness_Partner(self):
#         print("BP entity created")
#
#     def Client_contact(self):
#         print("CC entity created")
#
#
#     #
#     # # method
#     # def greeting(self):
#     #     print("Good Morning")
#
#
# # create obj of the class
# obj = IRIS()
# # calling of the method through the object
# obj.Buisness_Partner()

class Prospect:

    job_details = "Details of the jobs"

    def __init__(self, X, Y ):
        self.jp = X
        self.cm = Y

    def job_ads(self):
        print("Print job ads:" , self.jp+self.cm )

    def jobposting(self):
        print("print job posting:", self.jp*self.cm )

    @classmethod
    def Class_method_name(cls):
        print(cls.job_details)


# obj = Prospect( 10 , 20)
obj = Prospect(20,30)
obj.job_ads()
obj.Class_method_name()
