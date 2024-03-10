"""  PythonIf_elif_else_Practice.py

if condition1:
code
elif condition2:
code
elif condition3:
code
else:
code


Multiple elif conditions , whichever is first true will get executed

"""
############################################################
a=30
b=40
c=50

if a > b and a>c:                                            #Only if both are true , then true
    print("a is the greatest:" ,a)
elif b>a and b>c:
    print("b is the greatest:" ,b)                           #If F and T , then F
elif c> a and c> b:
    print("c is the greatest : " ,c)                         #c is the greatest :  50
else:
    print("No variable has the greatest value")


############################################################
a = 300
b = 400
c = 400

if a > b and a > c:  # Only if both are true , then true
        print("a is the greatest:", a)
elif b > a and b > c:
        print("b is the greatest:", b)  # If F and T , then F
elif c > a and c > b:
        print("c is the greatest : ", c)
else:
        print("No variable has the greatest value")            #No variable has the greatest value

#########################################################
a = 600
b = 500
c = 400
d = 300
e = 200

if a>b and a>c:
    print("a has greater value:")
if b > d and b > e:
        print("b has greater value:")

#########################################################

#Provide grade to  students on the basis of marks percentage

marks = float(input("Please enter marks:"))
if marks >= 40 and marks <= 50:                                         ###no specific range , int and float enough throughout
    print("Student got 3rd grade")
elif marks > 50 and marks <= 60:
    print("Student got 2nd grade")
elif marks > 60 and marks <= 80:
    print("Student got 1st grade")
elif marks > 80 and marks <= 100:
    print("Student got Excellent grade")
elif marks > 100:
    print("Marks can not be more than 100")
else:
    print("Student failed")

######################################################


