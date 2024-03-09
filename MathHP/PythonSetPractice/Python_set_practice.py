### Set
# No duplicates, only unique, {}, random order
# Only immutable data

set1 = {'a','b',4,8,2,'c',2,'a'}

print(set1,type(set1))                      #{'a', 2, 4, 'c', 8, 'b'} <class 'set'>

"""
Properties : 
Set is mutable data type, we can modify the set at any point of time
Set contains only immutable data type as member,int,float,string,tuple,boolean
Mutable data type cannot be the member of set, list, dict and set
Set does not follow index, data stored in random order
"""

set2 = {4,4.5,'Hello',(5,7,8),True}
print("Set2:",set2)                         # Set2: {True, 4, 4.5, 'Hello', (5, 7, 8)}

# set3 = {[4,6,8,98]}
# print("Set3 with list as data member :",set3)          list is mutable , list cant be the data member of set
#  set3 = {[4,6,8,98]}

#TypeError: unhashable type: 'list'

############################# Methods in set##########################

print(dir(set))

# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint',
# 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'


# add() method: This method add data to the set

seta = {6,8,9,4,5,2}
seta.add(700)
print("seta:",seta)             #seta: {2, 4, 5, 6, 8, 9, 700}

print("_" * 50)

#update() method: This method update data from set1 to set2

set_c = {5,8,0,2}                      #int immutable
set_d = {'a','b','c','d'}             # string immutable data member

set_d.update(set_c)                 # Values of set_d in addition to the values of set_c
print("set_d",set_d)               #set_d {0, 'd', 'c', 2, 5, 'b', 8, 'a'}
print("set_c:",set_c)             # set_c: {8, 0, 2, 5} Random order , No change

set_d.update({6789})            # Can update a single value but it should be in the form of set
print("set_d",set_d)           #set_d {0, 2, 5, 6789, 8, 'c', 'd', 'b', 'a'}

print("_" * 50)

# union() method: This method combine two sets and return new set

set_e = {5,8,0,2,22,'a','b'}
set_f = {'a','b','c','d',22}

set_g = set_f.union(set_e)                # set_g {0, 2, 5, 8, 'b', 'c', 'd', 22, 'a'}
print("set_g",set_g)

set_g = set_e.union(set_f)               # Whatever order it can be , both same
print("setg1:",set_g)                    #setg1: {0, 2, 5, 'c', 8, 'b', 22, 'd', 'a'}

print("set_e:",set_e)                   #set_e: {0, 2, 5, 'b', 'a', 8, 22}
print("set_f:",set_f)                   #set_f: {'d', 'c', 'b', 'a', 22}


################# Remove data from set ##############
print("_" * 50)

#remove() method : This removes specific data from set and does not return

set_h = {6,8,3,90,88}
set_h.remove(90)
print("set_h:",set_h)                 #set_h: {3, 6, 8, 88}

# set_h.remove(4)
# print("set_h:",set_h)

# set_h.remove(4)
# KeyError: 4

# if given data is not available in the set , then it will throw the error

##############################################

# discard() method: This method removes data from the set and does not return anything

set_i = {9,7.8,False,'BBC',(7,8,9)}
set_i.discard(7.8)
print("set_i:",set_i)               #set_i: {False, (7, 8, 9), 'BBC', 9}

set_k = {657,97,4,100}
set_k.discard(10000)
print("set_k:",set_k)               # set_k: {657, 100, 4, 97} same set values no changes , as 10000 is not available inside the set

# If the target data is not available in the set, then discard does not show error

# remove() throws error if the value not present inside set
# discard() does not throw error if the value is not present as well

#############
print("_" * 50)

#pop() method : This removes data from set and return it
# To reduce the data set

set_l = {8,9,3,5,7,8,2,7,100}
val = set_l.pop()
print("Removed val:",val)
print("set_l:",set_l)

# Removed val: 2
# set_l: {3, 100, 5, 7, 8, 9}

# Everytime as you run the code, it will remove any random value , cant predict
# Each time it changes

#################################################

# clear() method : This method removes all data from the set

set_m = {7,4,8,9,2,3,0,1,7}
set_m.clear()
print("set_m:",set_m)                 # set_m: set() , blank set

set_a = set()
print("set_a:",set_a)                  # set_a: set()

# Empty set is set()
# dont use {} which represents dictionary

####################################################
# del function to remove the set object from memory

set_v ={5,8,9,22}
del set_v
#print("set_v :",set_v)            #NameError: name 'set_v' is not defined , bcoz set is deleted

# intersection method: common elements

set_a = {'a','b','c','d',5,6,7}
set_b = {5,10,50,70,33,'a','b'}

output = set_a.intersection(set_b)
print("Intersection output:" ,output)        #Intersection output: {'b', 5, 'a'}

# intersection_update method: This method update the intersection values to target set
# set_a is updated with the intersection values completely , all other values are discarded

updated_data = set_a.intersection_update(set_b)
print("set_a:",set_a)                         # set_a: {5, 'b', 'a'} only intersection elements
print("set_b:",set_b)                        # set_b: {33, 50, 5, 70, 'a', 10, 'b'} , same values as set_b no change

updated_data1 = set_b.intersection_update(set_a)
print("set_b:",set_b)                     #set_b: {'a', 'b', 5} only intersection
print("set_a:",set_a)                    # set_a: {'a', 'b', 5} since set_a is already done with intersection_update


