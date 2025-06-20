"""

In Python, a generator is a special kind of iterator that allows you to iterate over a sequence of values. Unlike lists,
generators do not store all the values in memory; instead, they generate each value on the fly as you iterate through them,
which can be more memory-efficient for large datasets.

A generator is created using a function that contains one or more yield statements.
When the generator function is called, it returns a generator object without executing the function.
Each time you iterate over the generator object (for example, using a for loop),
the function executes until it hits a yield statement, which returns the yielded value and pauses the function’s execution.
The function resumes where it left off when the next value is requested.

Here’s a simple example of a generator function that yields numbers from 0 to n-1:

Python

def my_generator(n):
    i = 0
    while i < n:
        yield i
        i += 1

# Using the generator
for number in my_generator(3):
    print(number)

This will output:

0
1
2


What are some advantages of using generators over lists?

Generators offer several advantages over lists, particularly when dealing with large datasets:

Memory Efficiency: Generators do not store all the values in memory; they generate them on-the-fly, which saves memory especially for large data sets1.
Lazy Evaluation: They compute values only when needed, allowing the program to start using the data immediately while the rest is being computed1.
Improved Performance: By yielding one value at a time, generators can provide better performance as they minimize resource usage2.
Responsiveness: They can make your code more responsive to the end user by generating values as they are needed, rather than upfront3.
Single Iteration: Generators are designed to be iterated over once, which is suitable for certain use cases where a single pass through the data is sufficient4.
These characteristics make generators a powerful feature in Python for efficient data processing1432.

"""

def greetings():
    yield "good Morning"
    yield "how are you"
    yield "Hope you are fine"
    yield "Learning python automation"

gen_obj = greetings()
print(gen_obj)

for data in gen_obj:
    print(data)


"""
Decorator: Its a design pattern that allows the to add functionality to an existing method/function 
without modify the original structure
Decorators are commonly used for tasks such as logging, authentication, caching.


"""
