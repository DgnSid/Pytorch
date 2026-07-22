from micrograd.engine import Value
a = Value(-2.0)
b = Value(3.0)
c = a * b
d = a.relu()
print(d)
print(c) 
c.backward()
print(a)
print(b) 
print(b.grad)
