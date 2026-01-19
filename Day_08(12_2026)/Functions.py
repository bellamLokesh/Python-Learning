#-01>>> Creating Function
#Ex-01>>>
# def myfun():#  here i declared a myfun by using def key word ,
#     # : collon should be mandatary after delcaring a function.
#     print("hello")
# myfun()#hello # by calling function name only we will get output

#Ex-02>> creating a function by adding single parameters
# def myfun(name):# here i passed a name paramenter ,single parameter
#     print("hello",name)
# myfun("lokesh")#hello lokesh # by calling function we need to delclare a name

# # Ex-03>>> creating a function by adding multiple parameters
# # once we create a function we can call any number of times
# def cal(a,b):
#     return(a+b)
# print(cal(10,20))#30 # here by calling function and assigning values and storing values and printing print statements.
# sum=cal(100,200)# here i called function and assigning values and storing those values into sum variable
# print(sum)#300

#Ex-04>> Creating empty function calling empty function:
#
# def myfun():# empty function
#     return# by passing return we are expecting something even though we are not providing any values
# print(myfun())#None # see here it will reslut as none
#
# # same above example without passing return
# def myfun():# without passing any argument i created empty function
#     i=10# here i passed values
# print(myfun())#None # by calling my function without return  keyword it will print as none

# def myfunc(a,b):
#     print(a+b)
# myfunc(100,200)

# def myfunc(a,b):
#     return (a+b)
# print(myfunc(10,20))