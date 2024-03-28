#printing user defined error
# try:
#     num1 = 40
#     num2 = python
#     addition = num1 ++ num2
#     print("addition :", addition)
# except:
#      print("Can not add string and integer values")

#printing system defined error

# try:
#     num1 = 40
#     num2 = python
#     addition = num1 ++ num2
#     print("addition :", addition)
# except Exception as e:
#       print("Can not add string and integer values")
#       raise e

#Printing system defined error

# try:
#     num1 = 40
#     num2 = '50'
#     addition = num1 + + num2
#     print("addition :", addition)
# except Exception as e:
#     print("Can not add string and integer values")
#     print(e)
#
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
#explicit_raise_exception(40, 40)



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

try_except_else(num1=20,num2=0)


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

try_except_else_finally(4, 4)

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
#multiple_exceptions(30, 40)
#multiple_exceptions(30, 'Hello')
#multiple_exceptions(50, 0)

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

nested_exception(50, 'Python')




