"""
if cond1:
    code
    if cond2:
    code
    if cond3:
    code
    else:
        code
    else:
        code
    else:
        code
"""
round1 = "PASS"
round2 = "pass"
round3 = "PASS"
if round1 == "PASS":
#    print("You are cleared first round")
    if round2 == "PASS":
            print("Contracts you are passed second round")
            if round3 == "pass":
                    print("Congratulations you have cleared the interview")
            else:
                print("Sorry you haven't cleared in 3rd round")
    else:
        print("You haven't cleared 2nd round")
else:
    print("You have cleared 1st round")

#---------------------------------
