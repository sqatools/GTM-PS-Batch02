
"""
str2 = "python"
result = ("_").join(str2)

str3 = ""


str4 = ""


  str5 = ""


"""


"""
str7 = "Add user extra properties @facebook mobile no 9986088630
          become part of the test admin@gmail.com are available at 434345"


word_list = str7.split(" ")
print(word_list)
for word in word_list:
  if word.isnumeric() and len(word) == 10:
    print()
  elif "@" in word:
    print(word)
  else:
      continue
"""

"""
#2 program to find longest word in the given string
str_input = "user properties become a part of the test report and are available in the configuration"
longest_word = ''
long_len = 0
word_list = str_input.split()
for word in word_list: #user, propeties, become
    word_len = len(word)

    if word_len > long_len:
        long_len = word_len
        longest_word = word
        print(long_len, longest_word, ":", word)
        print("Longest word:", longest_word)
"""




#write a program to get count of vowels from each word
str1 = "user properties just become part of the test"
# output = {"User": 2, "properties": 3, "become" : 2, "part" : 1, "of": 1, "test" : 1}

word_list = str1.split(" ")
vowels = "aeiou"
output = {} # initiate the dict
for word in word_list:
    count = 0
    for char in vowels:
        if char in word.lower():
            count += 1
        else:
            continue
            output[word] = count
            print("output:", output)



