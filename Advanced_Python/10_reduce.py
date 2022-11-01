from functools import reduce
li=[34,45,65,76,83]

mul=lambda a,b:a*b

a=reduce(mul,li)
print(a)


