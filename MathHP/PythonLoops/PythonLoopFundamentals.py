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








