# 1.  write a python program to find the longest word from file.

def longest_word_in_file(filename):
    with open(filename, "r") as file:
        filedata = file.read()

    data = filedata.split(" ")
    long_word = max(data, key=len)
    print(long_word)

longest_word_in_file(r"C:\PythonseleniumTraining\GTM-PS-Batch02\Chinmayi\File_Handling\Test_data2.txt")