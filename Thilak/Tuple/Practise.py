tup1 = (4, 5.6, None, True, {'a' : 56, 'b' : 23}, "Python Programming",
        (3, 6, 7), [2, 4, 7, 8])

print(tup1[3])
print(tup1[5][6:11:])

print(dir(tuple))

#Methods:
#count & index
tupa = (4, 5.6, None, True, {'a' : 56, 'b' : 23}, "Python Programming",
        (3, 6, 7), [2, 4, 7, 8])
print(tupa.count("Python Programming"))