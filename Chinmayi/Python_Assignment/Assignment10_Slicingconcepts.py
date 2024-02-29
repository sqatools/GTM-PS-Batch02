# Writ a python program using a slicing concepts in Strings.
# 1)Slicing
# 2)Slice from the start
# 3)Slice to the end
# 4)Negative Indexing
# 5)Concatenation of Strings

#1.Slicing

str1 = "Hello Welcome to the World of programming"

print("String slicing output : ",str1[0:41])

print(str1[0:30])

print(str1[5:20])

print(str1[20:41])

print(str1[-10:-2])

print(str1[-15:-1])

print('*'*60)
#2)Slice from the start

str2 = "String slicing"

print(str2[0:10])

print(str2[0:18])

print(str2[:3])

print(str2[:7])

print('*'*60)

# 3)Slice to the end

str3 = 'We are learning programming'

print(str3[0:30])

print(str3[6:30])

print(str3[9:])

print(str3[0:])

print('*'*60)

# 4)Negative Indexing

str4 = 'We all are Indian'

print(str4[0:-10])

print(str4[-15:-1])
print(str4[-12:-6])
print(str4[-16:])

print('*'*60)
#5)Concatenation of Strings

str5 = 'Hello'
str6 = 'India'
str7 = str5+str6
print("String Concatenation: ",str7)

print("string concatenation: ",(str5+" "+str6))
