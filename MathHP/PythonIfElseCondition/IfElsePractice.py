"""
if condition
  code
else:
  code            # if you have space , then its intendation error

"""

# num1 = 100
# num2 = 200
#
# print(num1 == num2)
#
# if num1 == num2:                                     #either if / else will execute
#     print("Both variables have same value")         #If : then automatically intendation
# else:
#     print("Values are not same")                   # ctrl alt i for removing intendation error


"""
Logical operators:

> greatet than
> = greater than equal to
< less than
< = less than or equal to
!= not equal to
== equal to
"""

# var1 = input("Please enter val1: ")                        #input function takes input in the form of String only
# var2 = input("Please enter val2: ")                       #users input
#
# print(var1, type(var1), var2 , type(var2))
#
# if int(var1)> int(var2):
#     print("Variable 1 has greater value")
# else:
#     print("var2 has greater value")

    ####Check for float

    # var3 = float(input("Please enter val3: ") )        # input function takes input in the form of String only, convert data type as per requirement
    # var4 = float(input("Please enter val4: ") )        # users input
    #
    # print(var3, type(var3), var4, type(var4))
    #
    # if (var3) > (var4):
    #     print("Variable 3 has greater value")
    # else:
    #     print("var4 has greater value")

        ###String concatenation




        ###1 int 1 float

        # var5 = int(input("Please enter val5: "))  # input function takes input in the form of String only
        # var6 = float(input("Please enter val6: "))  # users input
        #
        # print(var5, type(var5), var6, type(var6))
        #
        # if (var5) > (var6):
        #     print("Variable 3 has greater value")
        # else:
        #     print("var4 has greater value")

            ##greater equal

var1 = 15
var2 = 14
if var1 >= var2:
       print("var1 has greater value:" ,var1)
else:
       print("var2 has greater value", var2)

####multi condition checking####

"""
     if cond1 and cond2:
"""
a=50
b=60
c=70

if c>a and c>b:
    print("c has the greatest value")
else:
    print("c does not have greatest value")

"""
         AND OR logical condition
         F and F = F
         T and F = F
         T and T = T
         F and T = F
         
         F or F = F
         T or F = T
         T or T = T
         F or T = T
         
"""
x= 500
y= 700
z= 500

if x==y or x==z:
    print("variables has equal value")
else:
    print("variables does not have equal value")                #####################################

