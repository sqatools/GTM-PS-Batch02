# *args and **kwargs

# *args parameter:
# args is default parameter name provided by python, which accepts the multiple values at a time.
# we can change args parameter name as per our requirements.

def print_square_values(var1, var2, *args):
    print("*args:", args)
    print("var1 :", var1, var1**2)
    print("var2 :", var2, var2**2)
    for val in args:
        print(val**2, end=" ")

print_square_values(5, 7, 9, 10, 30, 40, 50, 60)

# **kwargs : This parameter accepts the values in the form of key value pair.
# kwargs is the python suggested name, if we want to change the name, we change as per requirements


def show_details(**kwargs):
    print("values of kwargs :", kwargs)
    for key, value in kwargs.items():
        print(key, ":", value)

# print("_"*50)
# show_details(name='John', email='john@gmail.com', mobile=654645564, city="Mumbai")
# print("_"*50)
# show_details(var1='John', var2=[4, 6, 8, 2], var3=(5, 7, 22), var4={'a': 123, 'b' : 567})


def login(**temp):
    db_user = "Admin"
    db_password = "admin@123"

    if temp['username'] == db_user and temp['password'] == db_password:
        print("Login Successful")
    else:
        print("Access denied, wrong username and password")

print("_"*50)
login(username='Admin', password='admin@123')
print("_"*50)
login(username='Admin1', password='Admin@123')


# function documentation

def get_factorial(num: int):
    """
    This function will print the factorials of any given number
    :param int num: this is the number to get factorials
    :return:
    """

    fact = 1
    for i in range(num, 0, -1):
        fact = fact*i

    print("factorials : ", fact)

print("_"*50)
get_factorial(6) # 720
#get_factorial('Hello')

print(get_factorial.__doc__)

str1="Hello"
print(str1.upper())
print(str1.upper.__doc__)


############## Return values from the function ###################

def addition(num1, num2):
    return num1+num2

print("_"*50)
var1 = addition(50, 60)
print("var1 :", var1)

def multiple(num1, num2, num3):
    add_val = addition(num1, num2)
    return add_val*num3

mul_val = multiple(4, 5, 6)
print("multiplication result :", mul_val)
# multiplication result : 54


def show_values(num):
    for i in range(num):
        if i%3 ==0:
            print("divide by 3:", i)
        elif i%7 == 0:
            return i
        elif i%11 ==0 :
            print("divide by 11 :", i)

result = show_values(50)
print("result :", result)
"""
divide by 3: 0
divide by 3: 3
divide by 3: 6
result : 7

"""