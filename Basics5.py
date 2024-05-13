#STRING DATATYPES

x="RED"
print(x)
print(type(x))
print(len(x))
print(x[1])

for i in x:                                         #To get words in string seperately
    print(i)

y=" Python is a Programming Language "
print(y)
print("Language"in y)
print("Anuraj"not in y)
print(y[2:5])                                       #From 2 to 5
print(y[:5])                                        #From 0 to 4
print(y[4:])                                        #From 4 to end
print(y[-1])                                        #Last Word
print(y[-5:-2])                                     #From -5 to -2
print(y.upper())                                    #Make String full Caps
print(y.lower())                                    #Make ""    lower
print(y.strip())                                    #Make 
print(y.replace("P","M"))

y=" Python,is,a,Programming,Language "
print(y.split(","))                                 #To split a sentence from "," inbetween
print(x+y)                                          #"Concatination" -To merge 2 variables
print(x+" "+y)                                      # To provide space btw merged files

    #Format Method

age=30
z="My Name is John and I am {}"
print(z.format(age))  

    #Assigning

a=20
b=100
Tom="I have {} apples and the amount is {} for each"
print(Tom.format(a,b))

    #Count Fn                                        #To count the no of repeated words in string

Clan="I love apple and apple is a fruit"
print(Clan.count("apple"))    

