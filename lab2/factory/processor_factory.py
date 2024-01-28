# factory/processor_factory.py
from domain.components import Processor

class ProcessorFactory(ComponentFactory):
    def create_component(self):
        return Processor()
