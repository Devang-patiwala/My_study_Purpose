group1=[1,2,3,4,5]
search=int(input("enter element to search"))
for element in group1:
    if search==element:
        print("element found in the list",search)
        break
    else:
        print(search,"element not found")
