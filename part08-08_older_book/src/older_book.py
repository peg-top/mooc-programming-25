# DO NOT CHANGE CLASS Book!
# Write your solution after the class!

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

# -----------------------------
# Write your solution here
# -----------------------------

# High Adventure is older, it was published in 1956
# Fluent Python and Norma were published in 2015

def older_book(book1: Book, book2: Book):

    if book1.year == book2.year:
        print(f'{book1.name} and {book2.name} were published in {book1.year}')
    else:
        older_book = book1 if book1.year < book2.year else book2
        print(f'{older_book.name} is older, it was published in {older_book.year}')
        



# python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
# everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
# norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

# older_book(python, everest)
# older_book(python, norma)