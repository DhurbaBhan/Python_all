num=int(input("enter a num to check prime or not: \n"))
c=0
for i in range(1,num+1):
    if num%i==0:
        c=c+1
if(c==2):
    print(f"{num} is a prime number.")  
else:
    print(f"{num} is not a prime number.")  

num=int(input("enter a number:\n"))
prime=True
for i in range(2,num):
    if (num%i==0):
        prime=False
        break
if(prime):
    print("prime")
else:
    print("not prime")
        