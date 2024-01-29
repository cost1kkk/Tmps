# Computer Configuration System

## Author: Baxanean Constantin

## Project Description
The Computer Configuration System is a software application designed to create and manage computer configurations using a modular and extensible architecture. The system allows users to define and assemble various components, such as processors, memory, and storage, to create customized computer configurations.


### Use:
The Factory Method pattern is used in the ComponentFactory

The Singleton pattern is used in the ComputerFactory class


### Theory:
Singleton:
Ensures a class has only one instance and provides a global point of access to it. Useful when exactly one object is needed to coordinate actions across the system.

Builder:
Separates the construction of a complex object from its representation, allowing the same construction process to create different representations. Useful when an object needs to be constructed with various configurations.

Prototype:
Creates new objects by copying an existing object, known as the prototype. Useful when the cost of creating an object is more expensive than copying an existing one.

Object Pooling:
Manages a pool of reusable objects, reducing the overhead of creating and destroying instances. Useful when creating and initializing objects is resource-intensive.

Factory Method:
Defines an interface for creating an object, but leaves the choice of its type to the subclasses, creating instances of a class in a method. Useful when a class cannot anticipate the class of objects it must create.

Abstract Factory:
Provides an interface for creating families of related or dependent objects without specifying their concrete classes. Useful when a system needs to be independent of how its objects are created, composed, and represented




## Design Patterns Implemented

Factory Method Pattern

Class: ComponentFactory

Purpose: To create objects (computer components) without specifying the exact class to instantiate.

Explanation: The ComponentFactory class provides a method create_component() that is overridden by its subclasses (ProcessorFactory, MemoryFactory, StorageFactory). This promotes code decoupling and allows extending the 
system with new components without modifying existing code.

Singleton Pattern

Class: ComputerFactory

Purpose: To restrict the instantiation of a class to a single instance and provide a global point of access to it.

Explanation: ComputerFactory ensures that only one instance is created by utilizing a variation of the Singleton pattern. This ensures a single point of access for creating computers throughout the application.


## Code example:
Class: ComputerFactory
```python
from domain.computer import Computer
class ComputerFactory:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ComputerFactory, cls).__new__(cls)
        return cls._instance

    def create_computer(self, processor, memory, storage):
        return Computer(processor, memory, storage)
```


Explanation:

ComputerFactory implements a variation of the Singleton pattern.

The _instance variable ensures that only one instance of ComputerFactory is created.

The __new__ method is overridden to manage the creation of the instance.

The create_computer method creates and returns a Computer object.

This ensures a single point of access for creating computers throughout the application, controlling the instantiation of the factory class.


Class: ComponentFactory
```python
class ComponentFactory:
    def create_component(self):
        pass
```
ComponentFactory defines the Factory Method create_component(), leaving the creation of components to its subclasses.

This allows the system to create components without specifying their exact classes, promoting code decoupling and extensibility.

## Conclusion

In summary, the Computer Configuration System project effectively applies the Factory Method for flexible component creation and a variation of the Singleton pattern for centralized instance management. The modular design ensures code flexibility and scalability. While improvements could be made, the project demonstrates the practical benefits of well-utilized design patterns in creating a robust and maintainable software structure.

