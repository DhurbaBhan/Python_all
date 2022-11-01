def sum(a,b):
    return a+b

x=int(input("Enter a number: \n"))
y=int(input("Enter a number: \n"))    
su=sum(x,y)
print("The sum of given numbers is: ",su)  

def mul_table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
n=int(input("Enter a number whose multiplication table is to be calculated: \n"))
mul_table(n)        