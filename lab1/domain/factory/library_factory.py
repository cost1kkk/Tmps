# importing sys
import sys
 
# adding domain to the system path
sys.path.insert(1, '/home/niciu/lab1/domain')
 
# importing the hello
from library_service import LibraryService

class LibraryFactory:
    @staticmethod
    def create_library_service():
        return LibraryService()