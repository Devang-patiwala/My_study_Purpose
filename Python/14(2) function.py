list1=list (range(10))
print("Original list")
print(list1)

print()

list1.append(30)
print("list after appending")
print(list1)

list1[1]=99
print("list after updating")
print(list1)

del list1[0]
print("list after deleting")
print(list1)
