# 2.  write a python program to find out all the mobile numbers from file.
# 3.  write a python program to find out all the emails ids from file.


def find_mobile_no(filename):
    with open(filename,"r") as file:
        words = file.read().split()
        mobile_no = []

    #find the mobile no
    for num in words:
        if num.isnumeric() and len(num)==10:
            mobile_no.append(num)
    print(mobile_no)

find_mobile_no("first_file_2.txt")



