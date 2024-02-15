marks= int(input("enter a marks"))
if marks<40:
    print("result fail")
else:
    if marks>40 and marks<50:
        print("grade c")
    else:
        if marks>50 and marks<60:
            print("grade B")
        else:
            if marks>60 and marks<70:
                print("grade A")
            else:
                if marks>70 and marks<80:
                    print("grade A+")
                else:
                    if marks>80 and marks<100:
                        print("grade A++")
                    else:
                        if marks>100:
                            print("invalid marks")