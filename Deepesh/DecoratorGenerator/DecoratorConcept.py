# Decorator : Decorator will decorate existing code without changing its functionality.

def decorator(func):
    def inner(param):
        print("_"*50)
        func(param)
        print("_"*50)
    return inner


@decorator
def greeting(msg):
    print(msg)

greeting("Good Morning")

@decorator
def square(num):
    print("square 0f value :", num**2)


square(5)

def limit(func):
    def inner(param):
        if  param > 10:
            func(10)
        else:
            func(param)
    return inner

@limit
def get_square_number(nums):
    for i in range(1, nums):
        print(i**2, end=" ")


get_square_number(11)
