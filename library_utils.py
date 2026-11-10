# library_utils.py - helper functions of the library application

# c) Default parameter: rate=5 is used when no rate is given
def calculate_fine(days_kept, allowed_days, rate=5):
    overdue_days = days_kept - allowed_days
    if overdue_days > 0:
        return overdue_days * rate
    return 0


# b) The catalogue (dictionary) is passed as an argument
def is_available(catalogue, title):
    return title in catalogue and catalogue[title] > 0


# b) The borrowed-books list is passed as an argument
def prepare_summary(student_name, borrowed_books):
    if len(borrowed_books) == 0:
        return student_name + " has not borrowed any book"
    return (student_name + " has borrowed " + str(len(borrowed_books))
            + " book(s): " + ", ".join(borrowed_books))
