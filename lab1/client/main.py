import sys
 

from library_factory import LibraryFactory

def main():
    library_service = LibraryFactory.create_library_service()
    library_service.add_book("Harry Potter", "J. K. Rowling", "978-0606323451")
    library_service.add_book("Harap Alb", "Ion Creanga", "979-8985975147")
    library_service.add_book("Capra cu trei iezi", "Ion Creangă", " 978-9731968865")
    

    library_service.add_user("ion_da_silva", "ion.dasilva@gmail.com")
    library_service.add_user("mircea_adidas", "mircea.adidas@gmail.com")
    library_service.add_user("zinaida_fernandez", "zinaidafernandez@gmail.com")

    print("Books in the library:")
    for book in library_service.list_books():
        print(book)

    print("\nUsers of the library:")
    for user in library_service.list_users():
        print(user)

if __name__ == "__main__":
    main()
