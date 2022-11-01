# example 1 _ _ _ _ _ _

li=[4,5,6,6,7,8,9,9,7]
func=lambda a:a*a
print(set(map(func,li)))  

# example 2 _ _ _ _ _ _ 
def str(s):
    return s+" added. "
strin='youcandoit'
li=map(str,strin)
for i,item in enumerate(li):
    print(i,item)
print(type(li))
print(li)   