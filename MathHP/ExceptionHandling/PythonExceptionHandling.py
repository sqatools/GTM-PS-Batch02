try:
    num1=40
    num2='Hello'
    addition = num1+num2
    print("Addition:",addition)        # TypeError: unsupported operand type(s) for +: 'int' and 'str'
except Exception as e:
    print("Cannot add string and integer values")
    print(e)                         # unsupported operand type(s) for +: 'int' and 'str'  , system generated exception

try:
    num1=40
    num2=50
    addition = num1+num2                             # Addition: 90
                                                     # Multiplication: 2000
    multiplication = num1*num2
    print("Addition:",addition)
except :
    print("Cannot add string and integer values")


print("Multiplication:",multiplication)

# If exception occurs , then except will execute
# If no exception, then try will get executed

# Here will raise the explicit exception to fail to further execution

def explicit_raise_exception(num1,num2):
    try:
        assert num1 == num2                                    # assert keyword used to compare expected = actual result
    except Exception as e:
        print("Both values are not equal")
        raise e                                              # raise the exception and points out the line to stop further execution

#explicit_raise_exception(40,50)                            # AssertionError
explicit_raise_exception(40,40)

# try - except - else

def try_except_else(num1,num2):
    try:
        output = num1//num2
        print("Output",output)                                    # Output 25
    except Exception as a:
        print("Division operation failed")
        print(a)
    else:
        mul = num1*num2
        print("Multiplication:",mul)                            # Multiplication: 100

#try_except_else(40,0)                  #TypeError: try_except_else() takes 1 positional argument but 2 were given
try_except_else(50,2)                  #TypeError: try_except_else() takes 1 positional argument but 2 were given

########### try_except_else_finally ####################

# else block : This block will only execute when there is no exception in the code
# finally block : This block will execute in all conditions

def try_except_else_finally(num1,num2):
    try:
        addition = num1+num2
        print("Addition:",addition)
        division = num1//num2
        print("Division output:",division)
        assert  num1==num2

    except Exception as e:
        print("Math operation failed")
       # print(e)
        raise e                                             # AssertionError
    else:                                                  # This section only execute when there is no exception
        multiplication = num1*num2
        print("Success output:",multiplication)
    finally:
        for i in range(1,11):
            print(num1,"*" ,i,":",num1*i)

# 1) When try and except block is successful then else and finally block will execute
# 2) when there is exception in try_except block, then exception code and finally will execute, else will not execute

try_except_else_finally(4,4)
#try_except_else_finally(4,5)

# except and else like if else , any one must execute
# try must be followed by one or more except blocks

################# Handle multiple exceptions #################

def multiple_exception(num1,num2):
 try:
    addition = num1 + num2
    print("Addition:", addition)
    division = num1 // num2
    print("Division output:", division)
    assert num1 == num2,"both values are not equal"

 except AssertionError:
    print(f"Both values are not equal: {num1},{num2}")
    # print(e)
    raise
 except ZeroDivisionError:
     print("Can not divide the number by zero")
     raise
 except ValueError:
     print("Both numbers data type should be integer")
     raise
 except TypeError:
     print("Both numbers data type should be integer")
     raise

#multiple_exception(30,40)              # Assert Error
multiple_exception(30,30)
#multiple_exception(30,'hello')             # TypeError
#multiple_exception(50,0)                       #ZeroDivisionError

################### Nested Exception #################

def nested_exception(num1,num2):
    try:
        addition = num1+num2
        print("Addition of values",addition)
        try:
            divide = num1//num2
            print("division of values:",divide)
        except Exception as e:
            print("zero input is not allowed")
            print(e)
        finally:
            print("Multiplication :" ,num1*num2)

    except Exception as e:
        print("Both the number should be an integer")

nested_exception(50,0)
#nested_exception(50,'Hello')

# Any one of try or except will get executed not both

class CustomException(BaseException):
    def __init__(self):
        print("Hello everyone welcome to Exception handling")

def call_custom_exception(num1,num2):
    try:
        addition = num1+num2
        print("Addition:",addition)
    except Exception as e:
        CustomException()                                                 # Calling class CustomException
        print("Both the number should be an integer")
        print(e)

call_custom_exception(50,'hello')                         # TypeError: unsupported operand type(s) for +: 'int' and 'str'


