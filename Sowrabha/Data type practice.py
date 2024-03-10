#Integer data type
var1=2
var2=564783
print(var1,var2,type(var1))
print(type(var1))
#float

print("_"*50)
#float data type

var3=567.909
var4=33.45
print(var3,var4,type(var3))

print("_"*50)

#Complex number

var5=6+5j
print(type(var5))

#string

print("_"*50)

str="python"
print(str,type(str))

#str = "Python"
# 0  1  2  3  4  5   # +ve Indexing
#" P  y  t  h  o  n"
# -6 -5 -4 -3 -2 -1  # -ve indexing
print("_"*50)
print(str[3])
print(str[1])

#LIST data type

#        0  1     2       3
list1 = [3, 4.5, 'Hello', [4, 6, 8]]
#       -4  -3   -2      -1

print (list1[3])
print(list1[3][1],type(list1))

list1.append(20)#to add values to list
print(list1)

print("_"*50)

#Tuple data type

#       0  1     2        3          4          5       # +ve
tup1 = (3, 4.5, 'Python', [3, 5, 6], (3, 2, 1), True)
#      -6  -5    -4      -3          -2         -1      # -ve

print(tup1[4])
print(tup1[4][1])

print(tup1[-6],)
print(type(tup1))

print("_"*50)

dict1 = {'name' : 'Rahul', 'age' : 20, 'address' : 'Mumbai'}
#       {key : value}

print(type(dict1))
print(dict1)
print(dict1['name'],dict1[ 'age' ])

dict2 = {}
dict2['phone'] = 956755657
print(dict2) # {'phone': 956755657}

dict2={'phone':7406365216}
print(dict2)

dict3 = {'a' : 123, 'b' : 567, 'a' : 333, 'c': 789}
print(dict3)  # {'a': 333, 'b': 567, 'c': 789}

#num3 = 6546
#var3 = list(num3)
#print(var3)





# int ->  string
num2 = 576892
var2 = str(num2)
print(var2, type(var2), var2[2])

