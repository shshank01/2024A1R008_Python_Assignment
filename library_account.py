# library_account.py - class file (uses the functions of library_utils.py)
from library_utils import is_available, prepare_summary


class LibraryAccount:
    library_name = "MIET Campus Library"
    max_books = 3

    def __init__(self, member_id, student_name):
        self.member_id = member_id
        self.student_name = student_name
        self.borrowed_books = []

    def borrow_book(self, title, catalogue):
        if title not in catalogue:
            print("Sorry,", title, "is not in the catalogue.")
        elif not is_available(catalogue, title):      # function from module
            print("Sorry,", title, "is not available right now.")
        elif len(self.borrowed_books) == self.max_books:
            print("Maximum limit of", self.max_books, "books reached.")
        else:
            self.borrowed_books.append(title)
            catalogue[title] = catalogue[title] - 1
            print(self.student_name, "borrowed", title)
            return True
        return False

    def return_book(self, title, catalogue):
        if title in self.borrowed_books:
            self.borrowed_books.remove(title)
            catalogue[title] = catalogue[title] + 1
            print(self.student_name, "returned", title)
            return True
        print(self.student_name, "has not borrowed", title)
        return False

    def display_account(self):
        print("Library   :", LibraryAccount.library_name)
        print("Member ID :", self.member_id)
        print("Name      :", self.student_name)
        print("Books     :", self.borrowed_books)

    def __str__(self):
        return prepare_summary(self.student_name, self.borrowed_books)
