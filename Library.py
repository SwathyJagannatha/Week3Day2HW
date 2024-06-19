from colorama import Fore, Back, Style
from termcolor import colored
from datetime import date

#Task 1: Library System Enhancement
def add_books(library):
        name_ip = input("Enter the Book Name\n")
        author_ip = input("Enter the Book author\n")

        book = (name_ip,author_ip)

        if book in library:
            print("Sorry the book already exists!!You are trying to add a duplicate!")
        else:
            #library.append((name_ip,author_ip))
            library.append(book)
        print(library)
        pass

def display_books(library):
    for books in library:
        #print(f"For the library book {Fore.RED}{books}{Style.RESET_ALL}")
        print(books)
        for item in books:
            print(f"- {Fore.LIGHTGREEN_EX}{item}{Style.RESET_ALL}")
            #print(item)

def delete_books(library):
        name_ip = input("Enter the Book you would like to delete\n")
        author_ip = input("Enter the Author of the Book\n")

        book = (name_ip,author_ip)

        if book not in library:
            print("Sorry the book doesnt exist!")
        else:
            library.remove(book)

        print("Library Catalogue after delete operation:")    
        display_books(library)

def main(library):
     while True:
        response = input("""
                         
                        Library Module:
                        
                         1. Insert new books into library(ensure duplicate books handling)
                         2. View the books
                         3. Delete books
                         4. Quit
                         
                         What would you like to do? """)
        
        if response == '1':
            add_books(library)
        elif response == '2':
            display_books(library)
        elif response == '3':
            delete_books(library)
        elif response == '4':
            break
        else:
            print('Please enter a valid input')

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
main(library)