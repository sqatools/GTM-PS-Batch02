tuple1 = (5, 7, 9, (4, 6, 7), [3, 6, 8], 'Hello', 5.5)

print(tuple1, type(tuple1))

# get values from tuple with index

print(tuple1[3][1]) # 6

print(tuple1[-3][2]) # 8

print(tuple1[5][3]) # l

# slicing in the tuple

tup2 = (4, 5.6, None, True, {'a' : 56, 'b' : 23}, "Python Programming",
        (3, 6, 7), [2, 4, 7, 8])

print(tup2[2:5])  # (None, True, {'a': 56, 'b': 23})

print(tup2[-3][2:5]) # tho

print(tup2[-1][::-1]) # [8, 7, 4, 2]

print(tup2[1::2]) # (5.6, True, 'Python Programming', [2, 4, 7, 8])


# tuple methods
print(dir(tuple))

# 'count', 'index'

# count method :
tup_a = (4, 7, 8, 3, 4, 7, 2, 5, 7)
print("count of 4 :", tup_a.count(4))
# count of 4 : 2
print("count of 7 :", tup_a.count(7))
# count of 7 : 3
# print("count of 7 :", tup_a.count())
# TypeError: tuple.count() takes exactly one argument (0 given)

# Get length of tuple
print("length  :", len(tup_a))
# length  : 9

# get index of any value
print("index position of 8:", tup_a.index(8))
# index position of 8: 2

################### Apply loop on the tuple #############

# without indexing
tup_b = (303, 5, 7, 1, 9, 23, 56, 89)

for val in tup_b:
    print("val :", val)


# with indexing
for i in range(len(tup_b)):
    print(i, ":", tup_b[i])

print("max value :", max(tup_b))  # max value : 303
print("min value :", min(tup_b))  # min value : 1
print("sum of values :", sum(tup_b))  # sum of values : 493

# tuple is faster than list in terms of performance.

# tuple comprehension

tup_d = (5, 7, 9, 22, 66, 88, 12, 11, 13)

result = (val for val in tup_d if val%2 == 0)
print("result :", result)
for val in result:
        print(val)