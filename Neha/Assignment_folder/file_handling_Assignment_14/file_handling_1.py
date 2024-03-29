# Home work:
# 1.  write a python program to find the longest word from file.
#When having single line in any files
def longest_word_file(filename):
    with open(filename,"r") as file:
        filedata = file.read()
    #Longest word
    filedata_1 = filedata.split(" ")
    longest_word = max(filedata_1, key = len)
    print(longest_word)

longest_word_file("first_file_1.txt")

#when we have paragraph in any files

def find_largest_word(file_name):
    with open(file_name, 'r') as file:
        words = file.read().split()
        largest_word = max(words, key=len)
    print(largest_word)

find_largest_word("first_file_1_2.txt")
