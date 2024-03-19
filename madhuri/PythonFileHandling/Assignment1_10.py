"""
1). Python Program How to read a file in reading mode.
"""
import random


def read_file_data(filename):
    file = open(filename, 'r')
    data = file.read()
    print(data)


#read_file_data("test.txt")

"""
2. Python file program to overwrite the existing file content.
"""
def overwrite_file_content(filename):
    file = open(filename,'w')
    data = ("Line1 : This is India. \n Line2 : This is America. \n Line3 : This is Canada. \n Line4 : This is Australia. \n Line5 : This is China.")
    file.write(data)
    file.close()


# overwrite_file_content('test2.txt')

"""
3). Python file program to append data to an existing file.
"""

def append_file_data(filename):
    file = open(filename, 'a')
    data = '\n this is test data, which will append to an existing file'
    file.write(data)
    file.close()


# append_file_data("test2.txt")

"""
4). Python file program to get the file’s first three and last three lines.
"""

def get_filedata_by_line(filename):
    file = open(filename, 'r')
    data = file.readlines()

    for i in data[:3]:
        print("First Three: ", i)

    for i in data[:3]:
        print("Last Three: ", i)


#get_filedata_by_line("test2.txt")


"""
5). Python file program to get all the email ids from a text file.
"""

def get_emails_from_textfile(filename):
    with open(filename, "r") as file:
        data = file.read()
        words = data.split(" ")
        #print(words)
        emails = []
        for word in words:
            if '@' in word:
                #strip: Remove spaces at the beginning and at the end of the string
                emails.append(word.strip())
    print(emails)

#get_emails_from_textfile("test2.txt")

"""
6). Python file program to get a specific line from the file.
"""

def get_specificline_file(filename,lineno):
    with open(filename, "r") as file:
        data = file.readlines()
        print(data)
        #lineno-1 : bcz indices start from zero to manage index we did -1
        specific_line = data[lineno-1]
        print(specific_line)


# get_specificline_file("test2.txt", 3)

"""
7). Python file program to get odd lines from files and append them to separate files.
"""

def get_odd_lines(filename):
    with (open(filename, "r") as file):
        data = file.readlines()
        result = [data[i] for i in range(len(data)) if i % 2 == 0]
        #print(result)
        with open('test3.txt', 'w') as filew:
            for data in result:
                filew.write(data)


#get_odd_lines('test2.txt')

"""
8.Python file program to read a file line by line and store it in a list.
"""

def read_file_lineby(filename):
    data_list = []
    with open(filename,'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            data_list.append(line)
        print(data_list)


#read_file_lineby("test2.txt")

"""
9.Python file program to find the longest word in a file.
"""

def longest_word_in_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
        print(data)
        max_count = 0
        max_word = ''
        wordList = data.split(" ")
        for word in wordList:
            if len(word) > max_count:
                max_count = len(word)
                max_word = word
        print("longest Word: ", max_word)


#longest_word_in_file("test2.txt")

"""
10. Python file program to get the count of a specific word in a file.
"""

def get_count_word(filename,search_word):
    with open(filename, "r") as file:
        data = file.read()
        wordList = data.split(" ")
        count = 0

        for word in wordList:
            print(word,'=',search_word)
            if word == search_word:
                count = count + 1
        print("Word Count: ", count)


#get_count_word("test2.txt",'madhuri')

"""
11. Python file program to read a random line from a file.
"""
import random
def read_random_line(filename, lineno):
    with open(filename, "r") as file:
        lines = file.readlines()
        # Read data from the file and splitting it into lines
        data = random.choice(lines)
        print(data)


read_random_line('test2.txt',3)

"""
12). Python file program to copy the file’s contents to another file after converting it to lowercase.
"""

def convert_lowercase(filename):
    with open(filename, "r") as file:
        data = file.read()
        print(data)


convert_lowercase('test2.txt')