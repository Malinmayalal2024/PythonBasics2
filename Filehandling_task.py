import os
x=open("sampletask.txt","r")
#print(x.read())
#print(x.read(5))
print(x.readline())
print(x.readline())
print(x.readline())
x.close()
y=open("sampletask.txt","a")
print(y.write("its famous for its greenery"))
y.close()
os.remove("sampletask.txt")





