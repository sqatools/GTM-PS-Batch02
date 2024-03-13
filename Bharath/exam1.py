"""list1 = [2, -16, 6, 44, -71, 18, -11, -1]
print("The original list is : " + str(list1))
res1 = []
res2 = []
for i in list1:
    if (i > 0):
        res1.append(i)
    else:
        res2.append(i)
res1.sort()
res2.sort()
res1.extend(res2)

print("Result after performing sort operation : " + str(res1))
"""

str1 ="India is best cricket Team in the World"
print(len(str1))
words = str1.split(" ")
for i in range(0, len(words)):
    for j in range(i + 1, len(words)):
        if words[i] == (words[j]):
            print(words[i])


            str = input("Enter a String: ")

            word_list = str.split()

            longest_word = max(word_list, key=len)

            pos = str.index(longest_word)

            print("Longest word: ", longest_word)
            print("Position of Longest word: ", pos)