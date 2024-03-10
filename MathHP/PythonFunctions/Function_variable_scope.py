"""
global variable :  the variable declare outside the function is known as global variable
                   and the scope of variable is across the modules.

local variable : The variable declare inside the function is known as local variable
                 and the scope of the variable is limited to function only.

non local variable : The variable we declare inside the outer function and the scope of the
                variable is limited all the inner function.

"""

#global variable outside all functions , inner and outer

varp=600

def function1():
    print("___function1___")
    varq = 700                        # local variable , inside function
    print("global var varp:",varp)
    print("local varq:",varq)

def function2():
    print("__function2___")
    varq = 800                        # local variable , inside function
    global varp
    varp = 900                        # update the global variable inside the function as local using global keyword
    print("global var varp:",varp)
    print("local varq:",varq)

function1()                           # calling the function , then only print will get executed
function2()
function1()                           # Once updated it will remain same until further updation


# non local variable , is outside the inner function and inside the outer function

varz = 500 # global variable
def outer_function():
    varx = 250 # non local variable

    def inner_function1():
        print("------inner function 1 -----")
        vary = 300 # local variable
        print("global varz :", varz)
        print("non local varx :", varx)
        print("local vary :", vary)

    def inner_function2():
        print("------inner function 2 -----")
        varw = 100 # local variable
        global varz
        nonlocal varx
        varx = 800
        varz = 1000
        print("global varz :", varz)
        print("non local varx :", varx)
        print("local varw :", varw)

    def inner_fun3():
        inner_function1()
        inner_function2()
        inner_function1()

    inner_fun3()                           # 1st execution , inside fun3 it calls fun1 ,fun2, fun1

# From fun1 to fun2 again to fun1 .
# fun1 will not have same values printed again
# Bcoz its changed in global and non local

print("#"*50)
outer_function()


def math_operations(var1, var2):
    def addition(var1, var2):
        return var1+var2
    def multiply(var1, var2):
        return var1*var2

    result1 = addition(var1, var2)
    result2 = multiply(var1, var2)
    print("addition")
    return result1, result2
    #return addition(var1, var2), multiply(var1, var2)

print("_"*50)
var1, var2 = math_operations(5, 4)
print("addition :", var1)
print("multiplication :", var2)

var3 = var1 + var2
print("var 3:", var3)

result = math_operations(15, 40)
print("result :", result)
