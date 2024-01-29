from domain.library_component import LibraryComponent

class Book(LibraryComponent):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        return f"Book: {self.title} by {self.author}"
