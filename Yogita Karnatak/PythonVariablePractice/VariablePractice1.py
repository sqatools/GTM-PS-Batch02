var1 = 10
print(id(var1))

var2 = 20
print(id(var2))

var3 = 10
print(id(var3))
# if multiple variable holding same value then their memory address will be same.

# Rules to define variable name
 # Variable name should not start with number
   #2var = 600 : Invalid
   #Var345 = 700 : Valid
   #V1a4r = 500 : Valid

 # There should not be space in variable name.
   # Var 1 = 900 : Invalid
   # Var_1 = 900 : Valid
   # abc_pqr = "Hello" : Valid

 # Python is case sensitive language, variable name with upper case & lower case will be different.

"""
Multiple comment  with triple quote.
name = "Rahul"
Name = "Kapil"
NAME = "Raj"
nAmE = "Gaurav"
print(name, Name, NAME, nAmE)
"""
# Assign multiple values to multiple variables
p, q, r = 100, 200, 300
print("Value of p:", p)
print("Value of q:", q)
print("Value of r:", r)

# Assign single value to multiple variables
x=y=z= 100
print("Value of x:", x)
print("Value of y:", y)
print("Value of z:", z)
