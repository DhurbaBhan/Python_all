a=int(input("enter first no: "))
b=int(input("enter second no: "))
c=int(input("enter third no: "))

if a>b:
    f1=a
else:
    f1=b
if f1>c:
    f2=f1
else:
    f2=c

print("the greatest value is: ", f2) 

# we can do in this way also.

a=int(input("enter first no: "))
b=int(input("enter second no: "))
c=int(input("enter third no: "))

if (a>b and a>c):
    print(f"{a} is the greatest.")
elif(b>a and b>c):
    print(f"{b} is the greatest.") 
else:
    print(f"{c} is the greatest.")       