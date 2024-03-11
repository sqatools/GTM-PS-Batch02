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
     file.close()

# if the file is available on current location then we provide file name
#read_file("test_data.txt")

# if the file is available on some other location, then we have to provide the file path
#read_file(r"E:\Filesdata\count_name.txt")
#read_file(r"E:\Filesdata\employee_details.txt")


# E:\Filesdata\count_name.txt
# E:\xpath.txt


# Write content to the file
# 1. If the file is already available to write content
# 2. If the file does not exist
def write_content_one(filename, content):
     file = open(filename, "w")
     file.write(content)
     file.close()


# file already exist : In this case the old data of the file will overwrite by new content.
# write_content_one("write_data.txt", "Trying to write content to the file")

# file doest not exist: In the case, it will create new file with the name provide
# and add content to the file.
# write_content_one(r"E:\write_newfile_data.txt", "India won the Test series against England")


##################### Write content to the file with Append mode ################

def append_content(filename, content):
     file = open(filename, "a")
     file.write(content)
     file.close()

# file already exist : In case if file is already available, then the data will be added at the end of the file
# append_content("append_data.txt", "India is the best country")

# file doest not exist : In case , it will create new file with the name provided and add content to the file.
# append_content("append_newfile_data.txt", "We are learning Python Programming")
# append_content("newfile_data.log", "We are learning Python Programming")


############################## Check file status ############

def check_file_status(filename):
     file = open(filename, "r")
     print("file is open :", file.closed)
     print("file mode :", file.mode)
     print("file name :", filename)
     file.close()
     print("file is open :", file.closed)


#check_file_status("test_data.txt")
"""
file is open : False
file mode : r
file name : test_data.txt
file is open : True
"""


##################### context manager ################
# context manager : context manager has its own enter and exist method internally.
# so no need to close the file explicitly
def read_content_with_context_manage(filename):
     with open(filename, "r") as file:
          data = file.read()
          print(data)
          print("file is closed :", file.closed) # file is closed : False

     print("file is closed :", file.closed)
     # file is closed : True


#read_content_with_context_manage("test_data.txt")


########################### Different read option #################

# read specific number of characters
def num_of_char(filename, num_char):
     with open(filename, "r") as file:
          data = file.read(num_char)
          print(data)


#num_of_char("test_data.txt", 10)


# read specific number of lines
def read_num_lines(filename, num_line):
     with open(filename, "r") as file:
          for i in range(num_line):
               line = file.readline()
               print(line)


# read_num_lines("test_data.txt", 4)
# read_num_lines("test_webfile.html", 5)


##### read specific line from the file ######

def read_specific_line(filename, line_num):
     with open(filename, "r") as file:
          file_lines = file.readlines()
          print(file_lines)
          print(file_lines[line_num-1])

read_specific_line("test_data.txt", 5)



