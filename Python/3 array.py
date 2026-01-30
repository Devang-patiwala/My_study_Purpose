elements=[10,20,0,40,50]
print("elements befor modifying")
print(elements)
x=bytearray(elements)
x[0]=88
x[1]=99
print("elements after,modify")

for i in x:
    print(i)
