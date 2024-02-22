################### Assignment 10

# "WAP -Write a Python  Program using slicing concepts in Strings
# 1)Slicing
# 2)Slice from the start
# 3)Slice to the end
# 4)Negative Indexing
# 5)Concatenation of Strings"

# 1)Slicing

str1 = "Get ready for the interview"
print(str1[4:9])                             # last value excluded
print(str1[0:3])
print(str1[10:13])
print(str1[18:])                             # default last value till end of the string

# 2)Slice from the start

str2 = "All the very best"
print(str2[ :3])
print(str2[ :12])
print(str2[ :17])
print(str2[ :-5])                           # All the very

# 3)Slice to the end

str3 = "You will win"
print(str3[3:])                             #  will win , from space , default end is until end of the string
print(str3[6:])
print(str3[-7:])
print(str3[-9:])                           # till end

# 4)Negative Indexing

str4 = "You are selected"
print((str4[-8:]))
print((str4[-12:-9]))
print((str4[ :16:3]))                      # default initial is 0, default final is end of string,3rd place 3 difference skip rests

# 5)Concatenation of Strings

print(str1+" " +str2+" "+str3+" "+str4)
print(str1[4::2]+"  "+str2[ :12]+"  "+str3[-3::-1]+""+"Hello")         # right to left as -1 is negative indexing difference
