# Frozen set 
x=[20,21,22,23,24,25]
print(x)
print(type(x))
print(len(x))
y=frozenset(x)
print(y)
print(type(y))
y[1]=10
print(y)
