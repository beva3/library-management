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
    

# creat book instances
b1 = Book("The relativity","Albert Einstein",1954)
b1.display_details()
