## Program: write a python get below result

str1 = "Python"
list1 = [4, 6, 8, 2, 9, 10]
#output = {'PP' : 4, 'yy' : 6, 'tt' : 8, 'hh': 2, 'oo': 9, 'nn' : 10}

list2= list(str1)
print(list2)
output_dict={}

for i in range (len(list2)):
    output_dict[(list2[i])*2] = list1[i]
print(output_dict)


#String into dictionary
car = "'make':'BMW','model':'1100','Year':'2010'"
# output ={ 'make':'BMW','model':'1100','Year':'2010' }

car_dict = {}

# Split the string by comma and iterate over each key-value pair
for pair in car.split(","):
    # Split each pair by colon
    key, value = pair.split(":")
    # Remove extra spaces and single quotes
    key = key.strip().strip("'")
    value = value.strip().strip("'")
    # Add key-value pair to the dictionary
    car_dict[key] = value

print(car_dict)