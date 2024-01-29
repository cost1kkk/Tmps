from domain.book import Book

class BookFactory:
    @staticmethod
    def create_book(title, author):
        # Simulate complex book creation logic, perhaps involving a database
        return Book(title, author)
