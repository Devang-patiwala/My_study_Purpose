emp={1:'Yash',2:'Dev',3:'Ayush'}
empid = int(input('Enter Emp ID:'));
if(emp.keys()==empid):
    print('Yes')
else:
    emp[empid]='Devang'
print(emp)
