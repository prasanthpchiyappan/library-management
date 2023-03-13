class libaray():
    def __init__(self,list):
        self.books_list=list
        self.available_books=list[:]
        self.book_lent={}

    def allbooks(self):
        for book in self.books_list:
            print(book)

    def avb_books(self):
        for book in self.available_books:
            print(book)

    def book_ln(self,name,book):
        if book not in self.books_list:
            print("incorrect book name")
            return
        if book in self.available_books:
            self.book_lent.update({book:name})
            self.available_books.remove(book)
            print("you can tacken book ....")
        else:
            print("this book alredy taken " + self.book_lent[book])

    def return_book(self,book):
        if book not in self.books_list:
            print("incorrect book name")
            return
        if book not in self.book_lent:
            print("pooi book eduda punda")
            return
        if book in self.book_lent:
            del self.book_lent[book]
            self.available_books.append(book)
            print("successfully return the book")
            
        else:
            print("plz first take a book")


lib=libaray(['Thirukural','Ramayanam','Ponnyin Selvan','Pagavath Geethai'])
print("welcome to libarey")

while True:
    print('1. Allbooks')
    print('2. Available books')
    print('3. Barrow')
    print('4. Return Book')
    print('5. Quit')

    user_choice=int(input())
    if user_choice == 1:
        lib.allbooks()

    elif user_choice ==2 :
        lib.avb_books()

    elif user_choice == 3:
        name=input("enter the name: ")
        book=input("enter the book name: ")
        lib.book_ln(name,book)
    elif user_choice == 4:
        book=input("enter the book name: ")
        lib.return_book(book)
    elif user_choice >=6:
        print("plese enter vaild number")

    elif user_choice == 5:
        break
    else:
        print("plese enter number only")
