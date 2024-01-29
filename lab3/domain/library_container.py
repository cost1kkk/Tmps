from domain.library_component import LibraryComponent

class LibraryContainer(LibraryComponent):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def display(self):
        display_info = ""
        for child in self.children:
            display_info += child.display() + "\n"
        return display_info
