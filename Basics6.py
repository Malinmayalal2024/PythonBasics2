#List Datatypes
Fruits=["apple","orange","watermelon","banana","Grapes","pineapple","cocunut"]
print(Fruits)
print(type(Fruits))
print(len(Fruits))
m=list((20,30,40,50,60))                                                                        #Another way for list 
print(m)    
print(Fruits[1])
print(Fruits[-1])
print(Fruits[2:5])
print(Fruits[:1])
print(Fruits[1:])
print(Fruits[-5:-3])
print("guava"not in Fruits)                                                                    #Membership operator
print("guava"in Fruits)                                                                        #Membership operator
Fruits[1]="guava"                                                                              #Type of Replace dataype
print(Fruits)
Fruits[2:4]=["dragonfruit","berry"]
print(Fruits)

#Methods
m.append("Numbers")                                                              #append method-To add a new to list
print(m)
m.insert(2,35)                                                                   #insert method -To add new to list at any position
print(m)
Fruits.extend(m)                                                                 #extend method-To extend one list with another
print(Fruits)
Fruits.remove("apple")                                                           #remove method-To remove from list
print(Fruits)
Fruits.pop(3)                                                                    #pop method-To remove a position 
print(Fruits)
Fruits.pop()                                                                     #pop - To remove last chara
print(Fruits)

#del Fruits[4]                                                                    #del-not a method ,but delete position
#print(Fruits)
#Fruits.clear()                                                                   #To clear the list
#print(Fruits)
#del Fruits                                                                       #To delete the list
#print(Fruits)

for i in Fruits:
    print(i)

colours=["red","blue","black","brown","violet","white","pink","yellow"]
print(colours)
colours.sort()                                                                    #To sort in alphabetic order
print(colours)
colours.sort(reverse=True)                                                        #To reverse the sort order
print(colours)
y=colours.copy()                                                                  #To copy another list to a new list
print(y)
z=list(colours)                                                                   #     ""
print(z)
x1=y+z                                                                            #To add two lists together
print(x1)
y.extend(z)                                                                       #     ""
print(y)

list1=["a","b","c"]
list2=[1,2,3,1,3,4,5]
for i in list2:
    list1.append(i)                                                              #To append more than one in a list using for loop
print(list1)
y2=list2.count(3)                                                                #To count the repeating variables
print(y2)



