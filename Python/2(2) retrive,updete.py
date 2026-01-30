from array import *
x=array('i',[10,20,30,40,50,60,70])

n=len(x)
for i in range(n):
    print(x[i],end=' ')

print("\n Updated Array")
x[2:5]=array ('i',[4,5,6])
print(x)

print("diplay array element after slicing")
for i in x[2:6]:
    print(i)
