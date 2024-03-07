# 10) reverse() : This method reverses any given list and modify the original list

list1 = [4,7,92,8,1,12]
list1.reverse()
print("Reversed list :",list1)  #Reversed list : [12, 1, 8, 92, 7, 4]

#reversed() function: This function take list as input and reverse the list values with iterator object and loop

list2 = [5,8,2,9,11,55]
result = reversed(list2)
print("Result:",result)
for val in result:
                                       #print(val)   #Result: <list_reverseiterator object at 0x0000020462A55BA0> , value printed in vertical order
    print(val,end=" ")                 # 55 11 9 2 8 5  , same line without [ ]

print("__"*60)

# reverse the list with slicing
list3 = [7,9,8,3,18,4,1]
print("Slicing:" ,list3[::-1])

# Inbuilt function
# Get sum of list values
list4 = [5,7,8,3,1]
print("Sum of list value:", sum(list4))      #Sum of list value: 24
print("Max value of list:",max(list4))      #Max value of list: 8
print("Min value of list:",min(list4))     #Min value of list: 1

lista=["Hello","Howretyuio","Are","You","Hope","YOu","doing","good"]
#print("longest word:",max(lista))          #longest word: good , but good is not the longest word, whichever is the last
print("Longest word:",max(lista,key=len)) #Longest word: Howretyuio, numbers means its OK without key , Strings without key will take ASCII values
print("Smallest word:",min(lista,key=len)) #Smallest word: Are , first smallest word identified

# listc = [5,7,8,"H","W"]  #Mix of numbers and characters
# print(max(listc))
# TypeError: '>' not supported between instances of 'str' and 'int'

print("__"*60)
#################### Deep Copy and Shallow Copy #####
# List, Dictionary and Set same mutable but String is immutable
# Shallow Copy
# In shallow copy , if we change the values in copied list , it will reflect on original list as well, both list will change and ids are same
# Changes reflected in original list as well

listp= [5,7,9,12]
listq=listp
listr = listq
lists = listr
listr.append(100)
print("listq:",listq ,id(listq))    #listq: [5, 7, 9, 12, 100] 1380324156480
print("listp:",listp, id(listp))   #listp: [5, 7, 9, 12, 100] 1380324156480 changes will reflect on both list , id is same
print("listr:",listr,id(listr))   #listr: [5, 7, 9, 12, 100] 1380324156480
print("lists:",lists,id(lists))  #lists: [5, 7, 9, 12, 100] 1380324156480

# Deep Copy , only one list will change not both, ids are also different here bcoz values are different
# Keeping the existing list , its just a copy

listx = [6,8,9,4,2]
listy = listx.copy()      # passing the values of listx to listy using copy, deep copy
listy.append(30)

print("listx:",listx,id(listx))   # listx: [6, 8, 9, 4, 2] same listx , id is 1738289259776
print("listy:",listy,id(listy))  #listy: [6, 8, 9, 4, 2, 30] changes in listy only not listx , id is 1738289313792

# Shallow , reflection both list changed
# Deep , Only copy method and no reflection

########### List comprehension
print("---"*60)

list1 = [5,7,8,2,3]
#Need O/P like output = [25,49,64,4,9]

output =[]
for val in list1:
    sqr = val**2                #power **
    output.append(sqr)
   #print("Output:",output)    # If this is inside for loop 5 times it will print one by one , 25 , 25 and 49, 25 and 49 and 64
print("Output:",output)        #Output: [25, 49, 64, 4, 9]

# loop with list comprehension

result = [x**2  for x in list1] # In one line
print("Result:",result)      #Result: [25, 49, 64, 4, 9]

str1 = "We are Learning Python Programming"
upper_result = [ word.upper() for word in str1.split(" ")]
print("Upper case list:",upper_result)        #Upper case list: ['WE', 'ARE', 'LEARNING', 'PYTHON', 'PROGRAMMING']

output = " ".join(upper_result)
print("output:",output)                  #output: WE ARE LEARNING PYTHON PROGRAMMING
# Split the word with space , Convert to upper case , join works only on entire result

# List comprehension with if else condition
#If we have if else condition , then write in the left most of the loop

lista = [5,7,8,2,1,6]
#To get output =[(5,"odd"),(7,"odd"),(8,"even"),(2,"even"),(1,"odd"),(6,"even")]

output = [(val,"even") if val%2==0 else (val,"odd") for val in lista]     # Simple if condition , if else can be used
print("Output:",output)

#get even length word
# If we have only if condition then write it to the right most of the loop
word_list = ["WE","ARE","LEARNING","PYTHON","PROGRAMMING"]
result = [word for word in word_list if len(word)%2 == 0]
print("Result :" ,result)       #Result : ['WE', 'LEARNING', 'PYTHON']











