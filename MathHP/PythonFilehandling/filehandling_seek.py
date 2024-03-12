"""
tell() : This method return the current position of the cursor
seek() : This method help to set the cursor location to read the content of the file

"""

def read_content_with_tell(filename):
    with open(filename,"r") as file:
        print("current location of the cursor:" ,file.tell())
        char_20 = file.read(20)
        print("first 20 character :",char_20)
        print("Current location of the cursor after  20 char :",file.tell())
        char_40 = file.read(40)
        print("40 characters :",char_40)
        print("Current location of the cursor after  40 char:",file.tell())

# read_content_with_tell("test_data")                               # If different package, then copy absolute path

# read_content_with_tell("E:\PythonTest.txt")

"""
seek(50,0): This means 50 char movement from beginning file in a forward way
seek(30,0): This means 30 char movement from current position in a forward way
seek(-40,0): This means 40 char movement from end of the file  in reverse order
"""

def read_file_content_seek(filename):
    with open(filename,"rb") as file:                # reverse order means rb binary read
        #file.seek(30,0)                            # set cursor at 30 char from beginning of file
        #file.seek(-50,2)                           # set cursor from end of file
        print("cursor position:",file.tell())     # 0 for beginning and 2 for ending
        print("10 char:",file.read(20))
        file.seek(20,1)                         # 0 and 1 for beginning
        print("cursor position:",file.tell())

read_file_content_seek("test_data")

#(30,0)     30 chars from beginning of file 0 is begin
#(30,1)     30 chars from current position of file 1 is begin
#(30,2)     30 chars from end position of file 2 is end

