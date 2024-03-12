# WAP to replace one word with another

def replace_word_file(filename,word1,word2):
    with open(filename,"r") as file:
        filedata = file.read()


    replaced_content = filedata.replace(word1,word2)
    with open(filename,"w") as file:
        file.write(replaced_content)

replace_word_file("replace_content.txt","JAVA","PYTHON")


# WAP to combine two files line and add in another file

def combine_two_files(file1,file2,file3):
    with open(file1,"r") as file1_obj:
        file1_lines = file1_obj.readlines()

    with open(file2,"r") as file2_obj:
        file2_lines = file2_obj.readlines()

    with open(file3,"a") as file3_obj:
        for i in range(len(file1_lines)):
            file3_obj.write(file1_lines[i])
            file3_obj.write(file2_lines[i])

    with open(file3,"r") as file3:
        print(file3.read())                           # for printing in the console along with file

#combine_two_files("file1_data.txt" , "file2_data.txt" ,"file3_data.txt")
combine_two_files("file1_data.txt" , "file2_data.txt" ,"file4_data.txt")

# HW

# 1) WAP to find longest word from file
# 2) WAP to find out all the mobile number from given file ### length is 10
# 3) WAP to find out all the email id from given file