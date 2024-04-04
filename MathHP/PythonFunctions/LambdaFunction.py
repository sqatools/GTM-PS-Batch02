result = lambda x,y : x+y                     # lambda is the keyword is the function for one-liner operation
print(result(50,60))                   # x,y are variables

# Map, Reduce, Filter                       # 3 places where lambda function can be used

# Map: Map


def square(n):
    return n**2                              # ** is power

list1 = [5,7,8,22,15]

result = list(map(square,list1))
print("Result:",result)                                # Result: [25, 49, 64, 484, 225]

result2 = list(map(lambda x:x**2,list1))
print("Result2:",result2)                             #Result2: [25, 49, 64, 484, 225]