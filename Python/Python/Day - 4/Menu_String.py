nm = input('Enter Name : ')
print('1. Length String');
print('2. Upper String');
print('3. Lower String');
print('4. Initaial Capital String');
print('5. Split String');
ch = int(input('Enter Your Choice : '))
if(ch == 1):
    print('Length of String :',len(nm))
elif(ch==2):        
    print('String Upper :',nm.upper())
elif(ch==3):
    print('String Lower :',nm.lower())
elif(ch==4):
    print('Initaial Capital String :',nm.title())
elif(ch==5):
    print('String Split : ',nm.split(" "))
else:
    print('Invalid Choice')
