# File Handling
import os
x=open("sample.txt","r")
#print(x.read())
#print(x.read(5))
print(x.readline())
print(x.readline())
print(x.readline())
x.close()
#To open and append(write) add line
y=open("sample.txt","a")
print(y.write("i love football"))
y.close()
z=open("sample.txt","r")
print(z.read())
z.close()
#To open and rewrite a new line
x1=open("sample.txt","w")
x1.write(" i like games")
x1.close()
x1=open("sample.txt","r")                   # To Open a rewritten text
print(x1.read())
x1.close()
#x2=open("duplicate.txt","x")
#os.remove("duplicate.txt")                  # Imported os and used remove function to remove a file
#os.rmdir("xisting")                          #To remove a folder
