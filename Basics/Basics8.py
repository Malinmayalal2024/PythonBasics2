#Set Datatypes
data={"PV 100","PV 121","PV 200","MAX 150"}
print(data)
print(type(data))
print(len(data))
data1=set((22,23,24,25,26,27))
print(data1)
for i in data:
    print(i)
print("PB 100" not in data)
print(20 in data1)

#Methods
data1.add(28)                                                       #1. add method
print(data1)

data1.update(data)                                                  #2. update method
print(data1)
x=[120,150,160,170]                                                 
print(x)
data1.update(x)
print(data1)

data1.remove(25)                                                    #3. remove method                                                    
print(data1)
data1.discard(100)                                                  #4. discard method
print(data1)
data1.discard(22)
print(data1)

y=data1.pop()                                                       #5. pop method
print(y)
#data.clear()
#print(data)
#del data

x1=data1.union(data)                                                #6.union method
print(x1)

newdata={"PP","PC","PM"}
newdata2={"PC","PM","PS"}
X=newdata.intersection(newdata2)                                    #7.intersection method
print(X)
Y=newdata.difference(newdata2)                                      #8.difference method
print(Y)