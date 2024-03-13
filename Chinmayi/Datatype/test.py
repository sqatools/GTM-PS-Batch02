#str1 = “Rahul Mohit John Rahul Vaibhav John”

#Output = “Rahul John”

str1 ="Rahul Mohit John Rahul Vaibhav John"
str2 = str1.split()

count = 1

for i in str2:
    if i in str2:
        count +=1
        if count > 1:
            print(i)



"""
str1 = "India is best cricket Team in the World"

#output = “cricket”

str2 = str1.split(" ")
print(str2)
for val in str2:
    val1 = len(val)
    print(val1,val)





Oper = input("Enter a Math operation : ")
val1 = int(input("Enter the first value: "))
val2 = int(input("Enter the second value: "))
result = 0

Oper1 = ["add", "multiple", "subtract", "division"]
if Oper in Oper1:
    if Oper == "add":
        result = val1 + val2
    elif Oper == "multiple":
        result = val1 * val2
    elif Oper == "subtract":
        result = val1 - val2
    elif Oper == "division":
        result = val1 / val2
else:
    print("Enter a correct Math Operation")
print("Result:", result)

#Write Python Program to move all positive number on left side and negative values on right side.

Input = [2, -16, 6, 44, -71, 18, -11, -1]
temp = []
temp1 = []

#Output: [2, 6, 44, 18, -16, -71, -11, -1]

for val in Input:
    if val > 0:
        temp.append(val)
    else:
        temp1.append(val)

print("Output:", temp + temp1)


"""





