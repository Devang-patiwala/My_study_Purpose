def AOR(w,l):
    return w*l
def AOT(h,b):
    return 0.5*(h*b)
def AOC(r):
    return 3.14*r*r

while True:
    print('1. Area of Rectangle')
    print('2. Area of Circle ')
    print('3. Area of Triangle')
    print('4. Exit')
    ch = int(input('Enter Your Coice: '))
    if(ch == 1):
        w = int(input('Enter Width: '))
        l = int(input('Enter Length: '))
        print(AOR(w,l))
    elif(ch == 2):
        h = int(input('Enter Heigth: '))
        b = int(input('Enter Base: '))
        print(AOT(h,b))
    elif(ch == 3):
        r = int(input('Enter Radius: '))
        print(AOC(r))
    elif(ch == 4):
        break
    else:
        print('Invalid Choice')
