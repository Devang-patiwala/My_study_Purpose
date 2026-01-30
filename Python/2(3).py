class student:
    def __init__(self,nm='.',ag=15,m=0):
        self.name=nm
        self.age=ag
        self.marks=m
    def display(self):
        print("name",self.name)
        print("age",self.age)
        print("marks",self.marks)
s=student("mayur",15,89)
s.display()
s1=student("sunil")
s1.display()
