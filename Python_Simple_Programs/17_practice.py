text=input("Enter your text:\n")

if ("run out" in text):
    spam=True
elif ("make money" in text):
    spam=True
else:
    spam=False

if(spam):
    print("this is spam")
else:
    print("this is not spam")                