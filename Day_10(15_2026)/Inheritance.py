
# # # # # # # # #
# # # # # # # # # # Basic creation parent class and child calss
# # # # # # # # # #01- when you are creating a parent class try to name it in upper case for standard
# # # # # # # # # #02-similarliy when you are creating variable names try to name it in a lower case
# # # # # # # # # #
# # # # # # # # # #EX-01>>>
# # # # # # # # # # class A : # creation of parent class
# # # # # # # # # #  def m1(self): # m1 method
# # # # # # # # # #      print("this is a class of A ")
# # # # # # # # # #
# # # # # # # # # # class B(A):#here "B" is a child class of "A" #m2 method
# # # # # # # # # #     def m2(self):
# # # # # # # # # #         print("this a class of B")
# # # # # # # # # #
# # # # # # # # # # bobj =B # here i created object as "bobj" with the help of object iam calling "child class" B
# # # # # # # # # # bobj.m1("A")#this is a class of A  #with the help of object iam trying to call "m1" method
# # # # # # # # # # bobj.m2("B")#this a class of B
# # # # # # # # # #
# # # # # # # # # #Ex-02->>> Single inheritance:
# # # # # # # # # One child class and one parent class
# # # # # # # #one parent->> one child class
# # # # # # # # # class A:
# # # # # # # # #     x,y=10,20 # Class variable
# # # # # # # # #
# # # # # # # # #     def m1(self):
# # # # # # # # #         print(self.x+self.y)# by using self. we can access class variables inside methods
# # # # # # # # # class B(A): # class "A" is parent class for "B"
# # # # # # # # #     a,b= 200,100# class varibles
# # # # # # # # #     def m2(self):
# # # # # # # # #         print(self.a-self.b)#by using self. we can access class variables inside methods
# # # # # # # # #
# # # # # # # # # bobj =B()
# # # # # # # # # bobj.m1()#30
# # # # # # # # # bobj.m2()#100
# # # # # # # #
# # # # # # # # #Ex-03>>> VVVIMP - Multilevel inheritance:
# # # # # # # # # A class derived from another derived class
# # # # # # # # parent class->>> child class->> grand child
# # # # # # # # # class A:# parent class
# # # # # # # # #     x,y= 20,30
# # # # # # # # #     def m1(self):
# # # # # # # # #         print(self.x+self.y)
# # # # # # # # # class B (A):# Child class for A -
# # # # # # # # #     a,b= 300,150
# # # # # # # # #     def m2(self):
# # # # # # # # #         print(self.a-self.b)
# # # # # # # # # class C(B):# grand child class for A
# # # # # # # # #     c,d = 10,12
# # # # # # # # #     def m3(self):
# # # # # # # # #         print(self.c* self.d)
# # # # # # # # #
# # # # # # # # # cobj=C()
# # # # # # # # # cobj.m1()#50
# # # # # # # # # cobj.m2()#150
# # # # # # # # # cobj.m3()#120
# # # # # # # #
# # # # # # # # # EX-04>>> Hierarchy level inheritance
# # # # # # # # # one parent two child class
# # # # # # # # or multiple child class inherit from one parent class
# # # # # # # # on parent class->>> multiple child class
# # # # # # # #
# # # # # # # # class A:# parent class
# # # # # # # #     x,y= 20,30
# # # # # # # #     def m1(self):
# # # # # # # #         print(self.x+self.y)
# # # # # # # # class B (A):# Child class for A -
# # # # # # # #     a,b= 300,150
# # # # # # # #     def m2(self):
# # # # # # # #         print(self.a-self.b)
# # # # # # # # class C(A):# child class for A
# # # # # # # #     c,d = 10,12
# # # # # # # #     def m3(self):
# # # # # # # #         print(self.c* self.d)
# # # # # # # #
# # # # # # # # bobj=B() # by using class "B" we can access only m1 and m2 metthods
# # # # # # # # bobj.m1()#50
# # # # # # # # bobj.m2()#150
# # # # # # # #
# # # # # # # # cobj=C()# by using class "C" we can access only m1 and m3 methods
# # # # # # # # cobj.m1()#50
# # # # # # # # cobj.m3()#120
# # # # # # # # # Explanation : here m1 is common why because it is parent class for both class "B" and class :"C".
# # # # # # #
# # # # # # # # Ex-05>>> Multiple inheritance:
# # # # # # # # multiple parents ->> one child class
# # # # # # #
# # # # # # # class A:# parent class
# # # # # # #     x,y= 20,30
# # # # # # #     def m1(self):
# # # # # # #         print(self.x+self.y)
# # # # # # # class B:# parent class -
# # # # # # #     a,b= 300,150
# # # # # # #     def m2(self):
# # # # # # #         print(self.a-self.b)
# # # # # # # class C(A,B):# child class for A
# # # # # # #     c,d = 10,12
# # # # # # #     def m3(self):
# # # # # # #         print(self.c* self.d)
# # # # # # # cobj=C() # by using "C" child class iam accessing both "A,B" classes variables value.
# # # # # # # cobj.m1()#50
# # # # # # # cobj.m2()#150
# # # # # # # cobj.m3()#120
# # # # # #
# # # # # # #Ex-06>> Calling parent class method using child class (super))Overriding method
# # # # # # # here i created same m1 method for both classes and trying to print its values
# # # class A:
# # #     def m1(self):
# # #         print("this is m1 method from class A ")
# # # class B(A):
# # #     def m1(self):
# # #         print("this is m1 method from class B")
# # #         super().m1()#this is m1 method from class A  # if you want to invoke class"A" ma method by using "super" key
# # #         # .method name we can access
# # # bobj=B()
# # # bobj.m1()#this is m1 method from class B
# # # #
# # # # # # Ex-07->>>
# # # # # class A:
# # # # #     a,b= 200,150
# # # # # class B(A):
# # # # #     c,d= 300,600
# # # # #     def m(self,x,y):
# # # # #         print(x+y)# local variables
# # # # #         print(self.c+self.d)#class "b" variables # 900
# # # # #         print(self.a+self.b)# Class "A" variables # 350
# # # # # bobj=B()
# # # # # bobj.m(15000,22000)#37000
# # # #
# # # # #Ex-08: how to override variables in class:
# # # class parent:
# # #     name="lokesh"
# # # class child(parent):
# # #     name = "scott"
# # #     def test(self): # here i created "test" method to print parent class variables value
# # #         print(super().name)
# # #
# # # cobj=child()
# # # print(cobj.name)#scott # it will give latest updated variable value
# # # cobj.test()#lokesh
# # #
# # #Ex-09: Over riding method (by using hirarical inheritance)
# #
# # class Bank:
# #     def rateofintrest(self):
# #         return 0
# # class XBank(Bank):
# #      def rateofintrest(self):
# #          return 10
# # class YBank(Bank):
# #         def rateofintrest(self):
# #             return 12
# # Xobj=XBank()
# # print(Xobj.rateofintrest())#10
# #
# # Yobj=YBank()
# # print(Yobj.rateofintrest())#12
#
# #Ex-10->> Overloading -Example 01 (polymorphism)
# # Polymorphism: one name, many forms
# # class Human:
# #     def sayhello(self,name=None):
# #         if name is not None:
# #             print("hello"+ name)
# #         else:
# #             print("hello")
# # Hobj=Human()
# # Hobj.sayhello("lokesh")#hellolokesh
# # Hobj.sayhello()#hello
#
# # Ex-11->> Overloading -Example 02 (polymorphism)
#
# class Calculation:
#     def add(self,a=0,b=0,c=0):
#         print(a+b+c)
#
# Calobj=Calculation()
# Calobj.add()#0 # here add is method
# Calobj.add(10,20)#30
# Calobj.add(20,30,50)#100