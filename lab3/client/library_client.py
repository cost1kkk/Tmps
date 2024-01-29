from domain.book import Book
from domain.library_container import LibraryContainer
from factories.book_factory import BookFactory
from domain.library_adapter import LibraryAdapter

def main():
    book_factory = BookFactory()
    book1 = book_factory.create_book("The Catcher in the Rye", "J.D. Salinger")
    book2 = book_factory.create_book("To Kill a Mockingbird", "Harper Lee")

    library = LibraryContainer()
    library.add(book1)
    library.add(book2)

    print("Library Contents:")
    print(library.display())

    # Using Adapter to display library components differently
    adapted_book = LibraryAdapter(book1)
    print("Adapted Library Component:")
    print(adapted_book.display())

if __name__ == "__main__":
    main()
