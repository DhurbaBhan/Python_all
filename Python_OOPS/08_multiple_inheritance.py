class Base1:
    def greet(self):
        print('This is base1 greet.')
class Base2:
    def greet(self):
        print("This is base2 greet.")
class Child(Base1,Base2):  #In c++, it creates ambiguity and we use SRO(Scope Resolution Operator) but in python, MRO(Method Resolution Order)
    def getDetails(self):
        super().greet()
        print("this is child getDetails.")
c=Child()
c.greet()
c.getDetails()
