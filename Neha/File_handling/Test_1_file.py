"""

1). Python Program How to read a file in reading mode.

2). Python file program to overwrite the existing file content.

3). Python file program to append data to an existing file.



5). Python file program to get all the email ids from a text file.

6). Python file program to get a specific line from the file.

7). Python file program to get odd lines from files and append them to separate files.

8). Python file program to read a file line by line and store it in a list.

9). Python file program to find the longest word in a file.

10). Python file program to get the count of a specific word in a file.

11). Python file program to read a random line from a file.

12). Python file program to copy the file’s contents to another file after converting it to lowercase.

13). Python file program to copy the file’s contents to another file after converting it to uppercase.

14). Python file program to count all the words from a file.

15). Python file program to sort all the lines File as per line length size.

16). Python file program to consider a text file as a DB file and store all the student information in a text file.

17). Python file program to create n number of text files with given strings.

18). Python file program to generate text files with all alphabets.  e.g. A.txt , B.txt, C.txt….. Z.txt

19). Python file program to get all odd and even length words in two lists.

20). Python file program to get all mobile numbers from a file. e.g each mobile number size should be 10.
"""
#4). Python file program to get the file’s first three and last three lines.

def first_three_lines(filename):
    with open(filename,"r") as file:
        filedata = file.readlines()
    #first three
    lines = filedata[:3]
    for line in lines:
        print(line)

first_three_lines("file_practice_data.txt")

# def last_three_lines(filename):
#     with open(filename,"r") as file:
#         filedata = file.readlines()
#
#     #last three lines
#     lines = filedata[-3:]
#     print(lines)
#
# last_three_lines("file_practice_data.txt")

#6). Python file program to get a specific line from the file.

# def specific_line(filename):
#     with open (filename,"r" ) as file:
#         filedata = file.readlines()
#
#     #specific text
#     print("perticular text:", filedata[5] )
#
# specific_line("file_practice_data.txt")

#7). Python file program to get odd lines from files and append them to separate files.

# def odd_lines(filename):
#     with open(filename,"r") as file1:
#         filedata1 = file1.readlines()
#
#     with open (filename,"w") as file2:
#
#     #
#     for lines in range (1,(len(filedata1))
#         if lines[] % 2 == 0:
#             file2.write(filedata1[lines])
#         print("file2 content:",file2)
#
# odd_lines("file_practice_data.txt")

