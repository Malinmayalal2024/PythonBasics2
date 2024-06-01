 # Module -datetime
import datetime
#1. datetime-now
y=datetime.datetime.now()                                   # To get present date and time
print(y)

x=datetime.datetime(2014,12,31)

#2. Strftime                -                               #Codes-%a,%d,%b,%m,%y,%h,...
print(x.strftime("%I"))
print(x.strftime("%A"))
print(x.strftime("%b"))
print(x.strftime("%m"))
print(x.strftime("%Y"))
print(x.strftime("%H"))
print(x.strftime("%x"))
print(x.strftime("%X"))
print(x.strftime("%c"))



 
