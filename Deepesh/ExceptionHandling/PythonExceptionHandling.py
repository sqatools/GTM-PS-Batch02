"""
try:
    num1 = 40
    num2 = '50'
    addition = num1 ++ num2
    print("addition :", addition)
except Exception as e:
    print("Can not add string and integer values")
    print(e)

print("multiplication  :", num1*num2)
"""

# Here will raise explicit exception to fail to further execution.
def explicit_raise_exception(num1, num2):
    try:
        # assert keyword use to compare variable values or any expected output
        assert num1 == num2
        print("both values are equal")
    except Exception as e:
        print("Both values are not equal")
        # explicitly raise exception to stop further execution.
        raise e


#explicit_raise_exception(40, 50)
#explicit_raise_exception(50, 50)


######### try - except - else #########

def try_except_else(num1, num2):
    try:
        output = num1//num2
        print("output :", output)
    except Exception as e:
        print("Division operation failed")
        print(e)
    else:
        mul = num1*num2
        print("multiplication :", mul)


#try_except_else(40, 0) # else part will not execute if there is a exception
#try_except_else(50, 2) # else part only execute the code if there is no exception in the code


###### try-except - else - finally ############
# else block : This block will only execute when there is no exception in the code
# finally block : This block will execute in all the condition where there exception or no exception.

def try_except_else_finally(num1, num2):
    try:
        addition = num1+num2
        print("addition :", addition)
        division = num1//num2
        print("division output :", division)
        assert num1 == num2, "both values are not equal"

    except Exception as e:
        print("Math operation failed")
        print(e)
        #raise e
    else:
        # this section only execute when there is no exception
        multiplication = num1*num2
        print("success multiplication output :", multiplication)

    finally:
        # This section execute all the time, not dependent on exception output.
        for i in range(1, 11):
            print(num1, "*", i, ":", num1*i)


# 1. When try and except block is successful then else and finally block will execute
# 2. When there is exception in try-except block, then exception code and finally will execute, else will not execute.

#try_except_else_finally(4, 4)
#try_except_else_finally(6, 5)

############# Handle multiple exception #############

def multiple_exceptions(num1, num2):
     try:
        addition = num1+num2
        print("addition :", addition)
        division = num1//num2
        print("division output :", division)
        assert num1 == num2, "both values are not equal"
     except AssertionError:
         print(f"Both values are not equal : {num1}, {num2}")
         raise
     except ZeroDivisionError:
         print("Can not divide the number by zero")
         raise
     except ValueError:
         print("both numbers data type should be integer")
         raise
     except TypeError:
         print("both numbers data type should be integer")
         raise


# multiple_exceptions(30, 40)  # AssertError
# AssertionError: both values are not equal

# multiple_exceptions(30, 'Hello')
# TypeError: unsupported operand type(s) for +: 'int' and '

# multiple_exceptions(50, 0)
# ZeroDivisionError: integer division or modulo by zero

##################### Nested Exception #########

def nested_exception(num1, num2):
    try:
        addition = num1 + num2
        print("addition of values :", addition)
        try:
            divide = num1//num2
            print("division of values :", divide)
        except Exception as e:
            print("Zero input is not allowed")
            print(e)

        finally:
            print("Multiplication of the number :", num1*num2)

    except Exception as e:
        print("Both the number should be be integer")
        print(e)

#
#nested_exception(50, 'Python')
"""
Both the number should be be integer
unsupported operand type(s) for +: 'int' and 'str'
"""


#nested_exception(50, 0)
"""
addition of values : 50
Zero input is not allowed
integer division or modulo by zero
"""

#nested_exception(50, 'Hello')

class CustomException(BaseException):
    def __init__(self):
        print("Hello Everyone, Welcome to Exception Handling")



def call_custom_exception(num1, num2):
    try:
        addition = num1+num2
        print("addition of the values :", addition)
    except Exception as e:
        CustomException()
        print("both the number should be integer")
        print(e)
        #CustomException()



call_custom_exception(50, 'Hello')
