def addEmployee():
    file = open('emp.txt','a')
    no = int(input('Enter Employee no : '))
    name = input('Enter Employee name : ')
    dept = input('Enter Employee Department : ')
    sal = int(input('Enter Employee Salary : '))
    #file.write(str(no))
    #file.write(name)
    #file.write(dept)
    #file.write(str(sal))
    record = (f"\n{str(no)} {name} {dept} {str(sal)}\n\n")
    file.write(record)
    file.close()
    

def dispEmployee():
    file = open('emp.txt','a')
    for r in rec:
        print(f"\n{r.no} {r.name} {r.dept} {r.sal)}")
    file.close()
    

while True:
    print("--Employee List--")
    print("\n1.. Add Employee")
    print("\n2.. Display Employee")
    print("\n3.. Employee with growth salary")
    print("\n4.. Exit")

    ch = int(input("\nEnter Your choice : "))
    if ch==1:
        addEmployee()
    elif ch==2:
        dispEmployee()
    #elif ch==3:
     #   searchEmployee()
    elif ch==4:
        print("Thank You")
        break;
    else:
        print("Invalid Choice")
