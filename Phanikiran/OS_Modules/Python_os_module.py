import os
import shutil
import sys

"""
# get current working
print("current working directory:", os.getcwd())

# get environment value
print("path environment :", os.getenv("path")) # list values available in path
print("BROWSER environment :", os.getenv("browser")) # chrome
print("Python version :", os.getenv("PythonVersion")) # 3.12

# get list all files and folder
data_list = os.listdir(r"E:\Filesdata")
print(data_list)

for data in data_list:
    print(data)

# create folder directory on target location
# os.mkdir(r"E:\Filesdata\GTM_batch03") # folder create succesfully
# os.mkdir("folder1") # create folder on current location
"""

##### remove folder from target location  ######
"""
os.rmdir(r"E:\Filesdata\GTM_batch03") # delete emtpy directory
os.rmdir(r"E:\Filesdata\new_dir") # can not delete the non empty directory
# We can delete non empty directory with shutil.rmtree
shutil.rmtree(r"E:\Filesdata\new_dir")
"""

##### check given path is exist or not ##########
"""
result = os.path.exists(r"E:\Filesdata\Bi15")
print("result :", result) # True

result2 = os.path.exists(r"E:\Filesdata\Bi16")
print("result :", result2) # False
"""

######### Path operations ##########
# combine two path
path1 = "E:\\Filesdata"
path2 = "BI13\\OS_Module\\Copied_file.txt"
file_path = os.path.join(path1, path2)
print(file_path)

# check path is file or folder
print("is file :", os.path.isfile(file_path))  # true

# check for folder
folder_path = "E:\\Filesdata\\BI14"
print("is folder :", os.path.isdir(folder_path)) # True

########### Copy files from source to destination ###########

src_location = "E:\\Filesdata\\Bi15\\file1.txt"
tar_location = "E:\\Filesdata\\Tavet\\file_copies.txt"

shutil.copy(src_location, tar_location)

####### execute local cmd command #########

#os.system("notepad.exe")
#os.system("control")
#os.system("appwiz.cpl")

# os.system("dir")

####### Get size of file ##########
"""
file_size = os.path.getsize("E:\\Filesdata\\Bi15\\file1.txt")
print("file size :", file_size)

modify_time = os.path.getmtime("E:\\Filesdata\\Bi15\\file1.txt")
print("modify time :", modify_time)
"""

######## create directory structure ######

# os.makedirs(f"E:\\Filesdata\\gmt_batch03\\folder1\\folder2")
# It will create all the directories in the entire path structure

######### get platform information with the help of sys module ####

print(sys.platform) # win32
print(sys.version_info)
# sys.version_info(major=3, minor=12, micro=2, releaselevel='final', serial=0)
print(sys.version) # 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]

### get cpu count ####
print("cpu count :", os.cpu_count())  # 8

## rename folder directory ####
os.rename("folder1", "folder1_updated")

