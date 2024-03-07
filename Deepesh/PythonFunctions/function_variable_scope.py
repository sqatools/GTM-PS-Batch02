"""
global variable
local variable
non local variable
"""

# global variable
varp = 600

def function1():
    print("---function1 ----")
    var_q = 700 # local variable variable
    print("global var varp :", varp)
    print("local varq :", var_q)


def function2():
    print("---function2 ----")
    var_r = 800 # local variable variable
    global varp
    varp = 900
    print("global varp :", varp)
    print("local var_r :", var_r)

function1()
function2()
function1()