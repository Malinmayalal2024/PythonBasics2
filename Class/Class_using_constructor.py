# class name:
#     x=10
# y=name()                                              #To get the variable printed
# print(y.x)
# name.__init__                                         #function executed during initiation of class

# class person:
#     def __init__(self,name,age) -> None:              #self: to access variables from a class
#         self.name=name
#         self.age=age
# x1=person("Raj",30)
# print(x1.name)
# print(x1.age)

# Inheritance
class person:                                           #Function defined in a class -Method 
    def __init__(self,name,age) -> None:                
        self.name=name
        self.age=age
    def print_name(self):
        print(self.name,self.age)
class student(person):
    pass
y=student("Anu",10)
y.print_name()

# Polymorphism
# 1. Function Polymorphism
x=[2,3,4,5,6,6]
print(len(x))
x1=tuple(x)
print(type(x1))
print(len(x1))
x2=set((x1))
print(type(x2))
print(len(x2))
y1="Anuraj" 
print(len(y1))
y2={"Name":"Malin"}
print(len(y2))

# Operator Overloading
print("Anuraj"*2)

