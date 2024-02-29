# dict1 = {'key' : 'value'}

dict1 = {'a' : 456,
         4: 'Hello',
         4.5 : [4, 7, 8],
         (1, 4, 6) : {'a' : 4567, 'b' : 123},
         True : {5, 7, 9, 2},
         }

# Create a dictionary with the given 2 lists
list1 = ['a', 'b', 'c']
list2 = [123, 456, 78, 9]
output = {}
for i in range(len(list1)):
    output[list1[i]] = list2[i]
print("output: ", output) # {'a': 123, 'b': 456, 'c': 78}

srt1 = "Python"
list3 = [4, 6, 8, 2, 9, 10]
output2 = {}
for i in range(len(srt1)):
    output2[srt1[i]*2] = list3[i] # output:  {'PP': 4, 'yy': 6, 'tt': 8, 'hh': 2, 'oo': 9, 'nn': 10}
print("output: ", output2)



