print("position argument")

def attach(s1,s2):
    s3=s1+s2
    print("Total string "+s3)

attach("new","york")

print("kryword argument")

def grocery(item,price):
    print("item=%s"%item)
    print("price=%.2f"%price)

grocery(item='sugar',price=50.75)
grocery(price=88.00,item='oil')

print("default argument")

def grocery(item,price=40.00):
    print("item=%s"%item)
    print("price=%.2f"%price)

grocery(item='sugar',price=50.75)
grocery(item='sugar')
