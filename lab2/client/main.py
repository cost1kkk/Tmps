from domain.computer import Computer
from factory.computer_factory import ComputerFactory
from factory.processor_factory import ProcessorFactory
from factory.memory_factory import MemoryFactory
from factory.storage_factory import StorageFactory

def main():
    # Create factories
    computer_factory = ComputerFactory()
    processor_factory = ProcessorFactory()
    memory_factory = MemoryFactory()
    storage_factory = StorageFactory()

    # Create components
    processor = processor_factory.create_component()
    memory = memory_factory.create_component()
    storage = storage_factory.create_component()

    # Create computer using the factory
    computer = computer_factory.create_computer(processor, memory, storage)

    # Display information about the computer
    print("Computer Configuration:")
    print(f"Processor: {type(computer.processor).__name__}")
    print(f"Memory: {type(computer.memory).__name__}")
    print(f"Storage: {type(computer.storage).__name__}")

if __name__ == "__main__":
    main()
