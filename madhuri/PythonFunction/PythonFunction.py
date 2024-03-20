def function1():
    print("Hello Good Morning")


# function1()

def addition(num1, num2):
    num3 = num1 + num2
    print("addition :", num3)


# passing data to parameters with "pass by value" concept
# addition(40, 50)

# passing data to parameters with "pass by reference"
x = 500
y = 700
# addition(x, y)

# list1= [5, 8, 9]
# sorted(list1)

p = 100
q = 500


# addition(num2=p, num1=q)


def multiplication(x, y):
    print("multiply :", x * y)


# function with default parameter values
"""
  - if parameter is holding default value, then it is optional parameters.
    it means while calling the function no need to provide value for default parameter.

  - default parameter value can be overwrite while calling the function.

  - non default parameter will always be followed default parameter
    it means the default parameter always comes at the end or right side.

  - All parameter of function could have default value.
    def fun1(vara=50, varb=60, varc=70):
        print("addition :", vara+varb+varc)

"""


def division(var1, var2=5):
    print("division :", var1 / var2)


# call function with default value
division(40)  # division : 8.0
# division(var2=4)  # division : 25.0
# TypeError: division() missing 1 required positional argument: 'var1'

# overwrite the default parameter value
division(40, 4)  # var1 = 40, var2=4


# All parameter of function could have default value.
def fun1(vara=50, varb=60, varc=70):
    print("addition fun1:", vara + varb + varc)


fun1()  # addition fun1: 180


#  non default parameter always come first and default parameter will come at the end.
def fun2(v1, v2, v3=60):
    # v1, v2 = non default parameter
    # v3 : default parameter
    print("multiplication :", v1 * v2 * v3)


# print("_"*40)
# fun2(4, 5)
print("pythonFunction :", __name__)
if __name__ == '__main__':
    print(__name__)
    print("_" * 40)
    fun2(4, 5)

"""
- by default each python file module name is __main__ module
- if we call same file from other location, the filename will become module name.

"""


