
# ->01 creating a set
# myset = {"loki","shiva",123,45.324,"jilebi"}
# print(myset)#{'jilebi', 'shiva', 123, 45.324, 'loki'}
# # i mentioned in loki as a first element if you observe output the first element is jilebi
# # thats why set is unordered and unindexed(means if the values are elements are ordered only we can access by index)


#02>> accessing items from set
# by using for loop we can extract all the values from sets .
# but we can't extract specific values from sets beacuase set is unordered.

# myset = {"kala","parvathi",90,34.5}
# for i in myset:
#     print(i)

# Output:

# parvathi
# 90
# 34.5
# kala

# # 03>>> values exist in sets:
# myset = {"kala", "parvathi", 90, 34.5}
# print("kala"in myset)# True (Values are presented in set it will print true or else false)
# print(100 in myset)#False

#04>>> adding items into the set:
# by using add()--->> by using add function we can add single item in set
# by using update()--->>> by using update function we can add multiple items into a set

#
# # --->>>>Method-01 by using add():
# myset = {"kala", "parvathi","mango"}
# myset.add("orange")
# myset.add("orange","apple")#TypeError: set.add() takes exactly one argument (2 given)
# print(myset)#{'kala', 'parvathi', 'orange', 'mango'}

#--->>>> method-02 : by using update ()
# myset = {"kala", "parvathi","mango"}
# myset.update(["guva","grapes",223])# if you want to add multiple items by using update function mention all the values in side [], square brackets
# print(myset)#{'guva', 'parvathi', 'kala', 'grapes', 'mango', 223}

# #05>>>> find number of items in a set-->> len()
# myset = {"kala", "parvathi","mango",123,90.87}
# print(len(myset))#5

#06-->>> how to remove the items in set
# by using remove():-->> by using remove we can remove only one element value
# by using discard():->> by using discard we can remove only one element value

# -->>>method-01
# myset = {"kala", "parvathi","mango",123,90.87}
# myset.remove("kala")
# # myset.remove("kala","mango")# if you try to remove more than one element it throw an
# # TypeError: set.remove() takes exactly one argument (2 given)
# myset.remove("cheeku")# if you try to remove the unindexed value (its not presented in set )it will throw an
# # KeyError: 'cheeku'
# print(myset)#{'parvathi', 123, 90.87, 'mango'}
#
# # #method-02
# myset = {"kala", "parvathi","mango",123,90.87}
# myset.discard("kala")
# myset.discard("xyz")# it wont throw an error it just print set values
# # myset.discard("kala","mango")#TypeError: set.discard() takes exactly one argument (2 given)
# print(myset)#{'parvathi', 90.87, 123, 'mango'}

#07-->>> clear () all items form list:
# myset = {"kala", "parvathi","mango",123,90.87}
# myset.clear()# it will clear all the values in side the set but variable is avilable thats why it will return empty set.
# print(myset)#set()
# del myset# it will delete the set
# print(myset)# it will throw an error why bcz we are tying to print deleted set NameError: name 'myset' is not defined.
#
# #08-- join/combine two sets :
# #by using union()
# by using update()

#-->>>method 01 by using union():
# # prevoiusly we used + concatination operator for list and tuple
# myset={"loki","ramu","cherry"}
# myset1={1,2,3}
# myset2=myset.union(myset1)# using union we can join two sets but it is unordered
# print(myset2)#{1, 2, 3, 'ramu', 'cherry', 'loki'}

# #-->>> method-02 :  by using update()
# myset1={"loki","ramu","cherry"}
# myset2={1,2,3}
# myset1.update(myset2)# it will combine all the values from set1 and set2 and print the values
# print(myset1)#{1, 2, 3, 'ramu', 'cherry', 'loki'}