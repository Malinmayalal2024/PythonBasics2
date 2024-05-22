# While Loop
x=3
while x<10:
    print(x)
    x=x+1                                               # Increment - given last
#Break statement
x=0
while x<10:
    print(x)
    if x==5:
        break                                           # Break with 5 numbers as o/p
    x+=2                                                # Increment - given last
#Continue Statement
x=0
while x<=10:
    x+=1                                                # Increment -must be given first
    if x==5:
        continue
    print(x)                                            # Skip 5

