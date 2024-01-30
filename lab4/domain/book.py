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
