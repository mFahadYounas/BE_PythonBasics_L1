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


# print(read_student_data("assignment_2/assets/student_data.csv"))


def address_book_operations(operation: str) -> int:
    file_name = "assignment_2/assets/address_book.csv"

    match operation:
        case "add":
            name = input("Enter name of new contact: ")
            phone = input("Enter phone number of new contact: ")

            if not os.path.exists(file_name):
                with open(file_name, "a") as f:
                    f.write("Name,Phone\n")

            with open(file_name, "a") as f:
                f.write(f"{name},{phone}\n")

            return 1

        case "search":
            try:
                with open(file_name, "r") as f:
                    reader = csv.reader(f)
                    _ = next(reader)
                    name = input("Enter name to search: ")
                    for row in reader:
                        if row[0] == name:
                            print(f"Name = {name}, Phone = {row[1]}")

            except FileNotFoundError as error:
                print(f"{error}: Address book does not exist!")

            return 1

        case _:
            raise ValueError("Invalid Operation!")


address_book_operations("add")
