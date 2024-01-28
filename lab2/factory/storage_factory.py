from domain.components import Storage

class StorageFactory(ComponentFactory):
    def create_component(self):
        return Storage()
