"""
A lambda function in Python is a small anonymous function defined with the lambda keyword.
It can take any number of arguments but only contains a single expression, which is evaluated and returned.
Here’s a simple example of a lambda function that adds 10 to the input argument:

Python

x = lambda a: a + 10
print(x(5))  # Output: 15

Lambda functions are particularly useful when you need a simple function for a short period
 and are often used in conjunction with functions like filter(), map(), and reduce()
"""

#arr=[["a", 2],["d", 4],["g", 2],["b",4]]
#[["a", 2],["g", 2],["b", 4],["d", 4]]

#Reduce

"""
The reduce() function combined with a lambda expression in Python can perform a variety of operations on a list. Here are some examples:

Summing a List of Numbers: Calculate the sum of all elements in a list.
Python

from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)  # Output: 15
AI-generated code. Review and use carefully. More info on FAQ.
Finding the Maximum Value: Find the largest number in a list.
Python

from functools import reduce
numbers = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(max_value)  # Output: 97
AI-generated code. Review and use carefully. More info on FAQ.
Multiplying Elements: Multiply all elements in a list to get the product.
Python

from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120
AI-generated code. Review and use carefully. More info on FAQ.
Concatenating Strings: Concatenate a sequence of strings into a single string.
Python

from functools import reduce
strings = ['I ', 'love ', 'Python ', 'programming']
concatenated_string = reduce(lambda x, y: x + y, strings)
print(concatenated_string)  # Output: I love Python programming
AI-generated code. Review and use carefully. More info on FAQ.
These are just a few examples of the operations you can perform with reduce() and lambda functions. The key is to define the lambda function according to the operation you want to perform on the elements of the iterable
"""
