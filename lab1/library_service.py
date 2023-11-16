# importing sys
import sys
 
# adding models to the system path
sys.path.insert(1, '/home/niciu/lab1/models')
 
# importing the hello
from book import Book
from user import User

class LibraryService:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)

    def add_user(self, username, email):
        user = User(username, email)
        self.users.append(user)

    def list_books(self):
        return self.books

    def list_users(self):
        return self.users