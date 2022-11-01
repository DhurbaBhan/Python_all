import random

choices=["rock","paper","scissor"]
computer=random.choice(choices)
def playagain():
    human=None
    while human not in choices:
        human=input("rock or paper or scissor?: ").lower()
    if computer==human:
        print("Computer= ",computer)
        print("Human= ",human)
        print("Tie!!!")
    if computer=="rock":
        if human=="paper":
            print("Computer= ",computer)
            print("Human= ",human)
            print("You won!!!")
        if human=="scissor":
            print("Computer= ",computer)
            print("Human= ",human)
            print("You lose!!!")
    elif computer=="paper":
        if human=="rock":
            print("Computer= ",computer)
            print("Human= ",human)
            print("You lose!!!")
        if human=="scissor":
            print("Computer= ",computer)
            print("Human= ",human)
            print("You won!!!")  
    elif computer=="scissor":
        if human=="rock":
            print("Computer= ",computer)
            print("Human= ",human)
            print("You won!!!")                  
        if human=="paper":
            print("Computer= ",computer)
            print("Human= ",human)
            print("You lose!!!")
    decision=input("play again yes/no??: ").lower() 
    if(decision=="yes"):
        playagain()
    else:
        print("Bye!!!")        
playagain()            

    
