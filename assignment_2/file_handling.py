import csv
import os


def read_student_data(filename: str) -> list[float]:
    try:
        with open(filename) as csv_file:
            reader = csv.reader(csv_file)
            _ = next(reader)
            avg_grade_list = []
            for row in reader:
                summation = sum(int(num) for num in row[2:])
                avg_grade = summation / len(row[2:])
                avg_grade_list.append(avg_grade)

            return avg_grade_list

    except FileNotFoundError as error:
        raise error


print(read_student_data("assignment_2/assets/student_data.csv"))


def address_book_in(operation):
    if operation == "add":
        name = input("Enter name of new contact: ")
        phone = input("Enter phone number of new contact: ")
        if not os.path.exists("Assignment-2/address_book.csv"):
            with open("Assignment-2/address_book.csv", "a") as f:
                f.write("Name,Phone\n")

        with open("Assignment-2/address_book.csv", "a") as f:
            f.write(f"{name},{phone}\n")
    elif "search":
        try:
            with open("Assignment-2/address_book.csv", "r") as f:
                reader = csv.reader(f)
                _ = next(reader)
                name = input("Enter name to search: ")
                for row in reader:
                    if row[0] == name:
                        print(f"Name = {name}, Phone = {row[1]}")

        except FileNotFoundError as error:
            print(f"{error}: Address book does not exist!")
    else:
        print("Invalid operation!")


# address_book_in("search")
