class employee:
    def __init__(self):
        self.salary=0
        self.hours=0
    def getinfo(self,salary,hours):
        self.salary=salary
        self.hours=hours
    def addsal(self):
        if(self.salary<500):
            self.salary=self.salary+10
    def addwork(self):
        if(self.hours>6):
            self.salary=self.salary+5
            return (self.salary)
e1=employee()
e1.salary=450
e1.hours=7
e1.addsal()
print(e1.addwork())

        
