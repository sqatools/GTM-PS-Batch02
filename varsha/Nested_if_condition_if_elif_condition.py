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

# write a python program for interview process
round1 = "pass"
round2 = "pass"
round3 = "pass"

if round1 == "pass":
    print("congrats first round is clear")
    if round2 == "pass":
        print("congrats 2nd round is also clear")
        if round3 == "pass":
            print("Congratulation you are placed")
        else:
            print("Failed in 3rd round better luck next time")
    else:
        print("sorry, you are failed in 2nd round")
else:
    print("sorry, you are failed in first round")

print("_" * 50)
# write code for exam result:
result = "hold"

if result == "pass":
    print("Congratulation you are cleared")
else:
    if result == "hold":
        print("Your result is on hold")
    else:
        print("You are failed in exam")

# write a python program to given number is divible by 3

num1 = 15
if num1 % 3 == 0:
    print("Number can divide by 3")
else:
    print("Can not divide by 3")

# check given number is odd or even
num_a = 40

if num_a % 2 == 0:
    print("Number is even")
else:
    print("The number is odd")

var1 = 55

print("pointer result :", var1 / 2)  # 27.5
print("whole number output :", var1 // 2)  # 27
print("Get remainder of any value :", var1 % 7)  # 6


# check given value is available in the list or not

list1 = [4, 6, 7, 8, 1]
num1 = 7

if num1 in list1:
    print("Value is available :",  num1)
else:
    print("Value is not available :", num1)


str1 = "Good Morning"

if "oo" in str1:
    print("oo combination is available")
else:
    print("Combination is not available")