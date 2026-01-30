from emplyee13 import*

basic=float(input("Enter basic salary"))
gross=basic+da(basic)+hra(basic)
print("Gross salary:{:10.2f}".format(gross))

net=gross-pf(basic)-itax(gross)
print("Gross salary:{:10:2f}".format(net))
