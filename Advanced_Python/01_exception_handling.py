while(True):
    
    try:
        num=float(input("Enter a number: "))
        a=56.6/num
        print(a)

    except ZeroDivisionError as e:
        print(f"The error is: {e}") 
    except ValueError as e:
        print(f"The error is: {e}")  
    except:
        print("This is other exception.")  
    finally:
        print("We are done!!")  #finally block will get executed at any cost although the program exits.          