# HW

# 1) WAP to find the longest word from file
# 2) WAP to find out all the mobile number from given file ### length is 10
# 3) WAP to find out all the email id from given file

######################################

# 1) WAP to find the longest word from file

def longest_word_file(filename):
    file = open(filename,'r')
    word = file.read().split(" ")
    longest_word= max(word,key=len)
    print("Longest word in the file is :" ,longest_word)
    print("Length of the Longest word in the file is :" ,len(longest_word))

#longest_word_file("fileassignment.txt")

# 2) WAP to find out all the mobile number from given file ### length is 10

def mobile_number(filename):
    file = open(filename,'r')
    word_list = file.read().split(" ")
    for word in word_list:
        if word.isnumeric() and len(word) == 10:
            print("Mobile number :", word)

#mobile_number("fileassignment.txt")


# 3) WAP to find out all the email id from given file

def email_file(filename):
    file=open(filename,'r')
    word_list = file.read().split(" ")
    for word in word_list:
        if "@" in word:
            print("Email:" ,word)

email_file("fileassignment.txt")





