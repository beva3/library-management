from book import Book
from library import Library

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