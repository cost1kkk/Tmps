import sys 
from library_service import LibraryService

class LibraryFactory:
    @staticmethod
    def create_library_service():
        return LibraryService()
