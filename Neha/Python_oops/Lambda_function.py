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
##map-The map() function combined with a lambda expression in Python can perform a variety of mapping operations on a list

addition = lambda x , y : x + y
print(addition(5,5))

#eg-2
list1 = [5, 7, 8, 22, 15]

Square = list(map(lambda x : x**2 , list1))
print(Square)

#arr=[["a", 2],["d", 4],["g", 2],["b",4]]
#[["a", 2],["g", 2],["b", 4],["d", 4]]

#Reduce-The reduce() function combined with a lambda expression in Python can perform a variety of operations on a list.

#Summing a List of Numbers: Calculate the sum of all elements in a list.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)  # Output: 15

#Finding the Maximum Value: Find the largest number in a list.
numbers = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(max_value)  # Output: 97

#Multiplying Elements: Multiply all elements in a list to get the product.
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

#Concatenating Strings: Concatenate a sequence of strings into a single string.
strings = ['I ', 'love ', 'Python ', 'programming']
concatenated_string = reduce(lambda x, y: x + y, strings)
print(concatenated_string)  # Output: I love Python programming


# Filter : The filter() function combined with a lambda expression in Python can perform a filter operations on a list
# return the output as only with expected values.

print("_"*50)

list_a = [4, 7, 9, 22, 33, 11, 26]

result_a = list(filter(lambda x: x%11 == 0, list_a))
print("Result a:", result_a)


#Filtering Strings: To filter a list of strings, you might want to include only those that meet a certain condition. For example, filtering out strings that contain a specific substring:

string_list = ['apple', 'banana', 'cherry', 'date']
filtered_strings = list(filter(lambda x: 'a' in x, string_list))
print(filtered_strings)

#output:['apple', 'banana', 'date']

#Filtering Dictionaries: When filtering dictionaries, you can filter by keys, values, or both. For instance, to keep only the key-value pairs where the value is greater than zero:

my_dict = {'joe': 20, 'bill': 20.232, 'tom': 0.0}
filtered_dict = {k: v for k, v in my_dict.items() if v > 0}
print(filtered_dict)

#output:{'joe': 20, 'bill': 20.232}


arr=[["a", 2],["d", 4],["g", 2],["b",4]]
#[["a", 2],["g", 2],["b", 4],["d", 4]]

arr.sort(key=lambda x: (x[1],x[0]))
print(arr)

players = [('Alice', 9), ('Bob', 5), ('Cindy', 7), ('David', 6)]
sorted_players = sorted(players, key=lambda player: player[1])
print(sorted_players)
#output : [('Bob', 5), ('David', 6), ('Cindy', 7), ('Alice', 9)]

max_score = max(players ,key=lambda x : x[1])
print(max_score)

min_score = min(players,key=lambda x:x[1])
print(min_score)

strings = ['apple', 'banana', 'cherry', 'date', 'me']
#Wrong statement--->>shortest_str = min(key=lambda s:len(s), strings )
shortest_string = min(strings, key=lambda s: len(s))
print(shortest_string)  # Output: 'me'

#summing the second element in a list of tuples:
tuples = [(1, 2), (3, 4), (5, 6)]

# sum_value = (sum(map(lambda x: x[1],tuples)))
# print(sum_value)
sum_of_second_elements = sum(map(lambda x: x[1],tuples))
print(sum_of_second_elements)




