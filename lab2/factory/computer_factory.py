from domain.computer import Computer

class ComputerFactory:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ComputerFactory, cls).__new__(cls)
        return cls._instance

    def create_computer(self, processor, memory, storage):
        return Computer(processor, memory, storage)
