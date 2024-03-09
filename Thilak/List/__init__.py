str1 = "I am learning python"
output = [x.upper() for x in str1.split(" ")]
print(output)

list1 = [1, 2, 3, 4] # looking for the op [1, odd] [2, even].....
"""
for i in list1:
    if i%2 == 0:
        print(i, "even")
    else:
        print(i, "odd")
"""
output= [(i, "even") if i%2 ==0 else (i, "odd")for i in list1]

print(output)