from abc import ABC, abstractmethod

class LibraryComponent(ABC):
    @abstractmethod
    def display(self):
        pass
