
# # ways to create a string variable
# l ='single' # we can declare a string by using  '' single quotes
# h = "double" # we can declare a string by using "" double quotes
# f=str('hello') # we can decalre a string by useing 'str' string function within a single quotes
# d=str("welcome")## we can decalre a string by useing "str" string function within a Double quotes
#
# print(l,h,f,d)
# print(type(l))
# print(type(h))
# print(type(f))
# print(type(d))
from itertools import count

# # creating a empty string
# name1='' # by using single quote we can declare a  empty string variable
# name2="" # by suing a double quotes we can declare a empty string variable
# name3=str # by using a str string function we can declare a empty string variable


#----->>>>..Important for interview question
# is String is mutable or immutable?
# mutable means we can change the values of the variables
# immutable means we cannot change the values of the variables
#
#
# str1="welcome"
# print(id(str1)) # id of str1 3048916166016
# str1=str1+"to python"
# print(id(str1))# id of str1 1725027116784
#
# #->>> If the value is changed after updation then it is called immutable

#-->>>>(very Important) + and * with string
# + we can used this symbol as a airthemetic addition operator
#if we are using + by using strings it will joint two strings
# * this mutipication will multipy the variable and gives output



# # str="welcome"
# # print(str+"to python programming") # here + symbol concatinating two strings
#
# str="hello"
# print(str+"python")# Concatinate two strings it will gives output as hellopython
# print(str*5) # it will gives 5 output as hellohellohellohellohello

#--->>Very Important [slicing Index]
#Slice index will cut extracting a postion
# index starts with 0 left to right forward
# ending with -1  right to left  forward

# str = "welcome"
# print(str[0:1])
# print(str[:2])
# print(str[::2])#Taking every 2nd character from index 0 → w, l, o, e
# print(str[1:7])
# print(str[0:-1])

#Imp >>>> Example of ord() and chr()
#ASCII stands for American Standard Code for Information Interchange.
# It is a character encoding standard where each character (letters, digits, symbols) is represented by a numeric value.

# print(ord("A"))#ord(character) → Converts a character to its ASCII number.

# print(chr(65)) #chr(number) → Converts an ASCII number back to a character


# Examples of max(),min(),len()of string functions
# for albhabet a count is one Z count is 26 based on that it will print char values
# print(max("abc"))# it will print the maximum charcter of string
# print(min("lokesh")) # it will print the minimum charcter of the string
# print(len("this is my python code")) # it will print length of the string

#Imp>>>>>> in, not in operators in string -> it will return true or false
#01 in

# s = "welcome"
# print("come" in s)# it will check if the "come" is avilable in "s" string it gives true as output if not false

#02 not in
# Checks if a substring is NOT present in a string.
# Returns True if the substring is absent, otherwise False.

# y= "python"
# print("java"not in y)# here the substring  java is not presented in  string "y" thats why it gave output as # true
# print("th" not in y)# here the substring "th: is presented in string "y" thats why we got output as # false
#
# # IMP>>>> String comparisons
# print("teeth" =="tee") # false
# print("show" != "luck") # True
# print("lokesh">= "loki")#false
# print("chandra"<="loki")# true
# print("indu sai" > "indu")#true
# print("lokesh" < "loki") # false
# print('lokesh' > "")# true

# #imp>>>> testing strings -> these strings will gives as true/false
#
# s= "hello python code "
# print(s.isalnum())
# # print(s.upper())
# # print(s.lower())
# # print(s.isupper())
# # print(s.islower())
# # print(s.isspace())
# # print(s.isdigit())
# # print(s.isidentifier())
#
# #imp>>>> serching for substring
# x= "this is my first company"
# print(x.startswith("char"))#false
# print(x.endswith("any"))# true
# # print(x.find("is"))
# print(x.find("lucky"))# -1 if substring is not presented in string it will print output as -1.
# print(x.count("i"))# returns subcount of i
#
#>>> Converting strings
# Problem statement:  Convert String to Other Data Types
# To Integer: int("123")
# To Float: float("45.67")
# To Boolean: bool("True")

# # Example 1 for
# s = "123"
# num = int(s)
# print(num)
# print(type(num))
# s2 = "45.67"
# num2 = float(s2)
# print(num2)
# print(type(num2))

# example 02
#
# r=" Infosys"
# print(r.capitalize()) #capitalization is nothing but sentence format
# print(r.upper())#
# print(r.lower())
# print(r.title())# every first charcter of word will convert into capital letters and gives as output
# print(r.swapcase())#swap case is converting lower case into camel letters, camel into lower case letters
# print(r.replace("sys", "hi"))# it will replace old string 'hello' and updated as 'hi'
#
# # vvimp>>>>> Reverse string
# method one is by using for loop
# method two is by using slicing operator
# Using reversed() and join()
#
# # Approach -01
# s = " welcome"
# rev_str = ""
# for i in s:
#     rev_str=i+rev_str
# print("reverse string is:", rev_str)


#Approach -02
#
# x = "hello"
# rev_str=x[::-1]#[::-1]
# # here [: starting],[:ending] [-1 is the decrement] here i dint mentioned indexx by defualt : collan
# # will take
# print(rev_str)

# # Approach _03
# # Using reversed() and join()
# s = "love"
# rev = "".join(reversed(s))
# print(rev)  # Output: evol


#example _02

# problem reverse mentioned string and print in two different way
# " infosys"

# Approach _01 solution
# l = "infosys"
# rev_str =l[::-1]
# print(rev_str)


# # approach_02 solution
# m = "infosys"
# rev_str=""
# for i in m:
#     rev_str=i+rev_str
# print("reverse string is :",rev_str)
