from domain.library_component import LibraryComponent

class LibraryAdapter(LibraryComponent):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def display(self):
        # Adapting the LibraryComponent to a different representation
        return f"Adapted: {self.adaptee.display()}"
