# m3_oop.py - Milestone 3: Refactored using OOP
# The logic of the Milestone 2 version is moved into the LibraryAccount class

class LibraryAccount:
    library_name = "MIET Campus Library"      # a) class variable
    max_books = 3

    # b) Constructor
    def __init__(self, member_id, student_name):
        self.member_id = member_id
        self.student_name = student_name
        self.borrowed_books = []

    # c) Instance methods
    def borrow_book(self, title, catalogue):
        if title not in catalogue:
            print("Sorry,", title, "is not in the catalogue.")
        elif catalogue[title] == 0:
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

    # d) Short member / borrowing summary
    def __str__(self):
        return (self.student_name + " (" + self.member_id + ") has "
                + str(len(self.borrowed_books)) + " book(s)")


# Fine calculation of Milestone 1 / 2 kept as a function
def calculate_fine(days_kept, allowed_days, rate):
    overdue_days = days_kept - allowed_days
    if overdue_days > 0:
        return overdue_days * rate
    return 0


# e) Create two objects and demonstrate borrow and return
catalogue = {"Python Basics": 2, "Data Structures": 1,
             "Computer Networks": 2, "Operating Systems": 0}

account1 = LibraryAccount("2023A1R015", "Riya Sharma")
account2 = LibraryAccount("2023A1R020", "Aman Verma")

account1.borrow_book("Python Basics", catalogue)
account1.borrow_book("Operating Systems", catalogue)
account1.borrow_book("Computer Networks", catalogue)
account2.borrow_book("Data Structures", catalogue)
account2.borrow_book("Machine Learning", catalogue)
account1.return_book("Python Basics", catalogue)

print("\n--- Account 1 ---")
account1.display_account()
print("\n--- Account 2 ---")
account2.display_account()

print("\nSummary:")
print(account1)
print(account2)

print("\nFine for 18 days kept, 14 allowed, Rs. 5/day: Rs.",
      calculate_fine(18, 14, 5))
print("\nUpdated Catalogue:")
for title, copies in catalogue.items():
    print(" ", title, ":", copies)
