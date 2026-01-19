
# # # Ex-01>>>
# #
# # # class myclass: # here iam creating class name by using "class" key word and iam naming class as "myclass"
# # #     def myfun(self):# whatever we are creating inside class are called "methods","self"is a deafult
# # #         pass # none it wont return anything
# # #     def display(self,name):
# # #         print(name)
# # #
# # # obj =myclass() # here i created "object" by using class name as" myclass" and iam storing myclass values into "obj" variable
# # # obj.myfun() # iam calling "myfun" method it wont return anything because i didnt pass any argument
# # # obj.display(name="lokesh")#lokesh # here i called "display" method by printing name argument value.
# # #Above example is also example for (instance method)
# # # Ex-02>>>>>:
#
# class myclass:
#
#     def m1(self):
#         print("this is instance method")
#     @staticmethod
#     def m2(self,name):
#         print(self,name)
#
# mc=myclass()
# mc.m1()# here calling instance method by using "object" name "mc"
# mc.m2(20,100)#20 100
# myclass.m2(100,200)#100 200 # here calling static method by using class "myclass"not through object
# #

# # #Ex-03>>> How to create class variables and how to access class variables inside the method:
# #
# # # class myclass:
# # #     a,b=10,20# class variables
# # #
# # #     def add(self):# Adding two values
# # #         print(self.a+self.b)# when i tried to print class varibles within the method its showing error.
# # #         # if you want to print class variables inside the method we need to print "self". key word in
# # #         #print statement by mentioning variable name
# # #     def mul(self): # multiply two values
# # #         print(self.a*self.b)
# # # obj=myclass() # created object
# # # obj.add()#30 # addition of a,b
# # # obj.mul()#200 # multipication of a,b
# #
# #
# # #Ex-04>>>> Comindation of global variable,class variable,local variable:
# #
# # i,j=15,25 # global variable
# # class myclass:
# #      a,b=10,20 # class variable
# #
# #      def add(self,x,y):# x,y are the local variables inside method we can create local variable
# #          print(x+y) # local variables
# #          print(self.a+self.b) # class varaibles by using "self." we are printing class variables inside method
# #          print(i+j) # global variable we can access anywhere
# # obj=myclass()
# # obj.add(100,200)# these values will assing to the local variables of x,y
# #
# # # output
# # #-------
# # # 300
# # #30
# # #40
# # # explanation : first it will print local variable
# # # then it will print class variable
# # # then it will print global variable
#
#
# # Ex-05>>> take two variables a,b and assign same variables to the all varibles like
# #global,class and local with different value
# #
# # a,b= 15,25 # global variable
# # class myclass:
# #      a,b= 10,20
# #      def addition(self,a,b):
# #          print(a+b)#local varibles within the function local variables are printed
# #          print(self.a+self.b) # class varible for calss variable just specify self.variable name it will print.
# #          print(globals()['a']+globals()['b'])# global varible # if all the varible names are same if you want to print global
# #          # varible by using globals() keyword and [''] and mention varible names inside square bracket
#
# # mc=myclass()
# # mc.addition(100,200)
# #
# # # Output:
# # #300 -->> Local varibles
# # #30 ---->>> Class varibles
# # #40------>>> Global varibles
#
# #Ex-06-->>> one class can have multiple objects
# # # we can create multiple objects with single class
# # class myclass:
# #     def display(self,name):
# #         print("this is display method")
# #         print(name)
# #
# # obj1=myclass() # here i created object as myclass() and storing values into "obj1"
# # obj1.display("lokesh")
# #
# # obj2=myclass()# here i created object as myclass() and storing values into "obj2"
# # obj2.display("lucky")
# #
# # #Output:
# # # this is display method
# # # lokesh # obj1
# # # this is display method
# # # lucky # obj2
#
# #Ex-07: Constructor  along with methods example:
# class mycalss:
#     def __init__(self): # here i created constructor by using "def" key word and __ininit__()
#         print("this is constructor")
#     def m1(self):
#         print("hello")
#     def m2(self,x,y):
#         print(x+y)
#
# mc=mycalss() # invoke constructor automatically
# mc.m1()# method we have call explicitely by using object
# mc.m2(10,20)
#
# #output:
# # this is constructor
# # hello
# #30

#Ex-08: Constructor with argument:
# class mycalss:
#      name= "jhon" # class variable
#      def __init__(self,name): # constructor with argument "name"
#          print(name)
#          print(self.name) # here iam printing calss variable inside constructor
#
# mc=mycalss("loki")# passing parameter to the constructor

#output:
# loki # printing constructor argument value here
# jhon # printing class variable value

#Ex-09>>VVIMP : It will cover all examples
# Here i want to create employee "class" inside this employee "class" i will create one "constructor"
# which will accept three parameters eid,ename,esal
# display()-->>> this method will print eid,ename,esal
#
# class empclass:
#     def __init__(self,eid,ename,esal):
#         self.eid=eid
#         self.ename=ename
#         self.esal=esal
#     def display(self):
#         print(self.eid,self.ename,self.esal)
# e1=empclass(1,"lokesh",87000)
# e1.display() #1 lokesh 87000
#
# e2=empclass(2,"lucky",60000)
# e2.display()# 2 lucky 60000

# #Ex-10:
#
# class empclass:
#     def __init__(self, eid, ename, esal):
#         self.eid = eid
#         self.ename = ename
#         self.esal = esal
#
#     def __str__(self):# it will return only string type as areturn it wont print int,float if you try print e
#         #expect string it will throw an type error;__str__ returned non-string (type tuple)
#         return (self.ename)
#
#
# e1 = empclass(100, "lokesh", 76000)
# print(e1)#lokesh