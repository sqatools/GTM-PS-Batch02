################## Assignment 11

str11 = "i got the offer letter"
print(str11.upper())                                      # Each letter converted to upper case

str12 = "WHEN cAN I jOIN"
print(str12.lower())                                     # All letters into lower case

str13 = "I AM IN CAPITAL LETTERS"
print(str13.isupper())                                   # Check whether all letters are in upper case
print(str11.isupper())

str14 = "i am in lower low case"
print(str14.islower())
print(str12.islower())                                  # Checks all letters are in lower cases

print(str14.swapcase())                                 # swaps lower to upper and vice versa
print(str13.swapcase())

print(str11.count("o"))
print(str12.count("C"))                                 # C is not present , only c
print(str13.count("I"))
print(str14.count("low"))

print(str14.title())                                    # Pascal case, first letter of each word is capital
print(str13.title())

str15 = "Is There Any Training Courses Offered"
print(str14.istitle())
print(str13.istitle())
print(str15.istitle())

str16 = "      I do have leading and trailing spaces     "
print(str16.strip())                                        # Removes the space from the front and back
print(str16.lstrip())
print(str16.rstrip())

print(str14.replace("low","high"))                                                              # low to high replaced
print(str12.replace("I","We"))                                                                 # Wherever I is there it changes to We
print(str15.replace("Training","Teaching").replace("Courses","Companies"))

print(str12.index("c"))                                       # Single alphabet or substring
print(str14.index("low"))                                    # only starting index for l
#print(str15.index("Ant"))                                   # ValueError: substring not found, Creates the breakpoint, stops the execution

print(str16.find("i"))                                      # first position of i
print(str15.find("Coup"))                                  # -1 , don't have this word so -1

str17 = "Definitely, I will join this company 'Sky' ; very soon"
print(str17.split(","))                                  # ['Definitely', " I will join this company 'Sky' ; very soon"]
print(str17.split("'"))                                 # ['Definitely, I will join this company ', 'Sky', ' ; very soon']
print(str17.split(" ; "))                              # ["Definitely, I will join this company 'Sky'", 'very soon']
print(str17.split("'")[1])                            # Sky