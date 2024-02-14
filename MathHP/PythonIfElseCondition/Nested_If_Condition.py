"""
 if cond1:
   code
if cond2:
    code
if code3:
    code
else:
   code
else:
  code
else:
  code
"""

###WAP for interview process
round1 = "pass"
round2 = "fail"
round3 = "pass"

if round1 == "pass":
    print("Congrats first round is cleared")                        ##if else present inside if else
    if round2 == "pass":
        print("Congrats second round is cleared")
        if round3 == "pass":
            print("Congratulations you are placed")
        else:
            print("Failed in 3rd round .Better luck next time")
    else:
        print("Sorry failed in second round")
else:
    print("Sorry failed in first round")

#######################################

result = "fail"                                                     #assignment = operator

if result == "pass":                                                # == comparison operator equal to , relational operator
     print("Congratulations")
else:
    if result == "hold":
        print("Your result is on hold")
    else:                                                          # inside else also we can give if else
        print("You failed")

########################################

#WAP to check given number is divisible by 3

num1 = 15
if num1%3 == 0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")

#########################################

#Check giiven number is odd or even

a = 40

if a%2 == 0:
    print("Number is even")
else:
    print("Number is odd")

####################################################

var1 = 55

print("Whole number" ,var1//2)                         ####   //  int
print("pointer number" ,var1/2)                        ###   /   decimal
print("Remainder " ,var1%2)                            ## modulo operator

####################################################
#Check given value is avilable in the list or not

list1 = [4,6,7,8,1]
num1 = 5

if num1 in list1:
    print("Value is available : ", num1)
else:
    print("Value not available: " , num1)

######################################################

str1 = "Good Morning"

if "oo" in str1:
    print("oo combination is available")
else:
    print("oo combination is not available")

#######################################################
