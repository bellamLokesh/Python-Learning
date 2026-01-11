
# Break stops the loop immediately and jumps out of it

# #01 stop when you find 5
# for i in range(1,10):# it will print 1 to 9 numbers
#     if i==5: # here when the value is equals 5 loop will stop immediately and prints the values
#         break # break function is used to stop the loop immediately
#     print(i)
# print("loop existed")


# # same example when you find 95 stop
# for i in range(50,1000):
#     if i==95:
#         break
#     print(i)
# print("loop existed")


# Continue: it will skip the current iteration and moves to the next one
# >>>>>>>>>>>>>>

#01

# for i in range(1,10):# need to print 1 to 9 numbers
#     if i==7:# if the value is equals to 7
#         continue # This continue function will skip current iteration means it wont print 7
#     print(i) # expect 7 it will print

# #same example but mutiple condtion in single line
# for i in range(1,20):
#     if i==5 or  i==8 or i==15:
#         continue
#     print(i)

#note-> In output it will skip values of 5,8,15 and print remaining values