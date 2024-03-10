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

read_file(r"E:\PythonTest.txt")
read_file(r"D:\Hello.txt")


