"""
tell() : This method return the current position of the cursor
seek() : This method help to set the cursor location to read the content of file
"""

def read_content_with_tell(filename):
     with open(filename, "r") as file:
          print("current location of the cursor :", file.tell())
          char_20 = file.read(20)
          print("first 20 character :", char_20)
          print("current location of the cursor after 20 char :", file.tell())
          char_40 = file.read(40)
          print("40 characters :", char_40)
          print("current location of the cursor after 40 char :", file.tell())

#read_content_with_tell("test_data.txt")
#read_content_with_tell(r"E:\Filesdata\employee_details.txt")
"""
seek(50, 0) : This means 50 char movement from begining file
seek(30, 1) : This means 30 char movement from current position of the cursor
seek(-40, 2) : This means 40 character movement from end of the file in reverse order.
"""

def read_file_content_seek(filename):
     with open(filename, "rb") as file:
          # set cursor at 30 char
          # file.seek(30,  0) : set cursor from begining of file
          # set cursor from end of file
          #file.seek(-50, 2)
          print("cursor position :",file.tell())
          print("20 char :", file.read(20))
          file.seek(20, 1)
          print("cursor position :",file.tell())


read_file_content_seek("test_data.txt")

