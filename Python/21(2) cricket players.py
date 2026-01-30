x={}

print("How many players ?")
n=int(input())

for i in range(n):
    print("Enter player name")
    k=input()
    print("Enter runs:")
    v=int(input())
    x.update({k:v})

print(x)

print("Enter players name:")
name=input()
runs = x.get(name,-1)
if(runs==-1):
    print("player not found")
else:
    print("{}made runs {}".format(name,runs))
