# --------------------Python Elif Else--------------------------
"""
if condition1 :
    code
elif condition2:
    code
elif condition3:
    code
else:
    code
"""
# --------------------------------------------------
num1 = 800
num2 = 489
num3 = 564

if num1 > num2 and num1 > num3:
    print("num1 has the greater value ")
elif num2 > num1 and num2 > num3:
    print("Num2 holds the greater value")
elif num3 > num1 and num3 > num2:
    print("num3 has the greater value")
else:
    print("No variable holds the greater value")

print("*"*50)

if num1 > num2 and num1 > num3:
    print("num1 is greater")
print("*"*50)

# Provide grades to the student on the basis of the percentage of marks
marks = int(input("Enter your marks :"))
if marks >= 40 and marks <= 50:
    print("Student has got grade C")
elif marks > 50 and marks <= 60:
    print("The student has got grade B")
elif marks > 60 and marks <= 80:
    print("The student has gotten grade A")
elif marks > 80 and marks <= 100:
    print(" The student has got A+ grade")
elif marks > 100:
    print("Marks cannot be more than 100")
else:
        print("The student failed")









