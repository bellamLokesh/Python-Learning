# #
# # # three are two types of arguguments/ parmeters in function
# # # they are 1) positional Arguments:
# # # *:These are arguments passed to a function in the correct order as defined in the function.
# # # *:The position matters because Python assigns values to parameters based on their order.
# # # 2) key word arguments:
# # # *:These are arguments where you specify the parameter name explicitly while calling the function.
# # # *:Order does not matter because you are naming the arguments.
# #
# # # basic synatax:
# # # Syntax positional arguments:
# # #     def myfunc(x,y):# here i delcared x and y as two paramter
# # #         print(x,y)
# # #     myfunc(10,20)#10 20# positional arguments
# # #     # when i try to call function by function name  by specifing values to thoese x and y value is called positional arguements
# #
# # # #syntax for Key word arguments:
# def myfunc(a,b):
#     print(a,b)
#
# myfunc(b=30,a=10)# 10 30 # keyword arguments
# # # # In key word arguments we need to specify the variable name with their variable values.
# # # # In key word arguments we can jumble it means we  can take "b"last variable into first variable and assign into first varible
# # # # and taking "a"first variable and assgining into last variable by assiging value
# #
# #
# # #VVIMP-->Ex-01: Defulat values assigned to the positional arguments
# #
# # # def cool(i,j=10):# here i take two parametrs by defualt i assgined 10 value to the J
# # #     print(i,j)
# # # cool(100)#100 10 # when iam trying to calling function by passing one argument value it will assgin to the i varibale
# # # # and default value is already assgined to the j so its giving output as 100,10
# # #
# # # def cool(i,j=10):# here i declared default value to the j varible as 10
# # #     print(i,j)
# # #
# # # cool(100,500)#100 500 # if you observe here i passed two arguments value here whatever is updated in
# # # #in function it will give you as output it will ignore defualt value when you are assigning two parmenters value
# # #
# # # #vvimp->>02: Keyword arguments
# # # # Order does not matter because you are naming the arguments.
# # # def greetings(name,greetmsg):
# # #     print(greetmsg+" ",name)
# # # greetings(name="lokesh",greetmsg="hello")#hello  lokesh
# # # greetings(greetmsg="hello",name="lokesh")#hello  lokesh
# #
# #
# # #vvimp--03: Combination of positional&keyword parameters:
# # #
# def my_fun(a,b,c):
#     print(a,b,c)
# #
# my_fun(10,20,30)#10 20 30 # positional arguments
# my_fun(a=10,b=20,c=30)#10 20 30 # keyword arguments
# my_fun(c=30,a=10,b=20)#10 20 30 # key word arguments doesnt follow order
# my_fun(10,20,c=30) # 10 20 30 # comination postional and keyword arguments [all postional arguments need to mention
# # before keyword arguments.
# # firstly 10 value is assinged to the "a" variable and 20 is assigined to the "b" variable
# # the third variable i clearly delcared c=30 it means explicitly for c 30 value is allocted
# my_fun(10,b=20,c=30)#10 20 30
# # my_fun(10,b=20,30)#invalid (this is wrong as positional arguments must appear before any keyword argument
# # it will throw an error positional argument follows keyword argument
# my_fun(10,30,b=20)# syntax is correct logic is wrong #TypeError: my_fun() got multiple values for argument 'b'


# # VVIMP-->>04: How  function can return multiple values:
# def largest(a,b):
#      if a>b:
#          return a,b # if the condtion is true it will fallow and give output as a,b  value or else else block will execute
#      else:
#          return b,a
# print(largest(200,100))#(200, 100)
# print(largest(20,10))#(20, 10)
#
# res=largest(10,20) # here i assigned values and stroring those value into "res" variable
# print(res)#(20, 10) # here i printed "res" variable and its providing output
# print(type(res))#<class 'tuple'>


