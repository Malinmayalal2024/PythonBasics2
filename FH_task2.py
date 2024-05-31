#File Handling Task 2

#x=open("To_remove_file.txt","x")                                   #To create a new Text file
#x.close()
#y=open("To_remove_file.txt","w")                                   #To Overwrite or write a content to the file
#print(y.write("Hai,I am Malin"))
#y.close()
#z=open("To_remove_file.txt","r")                                   #To Read the Contents of File in O/P
#print(z.read())
#z.close()
#x1=open("b.txt","x")                                               #Created new file
#x1.close()
y1=open("To_remove_file.txt","r")                                   #Read the first file
m=y1.read()                                                         #To Store the read file
print(m)
y1.close()
y2=open("b.txt","w")                                                #To Overwrite the new file
y2.write(m)                                                         #To implement 
y2.close()
y3=open("b.txt","r")
print(y3.read())








