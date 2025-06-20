def read_file(filename):
    with open (filename,"r") as file:
        fileread = file.read()

    filedata_1 = fileread.split(" ")
    longest_word = max(filedata_1, key = len)
    print(longest_word)

longest_word_file("first_file_1.txt")

what is class:
    its a blueprint of any object
what is object
Object is entity or module for any class through which we ca access all the methods and function of it

patternProgram

for i in range (1,4):
    for j in range(i):
        print("*", end = " ")
    print( )

for i in range (4,0,-1):
    for j in range(i):
        print("*", end = " ")
    print( )

fibnocci
n1 = 0
n2 = 1

for i in range(2,10):
    sum = n1+n2
    print(sum)
    n1 = n2
    n2 = sum

#Prime

num= int(input("enter the number"))
count = 0


for i in range(1, num+1):
    if (num % i) == 0:
            count += 1
if count == 2:
    print("prime")
else:
    print("not prime")



##Factorial

num = int(input("enter the input number:"))
factorial = 1

if num < 0:
    print("no factorial")
elif num == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial*i
    print(factorial,"is the factorial for number",num)

#Split str
str = "My name is neha"

word =str.split(" ")[-1::-1]
final_output = " ".join(word)
print(final_output)

#6  Python Dictionary Program to create a dictionary from two lists.
list1 = ['a', 'd', 'e']
list2 = [12, 23, 24]
# # Output :
# # output dict: {'a': 12, 'd': 23, 'e': 24}
output = {}
#
# for i in range (len(list1)):
#     if i < len(list2):
#         output[list1[i]] = list2[i]
#     else:
#         output[list1[i]] = None
#
# print ('output dict:',output)

#list program
list = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]

#count value
values_count = {value:list.count(value) for value in list}
#remove duplicates
unique_list = (set(list))

print(f'Count of all values:{values_count}')
print(f"Unique list:{unique_list}")

list = [9,23,4,455,6,6,6,21,8,7,6,]

i = 0
for i in range (i ,len(list)):
    for j in range (i+1,len(list)):
        if (list[i] > list[j]):
            temp = list[i]
            list[i] = list[j]
            list[j] = temp

print (list)

list1 = [5, 7, 8, 2, 3]
#output = [25, 49, 64, 4, 9]

output = []
for val in list1:
    sqr = val**2
    output.append(sqr)
print("output :", output)

# loop with list comprehesion
result = [x**2 for x in list1 if x%2 == 0]
print("result :", result)

out_dict = { x:x**2 for x in list1 if x%2 == 0 }
print(out_dict)








