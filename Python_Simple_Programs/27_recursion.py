
fact=0
def factorial(num):
    if num==0:
        return 1 
    else:    
        return num*factorial(num-1)
num=int(input("Enter a number: "))

f=factorial(num)
print(f"The factorial is of {num} is: ",f)