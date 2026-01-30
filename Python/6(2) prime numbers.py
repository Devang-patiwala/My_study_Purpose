def prime(n):
    

    for i in range(2,n):
        if n%i==0:
          x=0
          break
        else:
          x=1
          return x

num=int(input("how many prime numbers do you want?"))
i=2
count=1
while True:
    if prime(i):
        print(i)
        count=count+1
    i=i+1
    if count>num:
        break
