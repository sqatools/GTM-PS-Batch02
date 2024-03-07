# *args and **kwargs

# *args parameter
# args is default parameter name provided by python, which accepts multiple values at a time
# we can change args parameter name as per our requirements *args = *gtm

#def is the keyword which is definition

def print_square_val(var1,var2,*args,var3):                   # in place of args can write anything, * means multiple values
    print("*args:",args)
    print("var1:",var1)
    print("var2:",var2)

    for val in args:
        print(val**2,end=" ")
print_square_val(5,7,9,7654,987 ,var3=60)     # last value u should initialize bcoz *args will consume all values so explicitly
                                                              # initialise

#**kwargs : This parameter accepts values in the form of key value pair
#kwargs is the python suggested name , if we want to change the name we can change as per requirements
# **temp any word will work after **

def show_details(**kwargs):
    print("Value of kwargs:",kwargs)
    for key,value in kwargs.items():
        print(key,":",value)

print("__"*60)

show_details(name='John',email='john@:gmail.com',mobile=7654356778,city="Mumbai")
print("__"*60)
show_details(var1='John',var2=[4,6,8,2],var3=(5,7,22),var4={'a':123,'b':567})          # Key = value not colon , but O/P in form of dictionary :

def login(**kwargs):
    db_user = "Admin"
    db_password = "admin@123"

    if kwargs['username']== db_user and kwargs['password'] == db_password:
        print("Login successful")
    else:
        print("Access denied : Wrong username and password")

# Function Documentation #

def get_factorial(num:int):
    """
    This function will print the factorial of any given number
    :param num: This is the number to get factorials
    :return:
    """
    fact=1
    for i in range(num,0,-1):
        fact = fact*i
    print("Factorials:",fact)
get_factorial(6)                                      # get_factorial is a function, pass the parameters then will print

print(get_factorial.__doc__)                        # To get the documentation of any inbuilt method

str1 = "Hello"
print(str1.upper())
print(str1.upper.__doc__)

######################## Return values from the function ######################

def addition(num1,num2):
    return num1+num2
var1 = addition(50,60)
print("var1:",var1)

def multiply(num1,num2,num3):
   add_Val= addition(num1,num2)
   return  add_Val*num3

mul_val = multiply(4,5,6)          #4+5*6 = 54
print("Multiplication :",mul_val)

def show_values(num):
    for i in range(num):
        if i%3==0:
            print("Divide by 3:",i)
        elif i%7 ==0:
            return i                                  #return statement condition basis , it will stop with this
        elif i%11 ==0:
            print("Divide by 11:",i)

result = show_values(50)
print("Result:",result)                              #Result: 7

#var1: 110
# Multiplication : 54
# Divide by 3: 0
# Divide by 3: 3
# Divide by 3: 6
# Result: 7




