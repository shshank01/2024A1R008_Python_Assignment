# m1_basic_loan.py - Milestone 1: Basic Data Handling for a Book Loan

# a) Take input from the user
student_name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
book_title = input("Enter book title: ")

# b) Convert numeric inputs to suitable data types
days_kept = int(input("Enter days kept: "))
allowed_days = int(input("Enter allowed days: "))
fine_rate = float(input("Enter daily fine rate (Rs.): "))

print("\nType of days kept :", type(days_kept))
print("Type of fine rate :", type(fine_rate))

# c) Calculate overdue days and total fine (book is assumed overdue)
overdue_days = days_kept - allowed_days
total_fine = overdue_days * fine_rate

# d) String operations to format the name and the book title
student_name = student_name.title()
book_title = book_title.upper()

# e) Display the result
print("\n----- LIBRARY LOAN RECEIPT -----")
print("Student Name :", student_name)
print("Roll Number  :", roll_no)
print("Book Title   :", book_title)
print("Overdue Days :", overdue_days)
print("Total Fine   : Rs.", total_fine)
