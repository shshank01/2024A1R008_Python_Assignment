# m2_catalogue_loop.py - Milestone 2: Catalogue, Decisions and Loops
# Extends the Milestone 1 version (the new parts are marked as NEW)

# ----- Student details (same as Milestone 1) -----
student_name = input("Enter student name: ").title()
roll_no = input("Enter roll number: ")

# NEW a) Catalogue stored in a dictionary {book title: available copies}
catalogue = {
    "Python Basics": 2,
    "Data Structures": 1,
    "Computer Networks": 2,
    "Operating Systems": 0
}
borrowed_books = []     # NEW d) list to store the borrowed books
MAX_BOOKS = 3

# NEW b) Keep asking until DONE is typed or 3 books are borrowed
while len(borrowed_books) < MAX_BOOKS:
    choice = input("Enter book title (or DONE to finish): ").strip()

    if choice.upper() == "DONE":
        break

    choice = choice.title()

    # NEW c) Selection statements: reject unknown / unavailable books
    if choice not in catalogue:
        print("Sorry, this book is not in the catalogue.")
    elif catalogue[choice] == 0:
        print("Sorry,", choice, "is not available right now.")
    else:
        # NEW d) Store the book and reduce the available copies
        borrowed_books.append(choice)
        catalogue[choice] = catalogue[choice] - 1
        print(choice, "borrowed successfully.")

if len(borrowed_books) == MAX_BOOKS:
    print("Maximum limit of 3 books reached.")

# ----- Fine calculation (Milestone 1 logic, now with a decision) -----
days_kept = int(input("\nEnter days kept: "))
allowed_days = int(input("Enter allowed days: "))
fine_rate = float(input("Enter daily fine rate (Rs.): "))

overdue_days = days_kept - allowed_days
if overdue_days > 0:
    total_fine = overdue_days * fine_rate
else:
    total_fine = 0

# NEW e) Display the borrowed list and the updated catalogue
print("\n----- LIBRARY RECEIPT -----")
print("Student Name :", student_name)
print("Roll Number  :", roll_no)
print("Books Borrowed:")
for book in borrowed_books:
    print("  -", book)
print("Overdue Days :", overdue_days)
print("Total Fine   : Rs.", total_fine)

print("\nUpdated Catalogue:")
for title, copies in catalogue.items():
    print(" ", title, ":", copies)
