from book import Book
from library import Library

# creat book instances

books = [
    Book("Blablabla", "George Orwell", 1949),
    Book("The Little Prince", "Antoine de Saint-Exupéry", 1943),
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
    Book("Moby-Dick", "Herman Melville", 1851)
]
# b1.display_details()

#creating Library instances
library = Library()

# add books to library

for b in books:
    library.add_book(b)
# display all books in library


# save library to file
library.save_to_file("library.json")

# load library from file
library.load_from_file("library.json")

# display all books in library again
library.display_books()