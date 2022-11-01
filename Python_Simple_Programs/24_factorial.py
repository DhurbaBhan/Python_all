from re import I


num=int(input("Enter a number: \n"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print('The factorial of entered number is: ', fact)