# # these path is common for every approach:
import sys
sys.path.append("C:/Users/User/PycharmProjects/python learning/Day_12(18_2026)/packA")#path of packA
sys.path.append("C:/Users/User/PycharmProjects/python learning/Day_12(18_2026)/packB")#path of packB
# # Approach-01
# import emp
# empobj=emp.Employee(1,"lokesh",34000)
# empobj.displayemp()#1 lokesh 34000
#
# import stu
# stuobj=stu.Student(23,"loki","A")
# stuobj.displaystu()#23 loki A

# # Approach -02
from emp import *
from stu import *

empobj=Employee(32,"loki",34860)
empobj.displayemp()#32 loki 34860
stuobj=Student(21,"lokesh","B")
stuobj.displaystu()#21 lokesh B
