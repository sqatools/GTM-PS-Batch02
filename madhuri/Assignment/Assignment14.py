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
        wordList = data.split(" ")
        for word in wordList:
            if len(word) > max_count:
                max_count = len(word)
                max_word = word
        print("longest Word: ", max_word)


longest_word_in_file(r"C:\PythonSeleniumTraining\GTM-PS-Batch02\madhuri\PythonFileHandling\\test2.txt")

"""
"""