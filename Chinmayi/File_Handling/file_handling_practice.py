def read_file(filename):
    file = open(filename,"r")
    data = file.read()
    print(data)

#read_file("testdata1.txt")
read_file(r"E:\pythonfilehandlingtext.txt")
