"""
global variable
local variable
non local variable

"""

#global variable

varp=600

def function1():
    print("___function1___")
    varq = 700        # local variable , inside function
    print("global var varp:",varp)
    print("local varq:",varq)

def function2():
    print("__function2___")
    varq = 800        # local variable , inside function
    global varp
    varp = 900
    print("global var varp:",varp)
    print("local varq:",varq)

function1()
function2()