from domain.observer import Observer

class NotificationService(Observer):
    def update(self, book):
        print(f"Notification: Book '{book.title}' by {book.author} has been updated.")
