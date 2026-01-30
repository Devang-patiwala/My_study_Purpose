class student:
    def setname (self,name):
     self.name=name

    def getname(self):
        return self.name

    def setmarks(self,marks):
        self.marks=marks

    def getmarks(self):
        return self.marks

n=int(input("how many students ?"))
i=0
while(i<n):
    s=student()
    name=input("Enter Name")
    s.setname(name)
    marks=int(input("Enter marks"))
    s.setmarks(marks)

    print("HI",s.getname())
    print("Your Marks:",s.marks())

    i+=1
    print("-------------------------")
