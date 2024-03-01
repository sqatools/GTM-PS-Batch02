"""
Python program to find the electricity bill. According to the following conditions:
Up to 50 units rs 0.50/unit
Up to 100 units rs 0.75/unit
Up to 250 units rs 1.25/unit
above 250 rs 1.50/unit
an additional surcharge of 17% is added to the bill

"""
n=int(input("Enter no of units:"))

if n<=50:
    print(n*0.50)
elif n>50 and n<=100:
    print(n*0.75)
elif n>100 and n<=250:
    print(n*1.25)
elif n>250:
    finalbill=n*1.50+((n*1.50)*0.17)
    print(finalbill)

