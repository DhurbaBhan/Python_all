class Student:
    def __init__(self,name,address,salary):
        self.a=name
        self.b=address
        self.c=salary
    def getDetails(self):
        print("The name is: ",self.a) 
        print("The address is: ",self.b)   
        print("The salary is: ",self.c)

s=Student("Dhurba","Kirtipur",500000)
s.getDetails()      