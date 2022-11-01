class Bus:
    def __init__(self,name,contact_no):
        self.name=name
        self.contact_no=contact_no
        
    def bookSeat(self):
        li=["A1","A2","A3","A4","B1","B2","B3","B4"]
        BookAgain=True
        lis=[]
        while BookAgain:
            print(f"Hello {self.name}, The available seats are: \n",li)
            b=input("Which seat do you want to book now?? ")
            if b in li: 
                lis.append(b)
                print(f"Congratulations, your seat {b} is booked successfully!!")
                li.remove(b)
                c=input("Still want to book another seat?? Yes/No: \n").lower()
                if c=="yes":
                    BookAgain=True
                else:
                    print(f"Your total seats are: {lis}")
                    print('''Thank you for joining with us!!
                    Feel free to contact for further information.
                    Contact NO: 9877777777''')
                    break
            else:
                print("Enter the correct seat no: \n") 
    

a=input("Do you want to book the bus seat yes/no? \n")  
if a.lower()=="yes":
    name=input("Enter your name: \n").title()
    contact_no=input("Please enter your contact number: \n")
    b=Bus(name,contact_no)
    b.bookSeat()
else:
    print("Thank you!! Have a nice day.")    
    
       