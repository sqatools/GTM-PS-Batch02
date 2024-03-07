# List,Set and Dict - mutable - can change
# string ,tuple - immutable - can't change

tuple1 = (5,7,9,(4,6,7),[3,6,8],'Hello',5.5)           #Mixture of number, string ,list

print(tuple1,type(tuple1))                             #<class 'tuple'>

# tuple follows same positive and negative indexing
print(tuple1[3][1])   #6
print(tuple1[-3][2])  #8
print(tuple1[5][3])   #l

# Slicing in the tuple

tup2 =(4,5.6,None,True,{'a':56,'b':23},"Python Programming",(3,6,7),[2,4,7,8])        #Mixture of number, string ,list,dict

print(tup2[2:5])         #(None, True, {'a': 56, 'b': 23}) , end-1
print(tup2[-3][2:5])    #tho
print(tup2[-1][::-1])  #[8, 7, 4, 2]
print(tup2[1::2])     #(5.6, True, 'Python Programming', [2, 4, 7, 8])

# tuple methods
print(dir(tuple))

#'count', 'index'

tup_a = (4,7,8,3,4,7,2,5,7)              # tuple is immutable data type
print("Count of 4:", tup_a.count(4))     #Count of 4: 2
print("Count of 7 :",tup_a.count(7))     #Count of 7 : 3
                               #print(tup_a.count())  #TypeError: tuple.count() takes exactly one argument (0 given)
print("Length of the tuple :",len(tup_a)) #Length of the tuple : 9

# get index of any value
print("Index position of 8 :",tup_a.index(8))     #Index position of 8 : 2

################# Apply loop on the tuple

# Without indexing

tup_b = (303,5,7,1,9,23,56,89)

for val in tup_b:
    print("Val:",val)

#Output without indexing
#Val: 303
# Val: 5
# Val: 7
# Val: 1
# Val: 9
# Val: 23
# Val: 56
# Val: 89

# With indexing

for i in range(len(tup_b)):
    print(i, ":", tup_b[i])

#Output with indexing
# 0 : 303
# 1 : 5
# 2 : 7
# 3 : 1
# 4 : 9
# 5 : 23
# 6 : 56
# 7 : 89

# Dynamic data list        changes list
# Static data tuple        7 days in a week , months in a year fixed tuple  , string , tuple immutable , not changed fixed , static

print("Max value:",max(tup_b))      #Max value: 303
print("Min value:",min(tup_b))      #Min value: 1
print("Sum of all values in a tuple :",sum(tup_b))  #Sum of all values in a tuple : 493

# tuple is faster than list in terms of performance
# list has 2 nodes , 1 to modify and 1 to manage the data
# tuple only one single node  to access the data Hence faster

#tuple comprehension
# WAP to find values in tuple divisible by 2

tup_d = (5,7,9,22,66,88,12,11,13)

# for val in tup_d:
#     if val%2==0:
#         print("Divisible by 2:",val)
#     else:
#         print("Not divisible by 2:",val)

result = (val for val in tup_d  if val%2==0)
print("Result:",result)                              #Result: <generator object <genexpr> at 0x000001F104D03780>
for val in result:
    print(val)

# tuple works on generator that's y most efficient in performance
# keeps entire load on the system consuming memory

# 22
# 66
# 88
# 12






