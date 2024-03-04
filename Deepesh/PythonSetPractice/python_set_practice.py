set1 = {'a', 'b', 4, 8, 2, 'c', 2, 'a'}

print("set1 :", set1, type(set1))
# set1 : {'c', 'b', 2, 4, 'a', 8} <class 'set'>

"""
# properites 
 - set is mutable data type, we can modify the set at any point of time.
 - set only contains immutable data type as member, int, float, string, tuple, boolean
 - Mutable data type can not member of set, list, dictionary and set.
 - Set does not follow index, data store in random order.
"""

set2 = {
    4, 4.5, 'Hello', (5, 7, 8), True,
    # [5, 7, 8], TypeError: unhashable type: 'list'
    # {'a' : 456, 'b' : 333}  # TypeError: unhashable type: 'dict'
}

print("set2 :", set2)

################## Methods in the set ##################
print(dir(set))

"""
 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
  'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
   'symmetric_difference', 'symmetric_difference_update', 'union', 'update'
"""

# add() method : this method add data to the set

seta = {5, 8, 9, 2, 1}
seta.add(700)
print("seta :", seta)
# seta : {1, 2, 5, 8, 9, 700}

#####################
print("_" * 50)
# update() method : this method update data from set1 to set2

set_c = {5, 8, 0, 2}
set_d = {'a', 'b', 'c', 'd'}

set_d.update(set_c)
print("set_d :", set_d)  # {0, 2, 'c', 'b', 5, 8, 'd', 'a'}
print("set_c :", set_c)  # {8, 0, 2, 5}

set_d.update({50})
print("set_d :", set_d)  # {'b', 0, 2, 5, 'a', 8, 50, 'd', 'c'}

##############################
print("_" * 50)
# union() method : This method combine two sets and retrun new set

set_e = {5, 8, 0, 2, 22, 'a', 'b'}
set_f = {'a', 'b', 'c', 'd', 22}

# set_g= set_e.union(set_f)
set_g = set_f.union(set_e)

print("set_g :", set_g)  # {0, 2, 5, 8, 'd', 'a', 'b', 22, 'c'}
print("set_e :", set_e)
print("set_f :", set_f)

################# Remove data from set ##############
print("_" * 50)
# remove() method :  This remove specific data from set and does not return.

set_h = {6, 8, 3, 90, 88}
set_h.remove(90)
print("set_h :", set_h)  # set_h : {3, 6, 8, 88}

# if given data is not available in the set, then it will show error.
# set_h.remove(100)  # KeyError: 100


##################
# discard() method : this method remove data from set and does not return anything

set_j = {6, 9, 33, 66, 99}
set_j.discard(33)

print(" set_j :", set_j)
# set_j : {66, 99, 6, 9}

# if the target data is not available in the set, then discard does not show error.
set_j.discard(200)
print(" set_j :", set_j)

#############
print("_" * 50)
# pop() method : this remove data from set and return it.

set_k = {5, 7, 8, 22, 33, 55}
val = set_k.pop()
print("removed value:", val)  # removed value: 33
print("set_k :", set_k)  # {5, 22, 7, 8, 55}

############
# clear method : this method remove all the data from set
set_l = {5, 7, 9, 22}
set_l.clear()
print("set_l :", set_l)  # set()

set_a = set()
print("set_a :", set_a)

##################
# del function to remove the set object from memory.

set_v = {5, 8, 9, 22}
del set_v
# print("set_v :", set_v) # name 'set_v' is not defined. Did you mean: 'set_c'?

#####################
# intersection method: This method return the common values between both sets.

set_a = {'a', 'b', 'c', 'd', 5, 6, 7}
set_b = {5, 10, 50, 70, 33, 'a', 'b'}

output = set_a.intersection(set_b)
print("intersection output :", output)  # {'a', 5, 'b'}

# intersection_update method : this method update the intersection values to target set.
set_b.intersection_update(set_a)
print("set_a :", set_a)  # {'a', 'c', 'b', 7, 5, 6, 'd'}
print("set_b :", set_b)  # {'a', 'b', 5}
