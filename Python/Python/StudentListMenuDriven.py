def addStudent():
    file=open('Student.txt','a')
    no=int(input('Enter No of Student : '))
    name=input('Enter Name of Student : ')
    Sub1=int(input('Enter Subject 1 Marks of Student : '))
    Sub2=int(input('Enter Subject 2 Marks of Student : '))
    Sub3=int(input('Enter Subject 3 Marks of Student : '))
    total = Sub1 + Sub2 + Sub3
    file.writeLines(no,' ',name,' ',Sub1,' ',Sub2,' ',Sub3,' ',total)
    file.close()

def dispStudent():
    file=open('Student.txt','r')
    print(file.read())
    file.close()

def searchStudent():
    rno = int(input('Enter no to search : '))
    file=open('Student.txt','r')
    record=file.readLines()
    found=False

    for record in records:
        rno, name = record.split(' ')
        if rno == rno_to_search:
            print(f'Record found : Roll No: {rno}, Name: {name}')
            found=True
            break;
    if found==False:
        print('Student not Found')

    file.close()

while True:
    print("--Student List--")
    print("\n1.. Add Student")
    print("\n2.. Display Student")
    print("\n3.. Search Student")
    print("\n4.. Exit")

    ch = int(input("\nEnter Your choice : "))
    if ch==1:
        addStudent()
    elif ch==2:
        dispStudent()
    elif ch==3:
        searchStudent()
    elif ch==4:
        print("Thank You")
        break;
    else:
        print("Invalid Choice")
