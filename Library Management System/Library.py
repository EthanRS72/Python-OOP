#OOP project - Library management system
#Classes: Library - display_books, lend_book, add_book, return book

import sys

class Library:
    #Default constructor
    def __init__(self, list, name):
        self.book_list = list
        self.name = name
        self.loaned_dict = {}

    #Prints all books in the library
    def display_books(self):
        print(f"Welcome to the {self.name} library, we have the following books in our library")
        sno = 1
        for book in self.book_list:
            print(f"{sno}: {book}")
            sno += 1
        print("\n")

    #Method to lend out a book, checks for present and not already booked
    def lend_book(self, book, name):
        if book in self.book_list:
            if book not in self.loaned_dict:
                self.loaned_dict.update({book: name})
                print(f"Lend complete to {name}, book: {book} can be taken from the library\n")
            else:
                print(f"Book {book} unavailable, has been loaned out by {self.loaned_dict[book]}\n")
        else:
            print(f"Book: {book} cannot be found\n")

    #Method to add a new book
    def add_book(self, book):
        self.book_list.append(book)
        print(f"Book: {book} has been added to the library\n")

    #Method to return a book
    def return_book(self, book):
        if book in self.book_list:
            if book in self.loaned_dict.keys():
                returner = self.loaned_dict[book]
                self.loaned_dict.pop(book)
                print(f"Book: {book} has been returned by {returner}\n")
            else:
                print(f"Book: {book} has not been loaned\n")
        else:
            print(f"Book: {book} cannot be found\n")



if __name__ == '__main__':
    computing_library = Library(["Python", "Java", "Data Science", "Web Scraping", "Data Mining"], "Computing School")
    while (True):
        print(f"Welcome to the {computing_library.name} library, please select an option: ")
        print("---------------------------------------------------------------------------")
        print("1 to view all books ")
        print("2 to add a books ")
        print("3 to loan a books ")
        print("4 to return a book ")
        print("5 to quit \n")

        choice = str(input("Select an option from above ")).strip()
        if choice not in ["1", "2", "3", "4", "5"]:
            print("Please select a valid option")
            continue
        else:
            choice = int(choice)

        if choice == 1:
            computing_library.display_books()
        elif choice == 2:
            new_book = str(input("Please enter the book you wish to add")).strip()
            computing_library.add_book(new_book)
        elif choice == 3:
            book_to_loan = str(input("Please enter the book you wish to loan")).strip()
            loanee = str(input("Who is loaning this book?")).strip()
            computing_library.lend_book(book_to_loan, loanee)
        elif choice == 4:
            book_to_return = str(input("Please enter the book you wish to return")).strip()
            computing_library.return_book(book_to_return)
        elif choice == 5:
            sys.exit()
        else:
            print("ERROR")