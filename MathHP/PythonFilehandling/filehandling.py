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

# read_file(r"E:\PythonTest.txt")
# read_file(r"D:\Hello.txt")

# If the file is available on current location, then we can provide file name
# If the file is available on some other loaction, then we have to provide the file path

# Write content to the file
# 1) If the file is already available to write content

def write_content_one(filename,content):
     file = open(filename,"w")                        # write
     file.write(content)
     file.close()

#write_content_one("write_data","Trying to write content to the file")             # override the existing file write_data is the filename

# 2) If the file does not exist : in this case it will create new file with the name provided and add contents to the file

#write_content_one("write_newfile_data.txt","India is the best")    # Create the new file

########################### Write content to the file with Append Mode ##############################

def append_content(filename,content):
     file = open(filename,"a")
     file.write(content)
     file.close()

# File already exist: In case if file is already availble, then the data will be added at the end of the file

#append_content("append_data_txt","Java is in OOPs")

# File does not exists: In this case, it will create new file with the name provided and add content to the file

#append_content("append_newfile_data.txt","We are learning Python")  # automatically creates new file

############################### Checkfile file status #########################

def check_file_status(filename):
     file = open(filename,"r")
     print("File is open:",file.closed)
     print("File mode:",file.mode)
     print("File name:",filename)
     file.close()
     print("File is open:", file.closed)

#check_file_status("test_data")

# File is open: False
# File mode: r
# File name: test_data
# File is open: True


##################### Context manager #####################
# context manager : It has its own enter and exit method internally
# so no need to close the file explicitly

def read_content_with_context_manage(filename):
     with open(filename,"r") as file:                           # with and as , after as is the keyword for context manager
          data = file.read()                                   # file can be anyname
          print(data)
          print("File is closed:",file.closed)               # context manager is for read, write and append as well

     print("File is closed:",file.closed)

#read_content_with_context_manage("test_data")

# File is closed: False
# File is closed: True

# always if the file is opened we have to close it
# orelse use context manager so that it will be closed automatically

################################## Different ways of read content ###########################

# read specific number of characters

def num_of_char(filename,num_char):
     with open(filename,"r") as file:
          data = file.read(num_char)
          print(data)

num_of_char("test_data",10)


# read specific number of lines, all lines

def read_num_lines(filename,num_line):
     with open(filename,"r") as file:
          for i in range(num_line):
               line = file.readline()
               print(line)


#read_num_lines("test_data",4)
#read_num_lines("test_webfile.html",4)

# read specific line from the file

def read_specific_line(filename,line_num):
     with open(filename,"r") as file:
         file_lines = file.readlines()
         print(file_lines)
         print(file_lines[line_num-1])             # 3rd line , index 2  3.hope you are doing good

#read_specific_line("test_data",3)






