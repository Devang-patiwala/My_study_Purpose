from array import *
x=array ('i',[])
print("how many elements?",end=' ')
n=int(input())

for i in range(n):
    print("Enter element: ",end=' ')
    x.append(int(input()))

print("original array",x)

print("Enter the element to search")
s=int(input())

try:
    pos=x.index(5)
    print("found at position=",pos+1)

except valueError:
    print("Not found in the array")
