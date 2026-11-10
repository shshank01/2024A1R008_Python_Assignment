# main.py - Milestone 5 (FINAL): menu based library application
import time
from library_account import LibraryAccount
from library_utils import calculate_fine
from library_storage import save_record, show_records, read_number

catalogue = {"Python Basics": 2, "Data Structures": 1,
             "Computer Networks": 2, "Operating Systems": 0}


def make_record(account, action, title, fine):
    now = time.strftime("%d-%m-%Y %H:%M")
    return (now + " | " + action + " | " + account.member_id + " | "
            + title + " | Fine: Rs." + str(fine))


print("===== MIET Campus Library =====")
name = input("Enter student name: ").title()
roll_no = input("Enter roll number: ")
account = LibraryAccount(roll_no, name)

while True:
    print("\n1. Borrow  2. Return  3. View records  4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter book title: ").strip().title()
        if account.borrow_book(title, catalogue):
            save_record(make_record(account, "BORROW", title, 0))

    elif choice == "2":
        title = input("Enter book title: ").strip().title()
        if account.return_book(title, catalogue):
            days_kept = read_number("Days kept: ", int)
            allowed_days = read_number("Allowed days: ", int)
            rate = read_number("Fine rate per day (Rs.): ", float)
            fine = calculate_fine(days_kept, allowed_days, rate)
            print("Fine to pay: Rs.", fine)
            save_record(make_record(account, "RETURN", title, fine))

    elif choice == "3":
        show_records()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
