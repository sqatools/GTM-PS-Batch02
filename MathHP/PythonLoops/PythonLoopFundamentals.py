#range(initial value,end value,different value


for i in range(1,10,1):                  # initial value 1 and less than final 10 , 1 to 9
    print(i)


for i in range(1, 10, 2):              # initial value 1 and less than final 10 , 1 to 9, difference 2
        print(i)


for i in range(0, 10, 2):              # initial value 0 and less than final 10 , 1 to 9, difference 2
            print(i)                   # range initial, final, difference , takes 3 parameters

#range with two parameters
#range(initial,end)
#default difference value is 1

for i in range(1,10):                 # initial to end-1
    print(i)

#range with one para: range(last value)
#default initial value will be 0 and difference value will be 1

print("_"*50)

for j in range(5):                    # repeats the loop
    print(j)                          # 1 value will be always end value
    print("_" * 50)                   #after each and every value

##########WAP to print the table of any given number

print("_" * 40)
num1 = 5

for i in range(1,11):
    print(i, "*" ,num1, ":" , i*num1)               #Times table

#### Print values in reverse order

print("_"*50)
for i in range(10,0,-1):
    print(i)

for i in range(-10,-20,-1):
    print(i)

# for i in range(-10, -20):                # difference 1 by default -10,-9.-8,    not possible no output
#         print(i)

        ###Check if condition in ;oop
        ###Get all the even number from 1 to 50

for i in range(1,50):
    if i%2 == 0:
        print(i)

#### Get factorial of any given number
# Fact of 5 = 5! = 5*4*3*2*1 = 120

fact = 1
num = 5

for i in range(num,0,-1):
    fact = fact*i                            #maintain the intendation
    #i=5, 1*5 = 5
    #i=4, 5*4 = 20
    #i=3, 20*3 = 60
    #i=2, 60*2 = 120
    #i=1, 120*1 = 120

print("Factorial output :" ,fact)

### break - can't execute further , stops the execution
### continue - that particular step is skipped and then continues from next

##### continue and break condition

print("_"*50)
for i in range(10):
    if i>5 and i<8:                            ### skipped 6,7 rest printed move to next iteration
        continue
    print(i)

print("_" * 50)
for i in range(10):
    if i > 5 and i < 8:
     break                                     ### from 6 it will stop the execution, 6,7,8,9 not printed
    print(i)

print("_" * 50)

for i in range(10):
        if i == 6:
            break                             ### from 6 it will stop the execution, 6,7,8,9 not printed
        print(i)

### Find out the palindrome number and check its output

print("_"*50)
num1 = 121
num2 = str(num1)                                           # int to String

if num1 == int(num2[::-1]):                                # :: means reverse order , convert String to int
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")

## Query Question:
#input = [1,"cat","dog",'true',10]

var1 = 40
print(type(var1))

if isinstance(var1,int):                                  # isinstance is for checking the type
    print("This is an integer")
else:
    print("Not an integer")

# Apply loop  on the list

input_values = [1,"cat","dog",True, 10, 6.7, [4,5,7]]

for data in input_values:                                  # declare and initialise input_values
     print(data)
     if isinstance(data, int):                             # isinstance is for checking the type
         print("This is an integer")
     elif isinstance(data, str):
         print("String")
     elif isinstance(data,float):
         print("Float")
     elif isinstance(data, list):
         print("list")
     elif isinstance(data, bool):
         print("Boolean")

# apply loop on the String

print("_"*50)
str1 = "Hello Good Morning"
vowels = "aeiouAEIOU"
result = ""
for char in str1:
    print(char)
    if char in vowels:
        continue                                    # ignores that particular line is skipped
    else:
        result = result + char                      # "" + H = H
print("result" ,result)

print(dir(str))                                    # dir() function provides us to find what and all present inside

#### Apply loop on tuple

print("_"*50)
tup1 = (5,7,'Hello', (4,7,9),7,9)
addition = 0
for val in tup1:
    if isinstance(val,int):
        print(val)
        addition = addition + val
    else:
        continue
print("Addition output:", addition)

## Apply loop on dictionary

dict1 = {'a' : 123, 'b' : 345, 'c' : {'e' : {'f' : 789}}}

for val in dict1.items():                                    #items() is  a function
    print(val)

### apply loop on set
set1 = {50,60,70,80}
for val in set1:
    print(val**2 , end =" ")                      # end = " " same line print    # **2 , square of 50,60,70,80

##6400
# 2500              Random order
# 3600
# 4900












