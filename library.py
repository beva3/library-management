from book import Book
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