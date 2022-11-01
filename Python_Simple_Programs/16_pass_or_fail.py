mathss=int(input("enter the marks of maths: \n"))
physics=int(input("enter the marks of physics: \n"))
python=int(input("enter the marks of python: \n"))

Om=(mathss+physics+python)/300
Om=Om*100
if Om>40:
    if mathss>33 and physics>33 and python>33:
        print("you are pass")
    else:
        print("you are fail.")    
else:
    print("you are failed.")        