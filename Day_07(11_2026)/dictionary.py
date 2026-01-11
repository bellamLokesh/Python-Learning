# -01>>> Creating a dictionary
# ------------------------------
# Alwaya remeber dictionary can hold both key and value
# we can write the code for dictionary in multiple lines
# Employee number    employee name
# 101                   "x"
# 102                   "y"
# 103                   "z"


# mydic={101:"x",102:"y",103:"z"}#if it is string you need to specify the value within Double quotes"",
# print(mydic)#{101: 'x', 102: 'y', 103: 'z'}# it will print keys along with the value
# print(type(mydic))#<class 'dict'>
# when we say item or elements in dictionary means key+value

#-02->>> Access items in dictionary

# --->>>Method -01 :By using key:
# here we dont have index to access dictionary
# but we can access through key it will return the value of that particular key.
# we need to write multiple lines of code in dictionary

# mydic={
#     "brand":"iphone",
#     "model": 13,
#     "price": 60000
# }
# print(mydic["brand"])#iphone (# here we don't have index to access dictionary
# # but we can access through key it will return the value of that particular key.)
# print(mydic["model"])#13
#
# # --->>>>method -02 by using get() function :
# mydic={
#     "brand":"iphone",
#     "model": 13,
#     "price": 60000
# }
# # print(mydic.get("brand"))#iphone
#
# #--->>>03: Changing values in dictionary
# mydic={
#     "brand":"iphone",
#     "model": 13,
#     "price": 60000
# }
# print(mydic)# before updation # {'brand': 'iphone', 'model': 13, 'price': 60000}
# mydic["price"]=45000 # mention key in [], square bracket
# print(mydic)# after updation #{'brand': 'iphone', 'model': 13, 'price': 45000}

# #-->>>> 04-Reading items in dictionary by using loop:
# mydic={
#     "brand":"iphone",
#     "model": 13,
#     "price": 60000
# }
# for i in mydic: # it will print only keys from dictionary
#     print(i)
#
# # output for keys:
#
# # brand
# # model
# # price
# for i in mydic: # it will print only values from dictionary
#     print(mydic[i])
# for i in mydic.values(): #this also same by adding.values it will print only values from dictionary
#     print(i)

# output for values:
# iphone
# 13
# 60000
# ----------->>>>>>>>>>------------

# VVIMP# Same above example printing both keys and values :
# mydic={
#     "brand":"iphone",
#     "model": 13,
#     "price": 60000
# }
# for x,y in mydic.items():#this loop first it will take first key and value and printed into x,y.
#     # and again it will loop to read all the keys and values from the dictionary until the execution complete
#     print(x,y)
#
# # output :
# # brand iphone
# # model 13
# # price 60000

#05->>>> How to check key is exist in dictionary or not:
# mydic={
#     "brand":"iphone",
#     "model": 13,
#     "price": 60000
# }
# if "brand" in mydic:# condtion is true
#     print("key is presented")
# else:
#     print("key is not presented")#key is presented
# if "warrenty" not in mydic: # condtion is true
#     print("key is presented")#key is presented
# else:
#     print("key is not presented")
# if "discount" in mydic:# Condtion is false
#     print("key is presented")
# else:
#     print("key is not presented")#key is not presented
# ----->>>same above example single line without if condtion
# print("model"in mydic)#True(Condtion is true so it will display as true or else fasle)

#---06>>>>> find number of items in dictionary:len(),
# mydic={
#     "brand":"iphone",
#     "model": 13,
#     "price": 60000
# }
# print(len(mydic))#3

# -->> 07 Adding items into dictionary:
# we cant add multiple items in dictionary at a time.
# if you want to add multiple items we neeed to write multiple items with keys and values in dictionary updation
# mydic={
#     "brand":"iphone",
#     "model": 13,
#     "price": 60000
# }
# mydic["color"]="blue"# here we need to specift the both key and values of dictionary
# print(mydic)#{'brand': 'iphone', 'model': 13, 'price': 60000, 'color': 'blue'}

#-->>> 08 remove item to dictionary:
# ->>>method 01: by using pop():
# mydic={
#     "brand":"iphone",
#     "model": 13,
#     "price": 60000
# }
# mydic.pop("price")# here we need to specify the key which we want to remove
# print(mydic)#{'brand': 'iphone', 'model': 13}

#method--02: by del keyword:
# mydic={
#     "brand":"iphone",
#     "model": 13,
#     "price": 60000
# }
# del mydic["brand"]# it will delete both key and values related to brand
# print(mydic)#{'model': 13, 'price': 60000}

# here i want to delete whole key words and values of dictionary by using del key word
# mydic={
#     "brand":"iphone",
#     "model": 13,
#     "price": 60000
# }
# mydic.clear()# it will clear the all values and keys but my dictionary is still displays in output
# print(mydic)#{}
# # del mydic # here whole dictionary will be deleted
# # print(mydic)# if we try to print delted dictionary it will thow an error NameError: name 'mydic' is not defined

#-->>> 09>>> copying dictionary:

# ---->>>method-01
# mydic={
#     "brand":"iphone",
#     "model": 13,
#     "price": 60000
# }
# without using copy function:
# mydic1=mydic # it will copy my dic keys and values and it will displyed as the same output for mydic1
# print(mydic)#{'brand': 'iphone', 'model': 13, 'price': 60000}
# print(mydic1)#{'brand': 'iphone', 'model': 13, 'price': 60000}

#--->>>>method-02: by using copy() function:
# mydic={
#     "brand":"iphone",
#     "model": 13,
#     "price": 60000
# }
# mydic1=mydic.copy()# by using copy function we can copying mydic keys and values and store it into mydic1
# print(mydic1)#{'brand': 'iphone', 'model': 13, 'price': 60000}