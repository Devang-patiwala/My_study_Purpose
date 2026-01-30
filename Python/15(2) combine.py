x=[10,20,30,40]
y=[100,120,130,140]
print("combined list ",x+y)

print("Repeat x",x*2)

m=x

print("m= ",m)
lst=x[:]

print("x= ",x)
print("cloned list=",lst)

x[1]=99
print("x= ",x)
print("lst=",lst)
