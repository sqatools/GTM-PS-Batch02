def function1():                            # function, no space , can't start with numbers
    print("Hello Good Morning")

function1()                                # If u call only, the function will get executed

def addition(num1,num2):
    num3 = num1+num2
    print("Addition:",num3)

addition(5,3)                        # Addition: 8

# passing data to parameters with "pass by value" concept , directly provide value
addition(40,50)                     #Addition: 90

# Pass data to parameters with "pass by reference" , referring with the help of other variables, reference is the most preferable one
# No need to change in all 10 places just in one place , it can be modified

x=500
y=700
addition(x,y)                                             #Addition: 1200

# One function can be called any number of times with different inputs

#list1 = [5,8,9]
#sorted(list1)                                          # inbuilt function

p=100
q=500
addition(p,q)                                         #Addition: 600

def multiplication(x,y):
    print("Multiply :",x*y)

multiplication(4,3)                             #Multiply : 12

#function with default parameter values

"""
if parameter is holding default value, then it is optional parameters.
it means while calling the function no need to provide value for default parameter.

- default parameter value can be overwrite while calling the function

- non default parameter will always be followed by default parameter
- 1st is non default para that takes the value whatever we give
- default must be at the right side 2nd position
- It means the default para always comes at the end or right side

- Sometimes both para can be default 
- But if only one default , then end is the default
- 3 para means end must be default or all 3 can be default or 2nd and 3rd can be default

- All para of function could have default value
   def fun1(vara=50,varb=60,varc=70):
       print("Addition:",vara+varb+varc)

"""

def division(var1,var2=5):                             # var2 already holding default value
    print("Division:",var1/var2)

#call function with default value
division(40)                                          # Only one value so it goes to var1 , Division: 8.0

#division(var2=4)
division(100,2)                            # Division: 50.0 , if both values are given , that var2 = 5 will be overridden by 2

# All parameter of function could have default value

def fun1(vara=50,varb=60,varc=70):
    print("Addition fun1:",vara+varb+varc)          #Addition fun1: 180

fun1()

def f1(a,b,c=78):
    print("Mul:",a*b*c)

f1(2,3,4)                                 #Mul: 24 , val c=78 overridden by 4 , val c=78 is the default value

# Non default parameter always comes first and default parameter will come at the end

def fun2(v1,v2,v3=60):
    print("Multiply:",v1*v2*v3)                   # Multiply: 120 , takes values for 1st 2 only , 3rd is default

fun2(1,2)

# v1,v2 are non-default para
# v3 is default para

print("&&"*60)

                                                 #def f3(p=2,q=3,r):                            # Compilation issue
                                                 # Bcoz non default 1st and default last

print("Python Function:",__name__)              # Python Function: __main__
if __name__ == '__main__':
    print(__name__)                            # __main__
    print("_"*60)
    fun2(4,5)                         # Multiply: 1200

"""
- By default each python file module name is __main__module
- If we call 

"""




















