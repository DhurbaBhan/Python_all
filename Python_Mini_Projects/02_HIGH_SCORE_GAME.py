def Score():
    score=int(input("Enter a score: "))
    return score
latest_score=Score()
with open(".\high_score.txt","r") as f:
    a=f.read()
if a=="":
    with open(".\high_score.txt","w") as f:
        f.write(str(latest_score))
else:
    with open(".\high_score.txt","r") as f:
        a=f.read()
        if (latest_score>int(a)):
            with open(".\high_score.txt","w") as f:
                f.write(str(latest_score))
                print("Your high score is updated. You can check it on txt file.")
        else:
            print("Your latest score is less than the high score.")        
