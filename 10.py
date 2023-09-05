class Time:
    def _init_(self,):
        self.hours1 =0
        self.minutes1 = 0
        
    def addTime(self,h2,m2):
        self.hours=self.hours1+h2
        self.minutes=self.minutes1+m2

    def displayTime(self):
        if(self.minutes>=60):
            self.hours+=1
            self.minutes=self.minutes-60
        print(self.hours," hrs", self.minutes," mins")

    def DisplayMinute(self):
        total_minutes = self.hours * 60 + self.minutes
        print("Total minutes: ",total_minutes)

time1 = Time()
time1.hours1=12
time1.minutes1=50
time1.addTime(1,20)
time1.displayTime()
time1.DisplayMinute()

