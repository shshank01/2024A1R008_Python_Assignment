# main_milestone4.py - Milestone 4: uses the modules library_utils and library_account
import time
from library_account import LibraryAccount
from library_utils import calculate_fine

catalogue = {"Python Basics": 2, "Data Structures": 1,
             "Computer Networks": 2, "Operating Systems": 0}

account1 = LibraryAccount("2023A1R015", "Riya Sharma")
account2 = LibraryAccount("2023A1R020", "Aman Verma")

account1.borrow_book("Python Basics", catalogue)
account1.borrow_book("Operating Systems", catalogue)
account1.borrow_book("Computer Networks", catalogue)
account2.borrow_book("Data Structures", catalogue)
account1.return_book("Python Basics", catalogue)

print("\nSummary:")
print(account1)
print(account2)

print("\nFine (default rate)  : Rs.", calculate_fine(18, 14))
print("Fine (rate=10)       : Rs.", calculate_fine(18, 14, rate=10))

# e) Transaction time using the time module
print("Transaction time     :", time.strftime("%d-%m-%Y %H:%M:%S"))
