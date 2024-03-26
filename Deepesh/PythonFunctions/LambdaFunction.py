result = lambda x, y: x+y
print(result(50, 60))


# Map, Reduce, Filter

# Map : map function initiate the mapping or any user defined function or inbuild with
# with list of inputs.

def square(n):
    return n**2

list1 = [5, 7, 8, 22, 15]

result = list(map(square, list1))
print(result) # [25, 49, 64, 484, 225]

result2 = list(map(lambda x:x**2, list1))
print("Result2 :", result2) # [25, 49, 64, 484, 225]

dict1 = {12 : 2, 13 : 12, 14: 15}

result3 = list(map(lambda x:x**2, dict1))
print("Result3 :", result3)  # [144, 169, 196]

list2 = ["Hello", "How", "You", "Hope", "Doing", "Good"]

result4 = list(map(lambda x: x.upper(), list2))
print("result4 :", result4)  # ['HELLO', 'HOW', 'YOU', 'HOPE', 'DOING', 'GOOD']

list3 = ["Python", 2, "Programming", 4]
result5 = list(map(lambda x: x*2, list3))
print("result5 :", result5)
# result5 : ['PythonPython', 4, 'ProgrammingProgramming', 8]

### Filter : filter return the output as only with expected values.
print("_"*50)

list_a = [4, 7, 9, 22, 33, 11, 26]

result_a = list(filter(lambda x: x%2 == 0, list_a))
print("Result a:", result_a)

# Reduce : reduce return the combine result from list of inputs
print("_"*50)
from functools import reduce

list_b = [4, 7, 8, 2, 4]
result_b = reduce(lambda x, y: x+y, list_b)
print("sum of all values :", result_b)


result_c = reduce(lambda x, y: x*y, list_b)
print("product of all values :", result_c)
