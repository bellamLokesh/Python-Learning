class Employee: # class of employee
    def __init__(self,eid,ename,esal):# Constructor
        self.eid=eid
        self.ename=ename
        self.esal=esal

    def displayemp(self):# method for class as a displayemp
        print(self.eid,self.ename,    self.esal)
