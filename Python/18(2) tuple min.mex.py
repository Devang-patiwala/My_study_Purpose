num=eval(input("Enter elements in(): "))
print(num)
sum=0
n=len(num)
for i in range(n):
    sum+=num[i]

print("Sum of numbers=",sum)
print("Average of numbers=",sum/n)
print("mamixmum number in tuple=",max(num))
print("minimum number in tuple=",min(num))
