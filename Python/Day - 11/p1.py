def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

while True:
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exit')
    ch = int(input('Enter Your Coice: '))
    if(ch == 1):
        no1 = int(input('Enter No1: '))
        no2 = int(input('Enter No2: '))
        print(add(no1,no2))
    elif(ch == 2):
        no1 = int(input('Enter No1: '))
        no2 = int(input('Enter No2: '))
        print(sub(no1,no2))
    elif(ch == 3):
        no1 = int(input('Enter No1: '))
        no2 = int(input('Enter No2: '))
        print(mul(no1,no2))
    elif(ch == 4):
        no1 = int(input('Enter No1: '))
        no2 = int(input('Enter No2: '))
        print(div(no1,no2))
    elif(ch == 5):
        break
    else:
        print('Invalid Choice')
