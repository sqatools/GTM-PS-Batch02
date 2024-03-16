def file_read(filename):
    file=open(filename,"r")
    data=file.read()
    print(data)

#file_read("newfile.txt")
#file_read("C:\learn\Againfile.txt")

def file_write(filename,content):
    file=open(filename,"w")
    file.write(content)
    file.close()

#file_write("newfile.txt","I am repeating the same task again")
#file_write("newfile5.txt","I am repeating the same task again and again")

file_write("F:\\Newfolder\\textfile6.txt","I am repeating the same task again and again")

# def file_append(filename,content):
#     file=open(filename,"a")
#     file.write(content)
#     file.close()
# file_append("newfile.txt"," I will practice")
# file_append("C:\\ newfile6.txt"," I will practice")

#to check the sttaus

def check_status(filename):
    file=open(filename,"r")
    print("file is open:",file.closed)
    print("file mode:",file.mode)
    print("filename is:",file.name)
    file.close()
    print("file status is open",file.closed)
#check_status("newfile.txt")

#####################context manager#####################

# def context_manager(filename):
#     with open(filename,"r") as file:
#         data=file.read()
#         print(data)
#         print("file is open", file.closed)
#     print("file is closed",file.closed)
#
# context_manager("newfile.txt")

#########################read character######################################
def read_char(filename,num_char):
     with open(filename,"r")as file:
        data=file.read(num_char)
        print(data)
#read_char("newfile.txt",10)


###################read line####################3

def read_line(filename,num_line):
    with open(filename,"r")as file:
        for i in range (num_line):
          line=file.readline()
          print(line)
#read_line("newfile.txt",4)

#####read specific no of lines#####################

def  line_specific(filename,num_line):
    with open(filename,"r")as file:
        line=file.readlines()
    print(line)
    print(line[num_line-1])
#line_specific("newfile.txt",3)


#######find the current position tell() #############
def cursor_position(filename):
     with open(filename,"r")as file:
         print("Current postion of th cursor",file.tell())
         char_20= file.read(20)
         print("first 20 character:",char_20)
         print("current cursor position after 20",file.tell())
         char_40= file.read(40)
         print("40 characters after 20:",char_40)
         print("cureent cursor position after 40",file.tell())
#cursor_position("newfile.txt")


##########################Seek()############################
def cursor_current_position(filename):
    with  open(filename,"r")as file:
          file.seek(30,-0)
          print("cursor current position:",file.tell())
          print("char_20:",file.read(20))
          print("cursor position after 20:",file.tell())
#cursor_current_position("newfile.txt")

##############seek () end of the file#############
def cursor_current_position(filename):
    with open(filename,"rb")as file:
          file.seek(-50, 2)
          print("cursor current position:",  file.tell())
          print("char_20:",file.read(20))
          print("cursor position after 20:", file.tell())

#cursor_current_position ("newfile5.txt")

#############Seek() mid value###################
def read_file_content_seek(filename):
    with open(filename, "rb") as file:
        # set cursor at 30 char
        # file.seek(30,  0) : set cursor from begining of file
        # set cursor from end of file
        # file.seek(-50, 2)
        print("cursor position :", file.tell())
        print("20 char :", file.read(20))
        file.seek(20, 1)
        print("cursor position :", file.tell())


#read_file_content_seek("newfile.txt.")
###################Json program#####
import json
def json_file_read(filename):
    with open(filename,"r")as file:
        file_data=file.read()
        data=json.loads(file_data)
        print(data)
#json_file_read("newfile1.json")

# *******************************************************************************

import json
def write_content_json_file(filename, content):
    with open(filename, "w") as file:
        # dumps method convert the dictionary data into json string
        json_data = json.dumps(content)
        file.write(json_data)

company = {
    'IT': [
        {'name': 'sanjay', 'email': 'sanjay@gmail.com', 'phone': 5654645, 'address': 'mumbai'},
        {'name': 'Neha', 'email': 'neha@gmail.com', 'phone': 434343, 'address': 'Pune'},
        {'name': 'Saumya', 'email': 'Saumya@gmail.com', 'phone': 33333232, 'address': 'Bangalore'},
    ],
    'HR': [
        {'name': 'priyanka', 'email': 'priyanka@gmail.com', 'phone': 8767657, 'address': 'Chennai'},
        {'name': 'swamini', 'email': 'swamini@gmail.com', 'phone': 98978998, 'address': 'Indore'},
        {'name': 'Bharath', 'email': 'Bharath@gmail.com', 'phone': 2332423432, 'address': 'Bhopal'},
    ]
}
write_content_json_file("new_json_content.json", company)







