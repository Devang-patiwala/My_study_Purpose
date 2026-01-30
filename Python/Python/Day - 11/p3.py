def DTB(no):
    return bin(no)
def OTH(no):
    return hex(no)

while True:
    print('1. Decimal to Binary')
    print('2. Octal To Hexa ')
    print('3. Exit')
    ch = int(input('Enter Your Coice: '))
    if(ch == 1):
        no = int(input('Enter Number: '))
        print(DTB(no))
    elif(ch == 2):
        no = int(input('Enter Number: '))
        print(OTH(no))
    elif(ch == 3):
        break
    else:
        print('Invalid Choice')
