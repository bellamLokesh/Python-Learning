
# 01-> how to create a tuple
# we can enter any type of data in collection either in list,tuple,set,dictionaries
# we can enter str,float,int


#ex-01
# x=()# Empty tuple
# print(type(x))#<class 'tuple'>

# #ex-02
# mytuple=("raju",18,29890.22)
# print(mytuple)#('raju', 18, 29890.22)
# print(type(mytuple))#<class 'tuple'>

#02-> access tuple items
# mytuple = ("cherry","raju","charan")
# print(mytuple[0])#cherry
# print(mytuple[-1])#charan
# print(mytuple[2])#charan
# print(mytuple[-4])# when you are giving index out of the range it will throw an error  "tuple index out of range"

#03-> Range of index
# mytuple = ("banana","kiwi","orange","grapes","guva")
# print(mytuple[1:4])#('kiwi', 'orange', 'grapes')
# print(mytuple[2])#orange

#04-> change the tuple items
# by defalut tuple does not allow you to change  value beacuse  it is immuatable
# but there is a  work around
# tuple -->>> list(modify)--->>> tuple # this indirect process to changeing values in tuple
#
# mytuple = ("banana","kiwi","grapes")
# mylist =list(mytuple) #here i converted tuple into list
# mylist[0]="orange"# here i modify list
# mytuple=tuple(mylist)# again here i converted list into tuple and printing the tuple .
# # it will display the changes in output
# print(mytuple)#('orange', 'kiwi', 'grapes')

#05--->> reading tuples items by using loop
# mytuple = ("apple","banana","cherry")
# for i in mytuple:
#     print(i)
# # output
# apple
# banana
# cherry
# #06-->>> check if the items existed (search of item in tuple)
# mytuple = ("apple","banana","cherry")
# if "apple" in mytuple:
#     print("yes ,item is presented")
# else:
#     print("no,item is not presented")
# if "kiwi" in mytuple:
#     print("yes ,item is presented")
# else:
#     print("no,item is not presented")
# output :
#yes ,item is presented
#no,item is not presented

# #07-->>>>> total length - counting items in  a tuple
# mytuple = ("raju",17,0.76,"ramu")
# print(len(mytuple))#4

# #08->>>add items in tuple (no we cant add,insert,replace tuple data bcz its immuatable)
mytuple = (18,19,20)
mytuple[0]="21"
# # print(mytuple)#TypeError: 'tuple' object does not support item assignment

#09->>>copy the tuple :

# mytuple = ("orange","apple","banana")
# mytuple1=mytuple
# print(mytuple)#('orange', 'apple', 'banana')
# print(mytuple1)#('orange', 'apple', 'banana')

# # 10->>> removing items in tuple (we can't bcs tuple is immuatable)
# mytuple = ("ramu","chandu","seetha")
# # mytuple.remove("ramu") # it will throw 'tuple' object has no attribute 'remove'
# del mytuple # we can delete tuple but it wont display output

# #11>>>> join/combine tuples
# t1= 10,20,30,40
# t2= "a","b",23,98.97
# t3= t1+t2
# print(t3)#(10, 20, 30, 40, 'a', 'b', 23, 98.97)
# print(type(t3))#<class 'tuple'>

#12->>> check tuples are equal/not equal

# t1= 10,20,30
# t2= "a","b","c"
# if t1==t2:# if condition checks  if the values t1 and t2 is equal it will print euqal otherwise not equal
#     print("Tuple is equal")
# else:
#     print("tuples are not equal")#tuples are not equal