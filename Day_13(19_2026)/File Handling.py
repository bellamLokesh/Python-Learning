
# Note: Change file path with local machine path

# # Ex-01: Writing data into text file
# # pre requisites this pc->osdisk-C-> Create new folder as demo file-> Create empty notepad name it as "File.txt"
# from os import close
#
# file= open("C:/demofile/File.txt","w")#open # take file path # is defalut # "w" is used to write
# file.write("This is my first statement...\n")#\n is used to print output in line by line
# file.write("This is my second statement...\n")
# file.write("This is my third statement...\n")
# file.write("This is my fourth statement...\n")
# file.write("This is my fifth statement...\n")
# file.close()
# print("program is completed")
#
# # #Ex-02> read data from text file

# file= open("C:/demofile/File.txt","r")#open # take file path # is defalut # "r" is used to read the data in file
# # print(file.readlines())# it will print all lines in single line
# # print(file.read())# it will print all lines in sequance
# # # print(file.readline())# it will print only first line
# file.close()
# print("program is completed")
#
# #Ex-03> Appending data into text file
file = open("C:/demofile/File.txt", "a")# "a" is for append by using append we can add statements previously we have five statements
file.write("\n This is my six statement \n")# here iam write again two statements
file.write("\n This is my seventh statement \n")
file.close()
print("program is completed")