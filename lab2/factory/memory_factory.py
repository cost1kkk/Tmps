from domain.components import Memory

class MemoryFactory(ComponentFactory):
    def create_component(self):
        return Memory()
