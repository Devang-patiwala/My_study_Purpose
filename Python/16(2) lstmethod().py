num=[10,20,30,40,50,60,70]
print('original list: ',num)

n=len(num)
print("number of elements in list= ",n)

num.append(80)
print('After appendimg 80',num)

num.insert(1,99)
print('After inserting 99 at position 1',num)

#copy
num1=num.copy()
print=("newly create copied list num1=",num1)

#count elements
num.append(50)
print(num)
n=num.count(50)
print("No of times 50 found in the list is: ",n)


#remove element
num.remove(70)
print('After removing 70',num)

num.pop()
print('list after using pop()',num)


#sort()
num.sort()
print('List after sorting',num)

#reverse()
num.reverse()
print('list after reversing',num)

#clear()
num.clear()
print('List after clearing all elements',num)
      
