"""
Three modes to open file
read mode (r)
write mode (w)
append mode (a)
"""

def read_file(filename):
     file = open(filename, "r")
     data = file.read()
     print(data)


#read_file("test_data.txt")
#read_file(r"E:\Filesdata\count_name.txt")
read_file(r"E:\Filesdata\employee_details.txt")


# E:\Filesdata\count_name.txt
# E:\xpath.txt
