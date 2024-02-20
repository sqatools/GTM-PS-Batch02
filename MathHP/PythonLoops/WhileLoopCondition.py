########################### While Loop condition

# To execute the code
# Print 1 to 10

temp = 1
while temp <= 10:                # if executed only once , while is infinite loop
    print(temp)
    temp += 1                    # temp++ not allowed that's for only Java

# WAP for infinite loop

n=1
while True:                     # Condition should be true then only will enter inside the loop , if False it will not get inside
    print(n)
    n += 1
    if n== 100:                 # 1,2, ....99 not 100
        break                   # while is for infinite

# n=1
# while False:                    # This code is unreachable will not go inside the loop as condition is false
#     print(n)


##### Find out the reverse of any given number without using type casting

num = 452
#output  = 254

reverse = 0

while num>0:
    temp = num%10                 # To get last digit 2 # 2,5,4
    reverse = reverse*10+temp     # reverse = 2 | 2*10 + 5 = 25 | 25*10+4 = 254
    num = num//10                 # Quotient  only means use //  Removes the last digit from num , ignore the last value , ignores the remainder, num=45
print("Reverse value:",reverse)   # % is remainder and // is for quotient       Reverse value: 254

# First extracting only last digit 2 and remove it as its printed
# Next step is only 45 extracting only 5 and remove it
# Last step is only 4

# % is remainder and // is for quotient

##### Armstrong ,  Reverse of a number

n = 153                                                              # Original number
n1 = n
length = len(str(n))
print("Length of the number ", length)

reverse = 0
arms_num = 0

while n>0:
    temp = n%10                                                        #Only 3
    reverse = reverse*10 + temp                                       # reverse = 3
    arms_num = arms_num + temp**length                               # 1^3 +5^3 +3^3 = 1+125+27 = 153 = original number
    n = n//10

print("Reverse value : ",reverse)

if arms_num == n1:                                                # If Armstrong number == original number
    print("This is Armstrong number :",n1)
else:
    print("This is not the Armstrong number :", n1)


##### Palindrome number

# While reversing the number still it is same as the original number

n = num = 12321                      # initialize 2 variables orelse you will not get the right output
reverse = 0                          # Check everything for original number

while num>0:
    temp = num%10                 # 1
    reverse = reverse*10+temp     # reverse = 1
    num = num//10                 # ignores last digit 1 and concentrates on all other digits

if n == reverse:                  # Condition check alone use other substitute variable
    print("The given number is Palindrome :",n)
else:
    print("The given number is not Palindrome : ",n)







