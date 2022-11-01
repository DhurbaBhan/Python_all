# using for loop
num=int(input("enter a num whose mul table is to be calculated: \n"))

for i in range(1,11):
    print(f"{num} x {i} ={num*i}")

# using while loop

num=int(input("enter a num whose mul table is to be calculated: \n"))
i=1
while (i<=10):
    print(f"{num} x {i} = {num*i}")
    i=i+1