from domain.book import Book
from utilities.notification_service import NotificationService

def main():
    book = Book("Mara", "Ioan Slavici")
    notification_service = NotificationService()
    
    book.add_observer(notification_service)

    print("Book Information:")
    print(f"Title: {book.title}")
    print(f"Author: {book.author}\n")

    # Simulate book update
    book.update_book("I. Slavici")

    print("\nAfter Update:")
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")

if __name__ == "__main__":
    main()
