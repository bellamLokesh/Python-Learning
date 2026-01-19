
class Student:# student class
    def __init__(self,sid,sname,grade):# Constructor
        self.sid=sid
        self.sname=sname
        self.grade=grade

    def displaystu(self):# method for class as a displaystu
        print(self.sid,self.sname,self.grade)