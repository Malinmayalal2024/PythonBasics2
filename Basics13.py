# Funtions
def len():
    print("Starter")
len()

# Arbritrary Arguments[args]
def len(*x):
    print(x[:5])
len(2,3,4,6,7,8,9)

# Keyword Argument[kwargs]
def len(a,b,c,d):
    print(a)
len(a="ab",b="ba",c="cb",d="de")

# Arbritrary Keyword Arguments[**kwargs]
def len(**x):
    print(x["Python"])
len(Python="Java")

# Default Parameters
def mycountry(country="India"):
    print(country)
mycountry("England") 
mycountry("Russia")
mycountry()                            # Default parameter                            

# Return Statement
def len(x):
    return 10+x
print(len(9))

def len(x,y):                          # To return 2 numbers
    return x+y
print(len(1,2))

def len(x):                            # Pass Statement
    pass

# Lambda Function
a=lambda x:10+x
print(a(10))

b=lambda x,y,z:x+y+z
print(b(30,30,30))





    
