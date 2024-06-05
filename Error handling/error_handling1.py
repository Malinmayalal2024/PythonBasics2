# try:
#     print(x)
# except:
#     print("error occured")
# try:
#     print(x)
# except NameError:
#     print("x is not defined")
# except:
#     print("error occured")
x= 2004
try:
    print(x)
except:
    print("error occured")
try:
    print(x)
except NameError:
    print("error occured")
else:
    print("No error")
finally:
    print("finished")

#Raise Keyword
x=-5
if x<0:
    raise Exception("No numbers below zero allowed")



















