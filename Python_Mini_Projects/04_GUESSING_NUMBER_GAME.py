import random

ran=random.randint(1,50)
guess=None
num=0
while(guess!=ran):
    guess=int(input("Guess a number from 1 to 50.\n"))
    num=num+1
    if (guess==ran):
        print('You guessed it right.')
    else:
        if(guess<ran):
            print("Try a larger number.")
        else:
            print("Try a smaller number.") 
print(f"you guessed it in {num} attempts.") 
with open("best_guess.txt","r") as f:
    data=f.read()
    if (num<int(data)):
        with open("best_guess.txt","w") as f:
            f.write(str(num))                 
