# 3.  write a python program to find out all the emails ids from file
# def find_email_id(filename):
#     with open(filename,"r") as file:
#         words = file.read().split()
#
#     #find the email id's
#     for word in words:
#         if "@" in word:
#             print(word)
#         else:
#             continue
#
# find_email_id("first_file_3.txt")

#from the paragraph find the email_id's

def find_emails_pargrapgh(filename):
    with open(filename,"r") as file:
        word_list=file.read().split()

    #find email id's
    for email in word_list:
        if "@" in email:
            print(email)
        else:
            continue

find_emails_pargrapgh("first_file_3_2.txt")