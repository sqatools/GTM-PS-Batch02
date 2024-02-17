# 12). Python program to describe the interview process.

round1 = input("Enter round 1 results :")
round2 = input("Enter round 2 results :")
if round1 == "passed":
    print("Congrats you have cleared first round!")
    if round2 == "passed":
        print("Congrats! You've cleared 2nd round, you are placed")
    else:
        print("You have not cleared the 2nd round. Try again later.")
else:
    print("Failed in 1st round. Try next time.")


"""
round1 = input("Enter round1 result:")
round2 = input("Enter round2 result:")

if round1 == "passed":
    print("Congrats your 1st round is clear")
    if round2 == "passed":
        print("Congrats 2nd round is clear, you are placed")
    else:
        print("Failed in 2nd round, please try next time")
else:
    print("Failed in 1st round, please try next time")

"""