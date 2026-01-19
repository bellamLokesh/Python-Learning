# # # here iam try to call both animal and bird modules
# # # Approach->>>>01
# # import animal# here i imported animal module through "import" keyword.
# # import bird #here i imported bird module through "import" keyword.
# # animal.fly()#animal can't fly # here i called through modulename.function name
# # animal.color()#animal is balck
# #
# # bird.fly()#bird can fly
# # bird.color()#bird is green
#
# #Approach->>>02
# from animal import *
# fly()#animal can't fly
# color()#animal is balck
# from bird import *
# fly()#bird can fly
# color()#bird is green
#
# ----------------------
# from  animal import *
# from bird import *
# fly()
# color()
# # if you try these import method at a time whatever is updted latest it will fetch data from that module.
# # so here problem is i created same functions thats why its giving latest update details from bird function
# # if it is different functions for both method we can use this one.