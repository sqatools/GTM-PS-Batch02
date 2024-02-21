"""
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks
"""
m=int(input("enter marks:"))


if m<40:
    print("fail")
elif m>=40 and m<50:
    print("Grade C")
elif m >=50 and m<60:
    print("Grade B")
elif m>=60 and m<70:
    print("Grade A")
elif m>=70 and m<80:
    print("Grade A+")
elif m>=80 and m<90:
    print("Grade A++")
elif m>=90 and m<=100:
    print("Grade Excellent")
else:
    print("Invalid marks")

