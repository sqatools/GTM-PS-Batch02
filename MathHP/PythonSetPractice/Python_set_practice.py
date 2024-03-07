








# 01/03/2024 Friday



####################################################
# del function to remove the set object from memory

set_v ={5,8,9,22}
del set_v
#print("set_v :",set_v)            #NameError: name 'set_v' is not defined

# intersection method:

set_a = {'a','b','c','d',5,6,7}
set_b = {5,10,50,70,33,'a','b'}

output = set_a.intersection(set_b)
print("Intersection output:" ,output)        #Intersection output: {'b', 5, 'a'}

updated_data = set_a.intersection_update(set_b)
print("set_a:",set_a)
print("set_b:",set_b)
