# library_storage.py - file handling and exception handling of the library application
# (Milestone 5; main.py imports save_record, show_records and read_number from here)

# ===== NEW in Milestone 5: file handling and exception handling =====
FILE_NAME = "library_records.txt"


# a) Append one transaction at the end of the file
def save_record(record):
    with open(FILE_NAME, "a") as file:
        file.write(record + "\n")


# b) Read and display the saved records
# d) Handle the case when the file is not available
def show_records():
    try:
        with open(FILE_NAME, "r") as file:
            print("\n----- SAVED RECORDS -----")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: library_records.txt not found. No records saved yet.")


# c) Keep asking until a valid number is typed
def read_number(message, number_type):
    while True:
        try:
            return number_type(input(message))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
