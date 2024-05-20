#Dictionary(Mapping Datatypes)
data={"Name":"Abhiram","Job":"Artist","Age":23}
print(data)
print(type(data))
print(len(data))
data1=dict(Name="Abhiram",Job="Artist",Age=23)
print(data1)
print(data1["Age"])
#Methods
print(data1.get("Age"))                                         # Get Method
print(data1.keys())                                             # Keys Method
print(data1.values())                                           # Values Method
print(data1.items())                                            # Items Method
print("Age" in data1)                                           
print("Salary" not in data1)                                    
data1["Name"]="Anu"                                                              #To change a key value
print(data1)
data1.update({"Name":"Malin"})                                  # Update Method - To change key value
print(data1)
data1.update({"Salary":100000})                                                  # To add new key and value
print(data1)
data1["Location"]="Edapally"                                                     # ""
print(data1)
data1.pop("Location")                                                            # To remove a key and value
print(data1)
data1.popitem()                                                 # To remove last key and value
print(data1)
    #del data1["Age"]                                           # Same as pop method
    #print(data1)
    #data1.clear()                                              # Clear Method
    #del data1
    #print(data1)
for i in data1:                                                                 # To get key only as o/p
    print(i)
for i in data1:                                                                 # To get key and value in loop as o/p
    print(data1[i])                                           
for i in data1.keys():                                                          # To get keys only as o/p 
    print(i)
for i in data1.values():                                                        # To get values as o/p 
    print(i)
for i in data1.items():                                                         # To get keys and values as o/p
    print(i)
data2=data1.copy()
print(data2)
z=dict(data1)
print(z)
# Nested Dictionary
Family={"Child 1":{"Name":"Poorna","Age":23},"Child 2":{"Name":"Anna","Age":21},"Child 3":{"Name":"Malin","Age":21}}
print(Family)
print(Family["Child 3"]["Name"])                                                # To get a key value from another key
print(Family["Child 2"]["Age"])                                                 #       ""
