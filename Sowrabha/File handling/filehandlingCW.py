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

#file_write(f"E:\\textfile5.txt","I am repeating the same task again and again")

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
line_specific("newfile.txt",3)

