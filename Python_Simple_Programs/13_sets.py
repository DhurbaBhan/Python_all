# a={} This is Dictionary type
# To 
a=set()
a.add(4)
a.add(6)
a.add(4)
a.add(7)
a.add(8)
a.add(9)
print(a)

a.remove(4)
print(a)
a.pop()
print(a)
a.pop()
print(a)
a.clear()
print(a)


b=set()
b.add(20)
b.add(20.0)
b.add('sring')
print(len(b))