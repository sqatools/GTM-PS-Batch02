########################### While Loop condition

# To execute the code
# Print 1 to 10

temp = 1
while temp <= 10:                # if executed only once , while is infinite loop
    print(temp)
    temp += 1                    # temp++ not allowed

# WAP for infinite loop

n=1
while True:                     # Condition should be true then only will enter inside the loop , if False it will not get inside
    print(n)
    n += 1
    if n== 100:                 # 1,2, ....99 not 100
        break                   # while is for infinite

##### Find out the reverse of any given number without using type casting

num = 452
#output  = 254

reverse = 0

while num>0:
    temp = num%10              # To get last digit
    reverse = reverse*10+temp
    num = num//10                 # Quotient  only means use //
print("Reverse value:",reverse)  # % is remainder and // is for quotient
print("Reverse value:",reverse)  # % is remainder and // is for quotient

##### Armstrong , Palindrome, Reverse of a number





