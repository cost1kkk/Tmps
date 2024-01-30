# Library Management System

## Author: Baxanean Constantin

## Project Description
The Library Management System is a software application designed to facilitate the management of a library's book inventory using a modular and extensible architecture. The system allows users to define and organize books, create book instances, and manage the overall library structure.


### Use:
The project employs the Composite pattern for structuring the library component

The Proxy pattern for managing the creation of book objects

The Adapter pattern for adapting the display of library components.


### Theory:
Composite:
Composite is a structural design pattern that lets you compose objects into tree structures and then work with these structures as if they were individual objects. Useful when clients need to treat individual objects and compositions of objects uniformly.

Proxy:
Proxy is a structural design pattern that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

Adapter:
Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate. Useful when you want to make existing classes work with others without modifying their source code.




## Design Patterns Implemented

Composite Design Pattern

Class: LibraryComponent, Book, LibraryContainer

Purpose: To represent a hierarchical structure of library components.

Explanation: LibraryComponent is an abstract class that declares the common interface for all library components. Book is a leaf node representing individual books. LibraryContainer is a composite node representing containers for other library components.

Proxy Design Pattern

Class: BookFactory

Purpose: To shield the client from the complexities of book creation.

Explanation: BookFactory acts as a proxy, providing a simple interface for creating book objects. It shields the client from the complex book creation logic, maintaining a separation of concerns.

Adapter Design Pattern

Class: LibraryAdapter

Purpose: To adapt the display of library components.

Explanation: LibraryAdapter adapts a LibraryComponent to a different representation. It takes an existing LibraryComponent and adapts its display method, demonstrating flexibility in displaying library components differently.

## Code example:
Class: BookFactory
```python
from domain.book import Book

class BookFactory:
    @staticmethod
    def create_book(title, author):
        # Simulate complex book creation logic, perhaps involving a database
        return Book(title, author)

```


Explanation:

BookFactory serves as a proxy by providing a simple interface to create book objects. It shields the client from the complexity of book creation logic, showcasing the Proxy pattern.

Class: LibraryAdapter
```python
from domain.library_component import LibraryComponent

class LibraryAdapter(LibraryComponent):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def display(self):
        # Adapting the LibraryComponent to a different representation
        return f"Adapted: {self.adaptee.display()}"
```
Explanation: 

LibraryAdapter demonstrates the Adapter pattern by adapting the LibraryComponent interface to a different representation. It takes an existing LibraryComponent (adapter) and adapts its display method.

## Output
```
Library Contents:
Book: The Catcher in the Rye by J.D. Salinger
Book: To Kill a Mockingbird by Harper Lee

Adapted Library Component: 
Adapted: Book: The Catcher in the Rye by J.D. Salinger 
```
## Conclusion

In conclusion, the Library Management System project effectively applies the Composite pattern for organizing library components, the Proxy pattern for managing book creation complexity, and the Adapter pattern for adapting the display of library components. The modular design ensures code flexibility, scalability, and maintainability. While improvements could be made, the project demonstrates the practical benefits of well-utilized design patterns in creating a robust library management system.


