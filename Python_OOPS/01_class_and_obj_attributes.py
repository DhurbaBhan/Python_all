class employee:
    name="google"
    salary=2000000
    def trying(self):
        print(f"the salary of {self.name} is {self.salary}")

myname=employee()
mySal=employee()
# object attribute
myname.name="youtube"
print(myname.name)
# class attribute
print(mySal.salary)
myname.trying()


