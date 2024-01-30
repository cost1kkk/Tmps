# Library Management System

## Author: Baxanean Constantin

## Project Description
The Library Management System is a software application designed to manage a library's book inventory efficiently. The system uses the Observer design pattern to establish a one-to-many dependency between objects, allowing multiple observers to be notified of changes.


### Use:
The project employs the Observer pattern for handling updates to the book objects and notifying observers.


### Theory:
Observer:

Observer is a behavioral design pattern that defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. Useful when a subject (or publisher) needs to notify a list of observers (or subscribers) about changes in its state.




## Design Patterns Implemented

Observer Design Pattern

Classes: Book, Observer, NotificationService

Purpose: To establish a one-to-many dependency between the Book object (subject) and the NotificationService (observer).

Explanation: The Book class acts as the subject, allowing observers to register interest and be notified of changes. The Observer abstract class declares the interface for concrete observers, and the NotificationService is a concrete observer that receives notifications when the book is updated.


## Code example:
Class: Book
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

    def update_book(self, new_author):
        self.author = new_author
        self.notify_observers()

```
Explanation:
The Book class acts as the subject (observable) in the Observer pattern:

Add/Remove Observers: The add_observer and remove_observer methods allow observers to subscribe and unsubscribe from changes in the book's state.

Notify Observers: The notify_observers method iterates over registered observers and triggers their update method, informing them about changes in the book.

Update Book State: The update_book method updates the book's state (author) and notifies observers, ensuring they are informed of any changes.


Class: NotificationService
```python
from domain.observer import Observer

class NotificationService(Observer):
    def update(self, book):
        print(f"Notification: Book '{book.title}' by {book.author} has been updated.")
```
Explanation:

The NotificationService class is a concrete observer:

Observer Interface Implementation: It implements the update method specified in the Observer interface, defining the action to be taken when notified.

Notification on Update: When the update method is called, it prints a notification message about the updated book, including the title and author.

## Output
```
Book Information:
Title: Mara
Author: Ioan Slavici

Notification: Book 'Mara' by I. Slavici has been updated.

After Update:Title: Mara
Author: I. Slavici
```
## Conclusion

In conclusion, the Library Management System effectively utilizes the Observer design pattern to maintain a decoupled relationship between the book objects and the observers. This pattern enhances the system's flexibility by allowing multiple observers to react to changes in the book's state independently. The project demonstrates a clean implementation of the Observer pattern for effective event handling in a library management context.

