"""
File handling programs
a)Longest word from file
b)All mobile number
c)All email id
"""

"""
a)Longest word from file
"""
def longest_word_in_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
        max_count = 0
        max_word = ''
        wordList = data.split()
        for word in wordList:
            if len(word) > max_count:
                max_count = len(word)
                max_word = word
        print("a. longest Word: ", max_word)


longest_word_in_file(r"C:\PythonSeleniumTraining\GTM-PS-Batch02\madhuri\PythonFileHandling\\test2.txt")

"""
2.All mobile number
"""

def all_mobile_num(filename):
    with open(filename, 'r') as file:
        data = file.read()
        wordList = data.split()
        mobile_no = []
        for word in wordList:
            if word.isnumeric() and len(word) ==10:
                mobile_no.append(word)
    print("b. mobile no: ", mobile_no)


all_mobile_num(r"C:\PythonSeleniumTraining\GTM-PS-Batch02\madhuri\PythonFileHandling\\test2.txt")

"""
3.All email id
"""
def all_email_ids(filename):
    with open(filename, 'r') as file:
        wordList = file.read().split()
        print(wordList)
        email_ids = []
        for word in wordList:
            if '@' in word:
                email_ids.append(word)
    print("c. email ids: ", email_ids)


all_email_ids(r"C:\PythonSeleniumTraining\GTM-PS-Batch02\madhuri\PythonFileHandling\\test2.txt")
