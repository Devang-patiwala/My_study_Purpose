x={}

print("how many elements you want in dictionry ?")
n=int(input())

for i in range(n):
    print("Enter key Roll no")
    k=input()
    print("Enter its value marks:")
    v=int(input())
    x.update({k:v})

print("The dictionary is ",x)
