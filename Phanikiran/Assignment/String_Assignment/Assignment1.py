#  ############### Program 1: Print g in first and h in for given string ###############.
print("-" * 20, "gello Good MorninH", "-" * 20)
# Method 1:
str1 = "Hello Good Morning"
print(str1[-1] + str1[1:17] + str1[0])

# Method 2:
val = str1[-1] + str1[1:17] + str1[0]
print(val)

print("-" * 20, "Pto rgamn", "-" * 20)
# ############### Program 2: Print following output for given string#######################################
str2 = "Python Programming"
# output2 = "Pto rgamn"

#  Method 1:
print(str2[0:17:2])

# Method 2:
val2 = str2[0:17:2]
print(val2)

# #################### Program 3 : Print "gninraeL nohtyP" in the output for given string ###############
print("-" * 20, "gninraeL nohtyP", "-" * 20)
str3 = "Learning Python"
# Method 1:
print(str3[-7:-16:-1] + str3[8] + str3[-1:-8:-1])

# Method 2:
val3 = str3[-7:-16:-1] + str3[8] + str3[-1:-8:-1]
print(val3)

# #################### Program 4 : Print "GGood Eveningg" in the output for given string ###############
print("-" * 20, "gninraeL nohtyP", "-" * 20)
str4 = "Good Evening"

# Method 1:
print(str4[0]+str4[0:13]+str4[11])

# Method 2:
print(str4[0]*2+str4[1:11]+str4[11]*2)
