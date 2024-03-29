#21). Python program to check whether the given list is palindrome or not. (should be equal from both sides).
# list20 = [1,2,3,4,32,2,1]
#
# rev_list20 = list20[-1::-1]
#
# if list20 == rev_list20:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#22). Python Program to get a list of words which has vowels in the given string.
Input = "www Student ppp are qqqq learning Python vvv"
#Output : [‘Student’, ‘are’, ‘learning’, ‘Python’]

output_list22 = [ ]
list_22 = Input.split(" ")
print (list_22)

for  words in list_22:
    for char in words:
        if char == 'a'or char == 'e'or char == 'i'or char == 'o'or char == 'u':
            output_list22.append(words)
            break
print(output_list22)

#23). Python program to add 2 lists with extend method.
lista = [4, 5, 7, 9, 2, 1]
listb = [2, 5, 8, 3, 4, 7]

lista.extend(listb)
print(f"Extended list: {lista}")
