############################### Pending #############


import os
import shutil
import sys

# Get current working directory

print("Current working directory:",os.getcwd())   #Current working directory: E:\PythonSeleniumTraining\GTM-PS-Batch02\MathHP\OS_Module
                                                 #import os

# Get environment value

print("path environment: ",os.getenv("path"))
#path environment:  C:\Python312\Scripts\;C:\Python312\;C:\Program Files\Common Files\Oracle\Java\javapath;C:\windows\system32;
# C:\windows;C:\windows\System32\Wbem;C:\windows\System32\WindowsPowerShell\v1.0\;C:\windows\System32\OpenSSH\;D:\Program Files\Git\cmd;
# C:\Program Files\Apache\apache-maven-3.9.6\bin;C:\Program Files\Apache\apache-maven-3.9.6\bin;;C:\Program Files\Docker\Docker\resources\bin;
# C:\Program Files\nodejs\;C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\130\Tools\Binn\;
# C:\Program Files (x86)\Microsoft SQL Server\140\Tools\Binn\;C:\Program Files\Microsoft SQL Server\140\Tools\Binn\;
# C:\Program Files\Microsoft SQL Server\140\DTS\Binn\;C:\Program Files (x86)\Microsoft SQL Server\160\DTS\Binn\;
# C:\Program Files\Azure Data Studio\bin;C:\Users\madha\AppData\Local\Microsoft\WindowsApps;C:\Users\madha\AppData\Roaming\npm;
# C:\Program Files\JetBrains\PyCharm Community Edition 2023.3.2\bin;;C:\Program Files\Azure Data Studio\bin;
# C:\Program Files\Azure Data Studio\bin

print("Browser environment:" ,os.getenv("BROWSER"))        #Browser environment: None

print("Python version:",os.getenv("python_version"))      #Python version: None

data_list = os.listdir(r"D:\\softwares")
print(data_list)                 #######################################################

#for data in data_list:
#print(data)                          ##################

# Create folder directory on target location
#os.mkdir(r"filesdata")            ##################################################

#remove folder from target loaction
#os.remove()

##### Check given path exists or not ####

result  = os.path.exists(r"filesdata")          #######################
#print("result:",result)

result2  = os.path.exists(r"D:\\fold1\\fold2\\fold3")          #######################
print("result2:",result2)


########################Path operations ##########
# combine two path
path1 = r"D:\Hello.txt"
path2 = r"D:\path2.txt"
file_path = os.path.join(path1,path2)
#print(file_path)

#print("is file:",os.path.isfile(file_path))

# check path is file or folder
#print("is file:",os.path.isfile(file_path))

#check for folder

folder_path = ""
#print("is folder:",os.path.isdir(folder_path))

########## Copy files from source to destination

src_location = " "
tar_location = " "

#shutil.copy(src_location,tar_location)

############### execute local and cmd command

# os.system("notepad.exe")
# os.system("control")
# os.system("appwiz.cpl")

os.system("dir")

##### Get size of file ####

file_size = os.path.getsize("folder1")
print("file size:",file_size)

modify_time = os.path.getmtime("folder1")
print("modify time:",modify_time)

################### Create directory structure

os.makedirs(f"D:\\fold1\\fold2\\fold3")

# It will create all the directories in the entire path structure

###

print(sys.platform)                # import sys
print(sys.version_info)

#### get cpu count

print("cpu count:",os.cpu_count())

## rename folder directory

os.rename("folder1","folder1_updated")

