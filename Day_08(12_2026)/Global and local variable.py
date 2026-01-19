

#The variables create outside of the functions are called as global variable.
#we can declare a global variable before function or after function
#global varible we can access from anywhere either outside of the function or inside of the function
#The Variables create inside of the functions are called as local variable.
# local variable can access only within the function

# #Ex-01:
# global_var=20 # global variable (outside of the function)
#
# def myfun():# function declaration
#     local_var=10 # local variable
#     print(local_var)#10 it is value of the local variable
#     print(global_var)#20 it is value of the global variable
# myfun()# calling function

# print(local_var)#invalid ->> Local variable can access only inside of the function.
# print(global_var)# 20 global variable can access anywhere from function in and outside of the function

# Ex:02->>

# xy=100 # global variable
# def cool():
#     xy=200 # local variable here i declare same "xy" as same for local and global variable
#     print(xy)# if i print xy it will print local variable value why bcz iam calling  print statement in within the function
# cool()#200


# #VVIMP->>Ex-03>>> : using global variable in local variable and update value
# if you want access global variable in local variable we need use "global" keyword
# xy=100 # global variable
#
# def cool():
#     global xy # by using global key word we are updating xy variable value in global value
#     xy=200# local variable
#     print(xy)#200
#
# cool()

#vvimp-->>Ex-04>>>: Taking global variable and updating global variable and calling the function:
# x=100 # global variable
# def cool():
#     global x # using global key word in side function
#     x=500 # here i updated global variable value as a 500
#     print(x)
# # cool()#500  when iam calling by function name it will give output as updated value of 500
# # print(x)# 100 when iam try to print by commenting calling function it will give as 100 defalut value

#VVimp->> Ex-05>> :taking global variable inside a function by using a "global" keyword:
#
# def cool():
#     global x # here i created a global variable inside a function by using "global" keyword
#     x=100
#     print(x)
# cool()#100
# print(x)#100 # when iam trying to print global variable outside of the function it will give as a 100
# # why beacuse we can access global varible as inside and outside of the function.