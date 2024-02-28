round1=input("Enter reslut round1:")
round2=input("Enter result of round2:")
if round1=="Pass":
    print("Round1 cleared and moved to round2")
    if round2=="Pass":
        print("Round1&2 cleared and got selected")
    else:
        print("Round2 is not cleared  please try next time")
else:
    print("Round1 is not cleared please try next time")




