"""
 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
  'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
   'symmetric_difference', 'symmetric_difference_update', 'union', 'update'

"""

# difference method : this method return the difference values between two sets.

set1 = {4, 7, 9, 2, 'a', 'b'}
set2 = {4, 2, 'a', 11, 33, 55}

result = set1.difference(set2)
print("difference values :", result)  # {9, 'b', 7}

result2 = set2.difference(set1)
print("difference values in set2 :", result2)  # {33, 11, 55}

# difference update : this method will update the set with difference only and remove all common values

set1.difference_update(set2)  # {7, 9, 'b'}

print("set1 :", set1)  # {7, 9, 'b'}
print("set2 :", set2)  # {4, 2, 'a', 11, 33, 55}

# box1 = apple, mango , banana | apple, mango
# box2 = lichi, watermelon, mango

# output = apple banana
print("_" * 50)
##############################
# issubset, issuperset

seta = {5, 8, 2, 4, 7, 22, 11}
setb = {2, 7, 4}
setc = {7, 22, 33}

print("is seta is superset of setb :", seta.issuperset(setb))  # True
print("Is seta is superset of setc :", seta.issuperset(setc))  # False

print(" is setb is subset of seta :", setb.issubset(seta))  # True
print(" is setc is subset of seta :", setc.issubset(seta))  # False

print("_" * 50)
###################################
# 'symmetric_difference','symmetric_difference_update'
# 'symmetric_difference' : This method return the difference of values from both sets

setp = {5, 7, 9, 2, 'a', 'b', 'c'}
setq = {'a', 'b', 6, 88, 11, 5}

result = setp.symmetric_difference(setq)
print("symmetric difference :", result)  # {2, 'c', 6, 7, 9, 11, 88}

result2 = setq.symmetric_difference(setp)
print("result2 :", result2)  # {2, 'c', 6, 7, 9, 11, 88}

# symmetric_difference_update : this method will update the target with symmetric_difference values
print("set p :", setp)
print("set q :", setq)

setp.symmetric_difference_update(setq)

print("after update set p :", setp)  # {2, 6, 7, 9, 11, 88, 'c'}
print("set q :", setq)  # {5, 6, 'b', 88, 'a', 11}

box1 = 'cricket', 'hockey', 'football'
box2 = 'tennis', 'cricket', 'bedmenton'

# symmetric difference : hockey, football, tennis, bedmenton
# symmetric difference update box1 : hockey, football, tennis, bedmenton

print("_" * 40)
############################### copy ######################
# deep copy and shallow copy

# shallow copy
setj = {4, 7, 9, 2}
setk = setj
setk.add(50)

print("set j :", setj)
print("set k :", setk)

# deep copy
setn = {'a', 'b', 'c', 'd'}
setm = setn.copy()
setm.add(100)
print("setn :", setn)  # {'b', 'c', 'd', 'a'}
print("setm :", setm)  # {'b', 100, 'd', 'a', 'c'}

print("_"*50)
##########################################################
# find out the unique values from list
list1 = [5, 8, 3, 9, 2, 8, 12, 44, 5]

# solution1 :
val = set(list1)
print(val)  # {2, 3, 5, 8, 9, 12, 44}
print(list(val)) # [2, 3, 5, 8, 9, 12, 44]

# solution2
output = []
for val in list1:
    val_count = list1.count(val)
    if val_count == 1 and val not in output:
        output.append(val)
    elif val_count >= 1 and val not in output:
        output.append(val)

print("output :", output)


# solution3
output2 = []

for val in list1:
    if val not in output2:
        output2.append(val)


print("output 2:", output2)







