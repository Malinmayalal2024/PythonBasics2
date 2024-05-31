#Tuple Datatype
data=(20,30,40,50,60,70)                                                        #T1
print(data)
print(type(data))
print(len(data))
print(data[1])
data1=("Roman",)                                                                #T2
print(type(data1))
x=tuple((21,31,41,51,61,71))                                                    #T3
print(x)
print(x[2:5])
print(x[-5:-2])
print(x[-1])
print(x[:-1])
print(40 in data)
print(41 not in x)

#No methods in Tuple

y=list(x)                                                                       #To change tuple to list
print(y)
print(type(y))
y[2]=40                                                                         #To change 2nd position to 40
print(y)
x=tuple(y)                                                                      #To change list back to tuple
print(x)
for i in x:
    print(i)
z=(x+data)                                                                      #Join two tuples
print(z)
data2=(10,20)
print(data2*2)
print(data2.count(10))