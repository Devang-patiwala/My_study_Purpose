student=["Akshay","Satish","Nisha"]
marks=[55,78,89]

#make dictionary
z=zip(student,marks)
d=dict(z)
print("{:15s} -- {:15s}".format("STUDENT","MARKS"))
for i in d:
    print("{:15s} -- {:5d}".format(i,d[i]))
