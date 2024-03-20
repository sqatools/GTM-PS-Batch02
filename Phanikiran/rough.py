def show_details(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, ":", value)


show_details(name="pk", email="pk@gmail.com", contact=92343)

"""
def print_square_values(*args):
    # print(args)

    for val in args:
       #print(args, end=" ")


#print_square_values(3, 5, 4, )

"""


# **kwargs

def show_details(**kwargs):
    print("value of kwargs", kwargs)

    for key, value in kwargs.items():
        print(key, value)


show_details(var1='name', var2=(2, 6, 2), var3=[3, 6, 7], var4={'name': 'phani'})


# function documentation
def get_factorial(num: int):
    """
    This function will print the factorial of any given number
    :param num: this is the number to get factorials
    :return:
    """
    fact = 1
    for i in range(num, 0, -1):
        fact = fact * i
    print("Factorial of a given number", fact)


get_factorial(5)

# __doc__ This inbuild magic method is used to display the documentation of the function
print(get_factorial.__doc__)
str1 = "hi"
print(str1.upper().__doc__)

print("*" * 100)


def addition(x, y):
    return x + y


z = addition(10, 20)
print(z)


def multiplication(x, y, z):
    result = addition(x, y)
    return result* z


value = multiplication(2, 3, 4)
print(value)
