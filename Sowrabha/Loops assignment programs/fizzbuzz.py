#Write a program that iterates the integers from 1 to 30 using python.
#For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
#For numbers that are multiples of both three and five print “FizzBuzz”.

for i in range(1,31):
    if i%3==0 and i%5==0:
      print("Fizzbuzz")
    elif i%5==0:
        print("buzz")
    elif i%3==0:
        print("Fizz")
    else:
      print(i)