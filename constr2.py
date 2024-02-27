class student:
    def __init__(self):
        self.name=input("enter your name: ")
        self.subj1=int(input("enter the mark of first subject:"))
        self.subj2=int(input("enter the mark of first subject:"))
        self.subj3=int(input("enter the mark of first subject:"))
        self.subj4=int(input("enter the mark of first subject:"))
        self.subj5=int(input("enter the mark of first subject:"))
    def total(self):
        self.tt=self.subj1+self.subj2+self.subj3+self.subj4+self.subj5
        print("total is :",self.tt)
    def average(self):
        self.avg=self.tt/5
        print("average is: ",self.avg)
objct=student()
objct.total()
objct.average()
        