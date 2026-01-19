# how to call funtions through another module
# Importing modules through import and module name
# her iam calling calculator modules in operations module.
# # Approach-01
# import Calculator # by using "import" key word and "module name" we can access modules
# Calculator.add(200,100)#300# calling function through "modulename"."functionname"
# Calculator.mul(12,5)#60 # calling function through "modulename"."functionname"

# Approach-02>> If we have multiple functions and call only specfic method according our requirement.
# Problem statement: from Calculator import add and div
#
# from Calculator import add,div
# add(100,200)#300
# div(10,2)#5.0

# Approach-03: If you have so many functions and calssess if you want to print all the functions and classes inside module
# By using # import *(Star) we can access all the functions and classes

from Calculator import *
add(100,150)#250
sub(50,25)#25
mul(10,20)#200
div(20,5)#4.0
