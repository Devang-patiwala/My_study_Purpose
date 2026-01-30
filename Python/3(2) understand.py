from array import*

arr=array('i',[10,20,30,40,50])
print('original array:',arr)
arr.append(30)
arr.append(60)
print('after apperding 30 and 60',arr)

arr.insert(1,99)
print('After inserting 99 at parition 1',arr)

arr.remove(20)
print('After removing 20',arr)

n=arr.pop()
print('Array After using pop()',arr)
print('poped element',n)

n=arr.index(30)
print("First or curante of 30 is at position ",n)

lst=arr.tolist()
print("list:",lst)
print("Array:",arr)







      
