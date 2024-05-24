# Task 
# Simple Calculator
x=int(input("Enter a number1 "))
y=int(input("Enter a number2 "))
Op=input("Enter the operator")
if Op=="+":
    sum=x+y
    print(sum)
elif Op=="-":
    sum=x-y
    print(sum)
elif Op=="/":
    sum=x/y
    print(sum)
elif Op=="*":
    sum=x*y
    print(sum)
else:
    print("Invalid")

# Factorial
x=int(input("Enter a Number ")) 
fact=1
while (x>1):
    fact=fact*x
    x=x-1
    print(fact)

# Fibonacci series
x=int(input("Enter a number"))
x1=0
x2=1
for i in range(0,x):
    if i<=1:
        x3=i
    else:
        x3=x1+x2
        x1=x2
        x2=x3
    print(x3,end= " ")



