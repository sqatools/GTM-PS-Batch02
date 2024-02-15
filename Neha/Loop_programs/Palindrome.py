##Python program to check whether any given number is a palindrome.


number = int(input("enter the number:"))
reverse_number = str(number)[::-1]
print(reverse_number)


if int(reverse_number) == number:
    print("Palindrome Number")
else:
    print("Not palindrome number")

##Python program to check if any given string is palindrome or not.
##Input: ‘jaj’
##output = palindrome
str = input("enter the text:")
reverse_str = str[::-1]


if (reverse_str) == str:
    print("Palindrome string")
else:
    print("Not palindrome string")