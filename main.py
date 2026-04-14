from models import Book
from database import LibraryDB

def run():
    db = LibraryDB()
    print("--- WELCOME TO LIBRARY SYSTEM ---")
    for b_data in db.get_all_books():
        book = Book(b_data['title'], b_data['author'])
        print(book)

if __name__ == "__main__":
    run()