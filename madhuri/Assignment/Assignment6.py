"""
Input str1 = "Hello Good Morning"
Output = gello Good MorninH
"""

str1= "Hello Good Morning"

start_letter = str1[0]
end_letter = str1[-1]

# print( str1[1:-1]) # start from 1 end at -ve index -1

result_string = end_letter + str1[1:-1] + start_letter
print("Question 1: ", result_string)
print("_"*100)
