
# # # #Exception Handling
# # # #Exception is an event which will cause program terminate
# # # # #Ex->>01
# # # #
# # print("this is exception handling ")
# # print("this is exception handling ")
# #
# # try :# try block
# #     print(x)# here "x" is not defined ,when i try to print exception will occur. with the help of
# #     # try and except we can fix error
# # except:# exception block # we can also specify the error
# #     print("Errror handle occured")
# #
# # print("hi this is automation tester")
#
# #
# # #Ex->>>02
# # #
# # print("hello")#hello
# # print("program is intiated here")#program is intiated here
# #
# # try:
# #     print(10/0)
# # except ZeroDivisionError:# here i mentioned error
# #     print("Exception occured and handled")#Exception occured and handled
# #
# #
# # print("program end here")#program end here
# # #
# # # #Ex->>03:Multiple except block ->> try, catch else, finally
# # # # when you are using "try" -> "except" block should be there
# # # #First need to write all except blocks
# # # # second "else" block
# # # # # after completion of else block we can write "finally" block
# # try:
# #     num1,num2=10,0
# #     results=(num1/num2)
# #     print("results is ",results)
# # except ZeroDivisionError:# Execute only when exception occured
# #     print("ZeroDivisionError occured and handled")
# # except SyntaxError:## Execute only when exception occured
# #     print("Synatax error occured and handled")
# # except:## Execute only when exception occured
# #     print("Exception handled.........")
# # else:# Executes only when no exceptions occured
# #     print("no exception occured")
# # finally:# finally always execute
# #     print("always execute")
# # #ooutput:
# # # ZeroDivisionError occured and handled
# # # always execute
# # #
# # # #Explanation :
# # # # 01.if exception is occured one of the exception will occured else block will not occured.
# # # #finally block always executed
# # # #02: Suppose exception will not occured else block will execute and finally always executed.
#
# # #Ex->>04: rising our own exception
# def enterage(num):
#     if num<0:
#         raise ValueError("enter only integers")
#     if num%2==0:
#         print("Even")
#     else:
#         print("Odd")
# print("Checking number is even or odd by calling functions")
#
# enterage(1)
# enterage(10)
# enterage(0)
# num=-1
# try:
#     enterage(num)
# except:
#     print("Exception occured and handled")
# print("progaram is completed")
# #
# # #Output:
# # # Checking number is even or odd by calling functions
# # # Odd
# # # Even
# # # Even
# # # Exception occured and handled
# # # progaram is completed
# #
# #
# #
# #