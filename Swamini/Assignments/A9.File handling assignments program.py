#1). Python Program How to read a file in reading mode.
"""file = open ("C:\pythonseleniumtraining\GTM-PS-Batch02\Swamini\File Handling\myy1.txt","r")
data=file.read()
print(data)
file.close"""

"""def fileread(filename):
    file=open(filename,"r")
    data=file.read()
    print(data)
    file.close()
fileread("C:\pythonseleniumtraining\GTM-PS-Batch02\Swamini\File Handling\myy1.txt")"""

#2).Python file program to overwrite the existing file content
"""def openfile(filename):
    file=open(filename,"w")
    file.write("this file is overwrite")
    file.close()
openfile("sfile.txt")"""

#3). Python file program to append data to an existing file.
"""def appendfile(filename):
    file=open(filename,"a")
    file.write(". i append this file")
    file.close()
appendfile("sfile.txt")"""

#4). Python file program to get the file’s first three and last three lines.
"""def lines(filename):
    file=open(filename,"r")
    filelist=file.readlines()
    for i in (filelist[:3]):
        print(i)
    for i in (filelist[-3:]):
        print(i)
lines("sfile.txt")"""

#5). Python file program to get all the email ids from a text file.
elist=[]
file=open("sfile.txt","r")
data=file.read()
word_list=data.split(" ")
for word in word_list:
    if "@" in word:
        elist.append(word)
    else:
        continue
print(elist)
file.close()



