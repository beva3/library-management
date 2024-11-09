class Book:
    def __init__(self, title, author,year):
        self.title = title
        self.author = author
        self.year = year
    
    def display_details(self):
        print('-'*50)
        print(f"Titre                   : {self.title}")
        print(f"Auteur                  : {self.author}")
        print(f"Année de publication    : {self.year}")
        print('-'*50)

class Library:
    def __init__(self):
        self.books = [] # list of books
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Book {book.title} added to the library")

    def remove_book(self, title):
        for b in self.books:
            if b.title == title:
                self.books.remove(b)
                print(f"Book {b.title} removed from the library")
                return  # Book found and removed. Return immediately.
        print(f"Book : {title} not found in the library")
    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return  # No books to display. Return immediately.
        else :
            for b in self.books:
                b.display_details() 

# creat book instances
b1 = Book("The relativity","Albert Einstein",1954)
b2 = Book("The Pragmatic Programmer","Andrew Hunt",2000)

# b1.display_details()

#creating Library instances
library = Library()

# add books to library
library.add_book(b1)
library.add_book(b2)

# display all books in library
library.display_books()
library.remove_book("The relativity")

library.display_books()