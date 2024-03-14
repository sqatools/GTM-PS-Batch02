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
file_write("newfile5.txt","I am repeating the same task again and again")