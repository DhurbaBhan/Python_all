class Library:
    def __init__(self,listofbooks):
        self.books=listofbooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print("  *",book)

    def borrowBook(self,bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname}. Please keep it safe.")
            self.books.remove(bookname)
        else:
            print("This book is not available or has already been issued, wait until return.")

    def returnBook(self,bookname):
        self.books.append(bookname)
        print("Thanks for returning this book.")

class Student:
    def requestBook(self):
        self.book=input("Enter the book: ").upper()
        return self.book
    def returnBook(self):
        self.book=input("Enter the book to return: ").upper()
        return self.book 

cl=Library(["DSA","PYTHON","SAD","MATHS","PHYSICS","CRYPTOGRAPHY"])
s=Student()
welcomemsg='''===Welcome to Central Library===
Please choose an option:
1.List of books.
2.Request a book.
3.Return a book.
4.Exit the library. '''
while(True):
    print(welcomemsg)
    a=int(input("Please enter a choice: "))
    if a==1:
        cl.displayAvailableBooks()
    elif a==2:
        b=s.requestBook()
        cl.borrowBook(b)
    elif a==3:
        b=s.returnBook()
        cl.returnBook(b)
    elif a==4:
        print("Thank you for choosing Central Library.")
        exit()
    else:
        print("Invalid choice!!")        




