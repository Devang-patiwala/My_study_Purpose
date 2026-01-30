class myclass:
    n=10
    def __init__(self):
        myclass.n+=1
    @staticmethod
    def no_of_objects():
        print("No of instances create are",myclass.n)
obj1=myclass()
obj2=myclass()
obj3=myclass()
myclass.no_of_objects()
