#variables
# age = 25
# name = "deepak"
# height = 5.11
# print(name,age,height)


# # approach 01
# #here i declared three variables in single line of code
# #here i added some comments for user output
# name,age,height="deepak",25,5.11
# print("name is :name")
# print("age is :age")
# print("height is :height")


#If you want to know the type of data  type by using "type" function.

# x = 10
# name = "lokesh"
# sal = 10000.88
# gender = "male"
# print(x,name,sal,gender)
# print(type(x))
# print(type(name))
# print(type(sal))
# print(type(gender))
# print(len(name))


#input and output
# name = input("enter your name")
# print("hello",name)

#convert string input to number
# # approach 01
# age = int(input("enter your age:")) # whatever you are giving input in console is treated as string
# print("next year you'll be", age+0)

# approach-02 # if you want to convert string into int by useing "int" function
# age = int(input("Enter your age"))
# sal = int(input("enter your salry"))
#
# print(int(age))
# print(int(sal))
# print(type(age))
# print(type(sal))


# #approach 03 Type conversion / string operation by useing decimals
# #here i converted string into values
# num01 = float(input("Enter your first decimal number"))
# num02 = float(input("enter your second decimal number"))
#
# print(num01+num02)
# print(type(num01))# here i find which data type of numo1,numb02
# print(type(num02))

#-> arithmetic operators

# a = 10
# b = 5
#
# print(a+b)#addition
# print(a-b)# substraction
# print(a*b)#multipication
# print(a/b)#divide
# print(a//b)#floor divison
# print(a%b)#reminder


#-> relational operators

# a = 20
# b = 25
#
# print(a>b)# greaterthan false
# print(a<b)# lessthan true
# print(a>=b) # greater than equals to false
# print(a<=b)#lessthan equals to true
# print(a==b) # equals to False
# print(a!=b)# not equals to True


#-> Logical operators (and,or,not)


# #-> string operations
# # Concatination is nothing but adding two strings by using + addition symbol
# first  = "Systems"
# second = "associate"
# print(first+second)
# print(len(first))

#Practice Program Simple Calculator
#-> input two numbers and show sum,difference,division

# num1 =int (input("Enter your first number")) # here i used int function for type conversion from string to int
# num2 =int(input("enter your second number"))# here i used int function for type conversion from string to int
#
# print("addition",num1+num2)
# print("substraction",num1-num2)
# print("Multipication",num1*num2)
#
# if num2 != 0:
#     print("Divison:" ,num1/num2)
# else:
#     print("Divison is not possible")


#Calaculate age after 5 years
# age = int(input("Enter your current age"))
# future_age = age + 5
# print("your age after 5 years:", future_age)

# # same above example for practice session caluclate age after 7 years
#
# age = int(input("Enter your current age"))
# future_age = age + 7
# print("your age after 7 years:",future_age)

# Area of rectangle

# length = input("Enter length of the rectangle ")
# width = input("Enter width of  the rectangle")
# area = length+width
# print("area of rectangle:",area)

#same example for practice # caluculate area of rectangle

# length = input("Enter your Length of the rectangle")
# width = input("Enter your width of the rectangle")
# rectangle = length + width
# print("area of the rectangle:",rectangle)


# age = int(input("Enter your current age"))
# future_age = age +10
# print("Age after 10 years is:",future_age)

#01 Comment practice
# print("This is my first practice program")

# #02 String concatination
# firstname = input("Enter your first name")
# secondname = input("Enter your second name")
# # print("Hello:",firstname+secondname)
#
# #03 Artithemetic operations
# # taking 2 numbers from user input, addition,substraction,muiltipication,Division and print all
#
# num1 = int(input("Enter your first number"))
# num2 = int(input("Enter your second number"))
# print("addittion is:",num1+num2)
# print("Substraction is:",num1-num2)
# print("Multipication is:",num1*num2)
#
# if num1 != 0:
#     print("Division is:",num1/num2)
# else:
#     print("Divison is not possible")


# # Type Conversion
# #take a user input of 25 string and then convert into number and add 10 (The output is 35)
# x = int(input("Enter your number"))
# print("x is:",x+10)
# print(type(x))


# #Relational operator
# # take two numbers from user input and then print x>y,x<y,x==y then print all relational opertaors
# x = int(input("Enter your x Number"))# give 10 number
# y = int(input("Enter your x Number"))# give 20 number
# print(x>y)
# print(x<y)
# print(x==y)
# print(type(x))
# print(type(y))

# # Problem statement oif the age is between 18 to 60 print ("you are eilgible) if not not
# age = int(input("Enter your age"))
# if age <=60:
#     print("you are eligible")
# if age< 18:
#     print("You are not eligible")

#problem statement taking 1 even and 1 od number from user input
# and print whether the values are even or odd

# num1 = int(input("Enter your first number"))
# num2 = int(input("Enter your second number"))
# if num1%2==0:
#     print("Given number is even")
# if num2%2==0:
#         print("Given number is even")
# else:
#     print("given number is odd")


# #Problem statement -> Simple login system
# #User input : username and password
# username = input("Enter your username")
# password = int(input("Enter your password"))
#
# if username=="admin" and password==1234:
#     print("login successful")
#
# else:
#     print("invalid credentials")
#
# #problem statement take 2 input numbers from user and  perform +,-,*,/
# # aithmetic operations and print all the data
# num1=int(input("Enter your first number"))
# num2=int(input("Enter your second number"))
# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)

# #take a marks from user input and check if marks >=35 pas, or else fail
#
# english=int(input("Enter your english marks:"))
# math=int(input("Enter your math marks:"))
# science=int(input("Enter your science marks"))
# biology=float(input("Enter your biology marks"))# enter decimal number
#
# if english>=35:
#     print("Your english  is :Cleared")
# else:
#     print("fail")
# if math>= 35:
#     print("Your math is :Cleared")
# else:
#     print("fail")
# if science>= 35:
#     print("Your science is :Cleared")
# else:
#     print("fail")
# if biology>=35:
#     print("Your biologyis :Cleared")
# else:
#     print("fail")
# #print overall results status
#
# if english >= 35 and math >= 35 and science >= 35 and biology >= 35:
#     print("Overall passed")
# else:
#     print("overall fail")

# #practice purpose for login functionality of above same example
# username = input("Enter your username")#enter username as admin
# password = int(input("Enter your password"))#enter password as 1234
# if username=="admin" and password==1234:
#     print("Login Successful")
# else:
#     print("Invalid credentials")
#
# #note: In above example if you gave space and enter correct user name ans password you will
# get "Invalid credtials you know why that space is conisdering thats why python is case sensitive lanugae"
