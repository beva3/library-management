from book import Book
import json as j
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
    
    def save_to_file(self, filename):
        # Save the the library to a file
        with open(filename,"w") as file:
            j.dump([book.__dict__ for book in self.books],file,indent=4)
        print(f"Library saved to {filename}")
    
    def load_from_file(self, filename):
        # load the library from a file
        try:
            with open(filename,"r") as file:
                books_data = j.load(file)
                self.books = [Book(**book_data) for book_data in books_data]
                print(f"Library save to {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except j.JSONDecodeError:
            print(f"Error parsing JSON data from file {filename}.")

