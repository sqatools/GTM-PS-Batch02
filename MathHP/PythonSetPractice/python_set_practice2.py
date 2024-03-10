
print(dir(set))

# Methods in set

# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint',
# 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

"""
Set is mutable , value once assigned can't be changed
Random order, No duplicates
Members of the set are immutable data types int,float,boolean,string,tuple
Mutable data types can't be the memmber of the set like set, list ,dict
"""

# difference() method: This method return the difference values between two sets A-B
# Present in seta but not in setb  , A-B

set1 = {6,7.5,'Hope',(1,2,3),False}
set2 = {29,17.87,'Grace',(9,8,7),True}
set3 = set1.difference(set2)
print("set3:",set3)                  # set3: {False, 6, 7.5, (1, 2, 3), 'Hope'}

seta = {6,8,9,3,4,5}
setb = {8,9,3,100,99,20}
result = seta.difference(setb)
print("Result:",result)             #Result: {4, 5, 6}
result1 = setb.difference(seta)
print("Result1:",result1)          # Result1: {99, 100, 20} , present in setb but not in seta

# difference_update : This method will update the set with difference only and remove all common values

setc = {45,89,23,90,100}
setd = {97,21,65,43,100,76,45,89}
setc.difference_update(setd)       #setc: {23, 90}
print("setc:",setc)
sete = {95,79,13,99,100}
setf = {97,21,65,43,100,95,79,89}
setf.difference_update(sete)
print("setf:" ,setf)

set1 = {4, 7, 9, 2, 'a', 'b'}
set2 = {4, 2, 'a', 11, 33, 55}
print("diff:",set1.difference(set2))                     #diff: {9, 'b', 7}
print("diff_update:",set1.difference_update(set2))       #diff_update: None
# difference_update method  does not return anything. That's the reason None is the output

print("set1:",set1)                                     #set1: {7, 9, 'b'}

# difference method :
# Only returns the difference values between two sets, but it does not modify the original sets

# difference_update method gives the same output , but it will update the original set.
# Modifies the original set

###################################################################################

# box1 = apple, mango , banana | apple, mango
# box2 = lichi, watermelon, mango

# output = apple banana
print("_" * 50)

# issubset ,issuperset
# issuperset - set a is a superset of setb if it contains all elements of setb along with extra elements


seta = {5,8,2,4,7,22,11}
setb = {2,7,4}
setc = {7,22,33}

result = seta.issuperset(setb)
print("seta is superset of setb:" , result)                   #seta is superset of setb: True
result1 = setc.issuperset(setb)
print("setc is superset of setb:" ,result1)                   #setc is superset of setb: False

result2 = setb.issubset(seta)
print("setb is a subset of seta:",result2)                   #setb is a subset of seta: True
result3 = setc.issubset(seta)
print("setc is a subset of seta:",result3)                   #setc is a subset of seta: False

print("$$"*60)

##################################################
# 'symmetric_difference', 'symmetric_difference_update'

# 'symmetric_difference': This method return the difference of values from both sets
# (A-B)U(B-A)
# Present in seta but not in setb together with present in setb but  not in seta

setp = {5,7,9,2,'a','b','c'}
setq = {'a','b',6,88,11,5}

solution = setp.symmetric_difference(setq)
print("Solution:" ,solution)                                  # Solution: {2, 6, 7, 'c', 9, 11, 88}

solution1 = setq.symmetric_difference(setp)
print("Solution1:" ,solution1)                                # Solution1: {2, 6, 7, 9, 11, 88, 'c'}

# Always symmetric difference of two sets will be equal

#'symmetric_difference_update' : This method will update the target with symmetric_difference values

print("setp:",setp)                  #setp: {'a', 2, 5, 'c', 7, 9, 'b'}
print("setq:",setq)                  #setq: {'a', 5, 6, 88, 11, 'b'}

setp.symmetric_difference_update(setq)

print("after update set p :",setp)                           # after update set p : {2, 6, 7, 9, 11, 88, 'c'} setp is changed after updation
# setp is modified with symmetric difference update

print("setq:",setq)                                          #setq: {5, 6, 'b', 88, 11, 'a'} same setq no change

box1 = {'cricket','hockey','football'}
box2 = {'tennis','cricket','badminton'}
print("sym diff:",box1.symmetric_difference(box2))           #sym diff: {'tennis', 'hockey', 'badminton', 'football'}
print("sym diff1:",box2.symmetric_difference(box1))          #sym diff1: {'tennis', 'hockey', 'badminton', 'football'}
print("sym diff up:",box1.symmetric_difference_update(box2)) #sym diff up: None
print("box2:",box2)                                          #box2: {'cricket', 'tennis', 'badminton'}
print("sym diff up box1:",box2.symmetric_difference_update(box1))  #sym diff up box1: None
print("box1:",box1)                                          #box1: {'hockey', 'football', 'tennis', 'badminton'}

print("$$"*60)

################################ copy ######################################

# deep copy and shallow copy

# shallow copy , will reflect on both sets

setj = {4,7,9,2}
setk = setj
setk.add(50)

print("setj:",setj)        #setj: {2, 4, 7, 9, 50}
print("setk:",setk)       #setk: {2, 4, 7, 9, 50}

# deep copy , will reflect on only one set not both

setn = {'a','b','c','d'}
setm = setn.copy()
setm.add(100)
print("setn:",setn)              #setn: {'b', 'a', 'd', 'c'}
print("setm:",setm)             #setm: {100, 'c', 'b', 'a', 'd'}

print("_"*50)
##########################################################

# Find out the unique values from list

list1 = [5,8,3,9,2,8,12,44,5]

# solution1:

val = set(list1)               # {2, 3, 5, 8, 9, 12, 44} , duplicates not allowed in set , so only unique values
print("Unique values in list using set :",val)

#solution2

output = []
for val in list1:
    val_count = list1.count(val)
    if val_count == 1 and val not in output:
        output.append(val)
    elif val_count >=1 and val not in output:
        output.append(val)

print("Output :",output)        #Output : [5, 8, 3, 9, 2, 12, 44]

#solution3

output2 = []

for val in list1:
    if val not in output2:
        output2.append(val)

print("output2:",output2)       #output2: [5, 8, 3, 9, 2, 12, 44]

















