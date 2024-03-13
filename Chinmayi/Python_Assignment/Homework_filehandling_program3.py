# 3.  write a python program to find out all the emails ids from file.

def search_email_file(filename):
    with open(filename, "r") as file:
        filedata = file.read()
        email_id = []

    data1 = filedata.split(" ")
    for data in data1:
        if "@" in data:
            email_id.append(data)

    print(email_id)

search_email_file(r"C:\PythonseleniumTraining\GTM-PS-Batch02\Chinmayi\File_Handling\Test_data4.txt")