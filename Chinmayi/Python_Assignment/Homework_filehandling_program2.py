# 2.  write a python program to find out all the mobile numbers from file.

def search_mobile_number_file(filename):
    with open(filename, "r") as file:
        filedata = file.read()
        mobile_num = []

    data1 = filedata.split(" ")
    for data in data1:
        if data.isdigit() and len(data) == 10:
            mobile_num.append(data)

    print(mobile_num)

search_mobile_number_file(r"C:\PythonseleniumTraining\GTM-PS-Batch02\Chinmayi\File_Handling\Test_data3.txt")