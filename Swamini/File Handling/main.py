"""import json

def read_json_data(filename):
    with open (filename,"r") as file:
        file_data=file.read()
        data =json.loads(file_data)
        return data
output = read_json_data("textdata.json")
print("name:", output["name"])
print("address:", output["address"])"""

"""def position(filename):
    with open (filename,"r") as file:
        file.seek(5,0)
        data =file.read()
        print(data)
        print("position of file:",file.tell())
position("myy1.txt")
"""


def read_file_content_seek(filename):
    with open(filename, "r") as file:
        # set cursor at 30 char
        # file.seek(30,  0) : set cursor from begining of file
        # set cursor from end of file
        # file.seek(-50, 2)
        print("cursor position :", file.tell())
        print("20 char :", file.read(20))
        file.seek(20, 1)
        print("cursor position :", file.tell())


read_file_content_seek("myy1.txt")

pop open


