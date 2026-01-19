python-- structured + object oriented.
#oops ->> (object oriented programming concepts)
#class
#object
#Inheritence
#polymorphisim

# class                                  object
# Employee ------------->>>>>>>jhon,ram,seetha,lakshman
# Animal --------------->>>>>>>dog,horse,elephant etc

#01->> Class:
#collection of variables (attributes) & method (behaviour)
# a class is a blue print
#if you want to create class in python use a keyword called "class"
# logical entity
# does not occupy space in the  memory
# once we create a class we can create a multiple objects.


#02-->>> Object: Object is an instance of a class
# physical entity
# it will occupy  certain amount space in the memory
#once we create a class we can create a multiple objects. but objects are independent(ex: if i have employee data
# i have 3 employess data emp1,emp2,emp3, i have their id,name,contact,sal,address these are independent)

# Difference between function VS Method:
# Function--->>>  we can create without class
# Method-->>> creates inside the calss


#->> How to create class:
#01-if you want to create class in python use a keyword called "class" .
# and space give class name ":" give collen.
#02- inside class we can create methods and variables
#03- methods and variables are optional(sometimes we have variables and sometimes we have only methods)
#04-Whenever we are creating "function" inside calss we can call it as "method"
#05- By default method called one argument called "self" ("self" by deafult argument)
#06- If we have multiple varibles we need specify "," comma after "self" and give varible names.
# don't remove self argument
#07- whenever we called "self" that method will represnting/indicating of particluar "class"
#08- how can we call object- object name+method name


#02--->>> 2 Types of methods we can define within the class:
# Instance method -(we can call only through object)
# Static method-(we can directly call by using class)

# annoatation  @staticmethod " whichever the method we are metiontioning static method that method is called staticmethod.
# Advantage of staticmethod -when you are creating a static method that method is common for every objects.
# instance method : we can call/invoke through "object" only.
# static method : we can call/invoke through "calss" only.

# global variable:
# class variable : class variables are variables created inside the class
# local variable :



# Method------>>>>>>>>>>>>> V/S> >>>>>>>>-----------------------------------Constructor
#01. give any name                                01.Constructor name is fixed  def__inint__(self)
#02.return the values                             02.constructor will not return any value
#03.method can take arguments/parameters          03. constructor can also take arguments/parameters
#04. we have to use an object to invoke method    04.constructor will be called at the time of object creation itself.