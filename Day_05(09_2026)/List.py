
# 01-> How to create a list
# we can mention any type of data in lists
# remember always what ever the data is mentioning in [], sqaure backet will considered into list.
# if you mention int,float,str inside the [], it will give output of that data type is list.
# this is how we create list with multiple values


# mylist=[10,20,30,40]
# mylist1=["apple","banana","sapota"]
# mylist2=[10,20.76,"gagan"]
# mylist3=list()# creating empty list
# print(mylist) #[10, 20, 30, 40]
# print(mylist1)#['apple', 'banana', 'sapota']
# print(mylist2)#[10, 20.76, 'gagan']
# print(mylist3)#[]
# print(type(mylist))#<class 'list'>
# print(type(mylist1))#<class 'list'>
# print(type(mylist2))#<class 'list'>
# print(type(mylist3))#<class 'list'>

# #imp-02>>>>>> How to access the items from the list:
# we can access elements from list by using [0], index
# remember always index starts from left to right forward is "0" and right to left forward is "-1".
# mylist=["charan","ntr","babu","ramu"]
# print(mylist[0])#charan
# print(mylist[3])#ramu
# print(mylist[1])#ntr
# print(mylist[2])#babu
# print(mylist[-1])#ramu
# print(mylist[-3])#ntr
# print(mylist[-2])#babu
#
# # # imp->>> 03-Range of index:
# # # alwys remember what is starting and ending indexs in list
# mylist=["apple","banana","orange","kiwi","melon","pineapple","butterfruit"]
# print(mylist[0:6])#["apple","banana","orange","kiwi","melon","pineapple","butterfruit"]
# print(mylist[1:2])#["banana"]
# print(mylist[-5:-1])## negative index,["orange,"kiwi","melon","pineapple"]
#
# #imp>>>>>04- how to change the item values in the list:
# #
# mylist=["apple","banana","orange"]
# print(mylist) #['apple', 'banana', 'orange']
# mylist[0]="kiwi"# this will change the values based on the index
# print(mylist) #['kiwi', 'banana', 'orange']
# mylist[-1]="melon"
# print(mylist) #['kiwi', 'banana', 'melon']
# # mylist[-6]="cheeku"# if you try to access the values out of the list range
# # # it will throw an error "list assignment index out of range"


#vvimp>>>>>>05- how to read the list using loop
# If we have limited elements we can access values by using index
# what if we have 20 items or elements in list we need to write 20 print statements
# so that by using for loop we can print the values

#
# #example:01
# mylist=["apple","banana","cheeku","orange","113","34.86","melon","butter","lambo"]
# for i in mylist:# first it will take "apple" and stored "apple" in "i" and print "apple".
#     # it will loop until my list items printed
#     print(i)

# # example -02 : check if the item is exist in the list or not
# mylist = ["apple", "banana", "cheeku", "orange", "113", "34.86", "melon", "butter", "lambo"]
# if "apple" in mylist:# the if condtion will check the apple is presented in list or not
#     print("yes,item is presented")
# else:
#     print("item,is not presented")

# # #example-03: total length of the list(counting number of items in a list)
# mylist = ["apple", "banana", "cheeku", "orange", "113", "34.86", "melon", "butter", "lambo"]
# print(len(mylist))


# # #example-06: Adding new items in the existing list:
# # # we can add new items by using append(),insert() functions.
# mylist = ["apple", "banana", "orange"]
# print(mylist.append("cheeku"))# it will add new item at the end of the list
# print(mylist)
# mylist.insert(2,"jilebi")# by using insert we can add the values wherever we want by mentioning
# #the index positions
# print(mylist)

#example-07: remove item from list
# if it is functions () it will display in paranthesis
# # if it is keyword it wont ask paranthesis(ex:del)
# # #>>>method-01>>>>>>>>>pop() function:
# mylist = ["apple", "banana", "orange"]
# mylist.pop(0)# here we need to specify the index not the value
# print(mylist)#['banana', 'orange']


# # # >>>>>>>method-02>>>>>>: By useing "del" keyword:
# mylist = ["apple", "banana", "orange"]
# del mylist[1] # here del commond removes single item based on the index
# print(mylist)#['apple', 'orange']

# # #>>>>>>>method-03>>>>>>:clear() function :
# mylist = ["apple", "banana", "orange"]
# mylist.clear()# here it will clear all the values in the list
# print(mylist)# [],it will print empty my.list varaibleis presented we just cleared the values inside the mylist


#imp>>>Example -08: copy list:
#
# # method -01: by using list function
# mylist1 = ["apple", "banana", "orange"]
# mylist2=list(mylist1)# by using list we can copy the same values into the another list
# print(mylist1)#['apple', 'banana', 'orange']
# print(mylist2)#['apple', 'banana', 'orange']
# #
# # # method-02 :by using copy() function:
# mylist1 = ["apple", "banana", "orange"]
# mylist2=mylist1.copy()# by using copy function we can copy the one list value into the another list
# print(mylist1)#['apple', 'banana', 'orange']
# print(mylist2)#['apple', 'banana', 'orange']

# 09- combine/join lists:

# # # method -01: using + operator (concatination)
# mylist1= ["a,","b","c"]
# mylist2=["1,2,3"]
# mylist3=[mylist1+mylist2]
# print(mylist1)#['a,', 'b', 'c']
# print(mylist2)#['1,2,3']
# print(mylist3)#[['a,', 'b', 'c', '1,2,3']]
# #
# #method :02 by using loop statement
# list1= ["a,","b","c"]
# list2= ["1,2,3"]
# for i in list2:
#     list1.append(i)
# print(list1)#['a,', 'b', 'c', '1,2,3']

# # #method-03: by using extend ()function:
# list1= ["a,","b","c"]
# list2= ["1,2,3"]
# list1.extend(list2)# by using extend we can join two lists.
# # here list1 is extending list2 it means whatever tha values in list1 it will just taking and
# # adding list2 values and printing all list1+list2 values together
# print(list1)#['a,', 'b', 'c', '1,2,3']

# #10->>> check whether lists are equal/not equal:
# mylist1= [10,20,30]
# mylist2= [10,20,30]
# if mylist1==mylist2:# if condition checks  if the values mylist1 and mylist2 is equal it will print euqal.
#     # otherwise not equal
#     print("List is equal")
# else:
#     print("lists are not equal")#List is equal