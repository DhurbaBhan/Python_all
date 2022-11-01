
class Computer:
    def config(a,cpu,ram):
        a.cpu=cpu
        a.ram=ram
        print("Config is : ",a.cpu,a.ram)
    def show(a):
        print("showing: ",a.cpu,a.ram)    
# class laptop(Computer):


com1=Computer()
com2=Computer()
com1.config("i9",32)        
com2.config("i11",32) 
com1.show()