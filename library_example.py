class Book:
    def __init__(self, title, author, stock):
        self.title = title
        self.author = author
        self.stock = stock

    def display_info(self):
        print(f"Book: {self.title} by {self.author}, Stock: {self.stock}")

    def borrow_book(self):
        if self.stock > 0:
            self.stock -= 1
            print(f"Book '{self.title}' borrowed successfully.")
        else:
            print(f"Sorry, '{self.title}' is out of stock.")
        print()

    def return_book(self):
        self.stock += 1
        print(f"Book '{self.title}' returned.")
        print()


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")
        print()

    def display_books(self):
        print("Library Inventory:")
        for book in self.books:
            book.display_info()
        print()


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.stock > 0:
            book.borrow_book()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is out of stock.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name}, you did not borrow '{book.title}' from the library.")


# Example Usage
book1 = Book("The Catcher in the Rye", "J.D. Salinger", 5)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 3)

library = Library()
library.add_book(book1)
library.add_book(book2)

member1 = Member("A")
member2 = Member("B")

library.display_books()

member1.borrow_book(book1)
member2.borrow_book(book2)

library.display_books()

member1.return_book(book1)
member2.return_book(book2)

library.display_books()
