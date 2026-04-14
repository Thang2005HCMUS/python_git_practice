class LibraryDB:
    def __init__(self):
        # Dữ liệu mẫu
        self.books = [
            {"title": "Python 101", "author": "Guido"},
            {"title": "Clean Code", "author": "Uncle Bob"}
        ]
    
    def get_all_books(self):
        return self.books