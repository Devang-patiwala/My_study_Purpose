import pickle

def Add():
    with open('sample.bin','wb') as file:
        line=input('Enter Any Data :')
        pickle.dump(line,file)

def Read():
    with open('sample.bin','rb') as file:
        data=pickle.load(file)
        print(f'Data From File {data}')

def Menu():
    while True:
        print('Menu Binary')
        print('1.. Add data')
        print('2.. Read data')
        print('3.. Exit')
        ch=int(input('Enter Your Choice : '))

        if ch == 1:
            Add()
        elif ch == 2:
            Read()
        elif ch == 3:
            break
        else:
            print("Invalid choice. Please try again.")
    

Menu()
