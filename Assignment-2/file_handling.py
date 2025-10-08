import csv
import os

def read_student_data():
    try:
        with open('Assignment-2/student_data.csv') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)
            avg_grade_list = []
            for row in reader:
                avg_grade = (int(row[2]) + int(row[3]) + int(row[4]) + int(row[5]))/4
                avg_grade_list.append(avg_grade)

            print(avg_grade_list)

    except FileNotFoundError as error:
        print(error)

# read_student_data()

def address_book_in(operation):
    if(operation == 'add'):
        name = input("Enter name of new contact: ")
        phone = input("Enter phone number of new contact: ")
        if(not os.path.exists("Assignment-2/address_book.csv")):
            with open("Assignment-2/address_book.csv", "a") as f:
                f.write("Name,Phone\n")

        with open("Assignment-2/address_book.csv", "a") as f:
            f.write(f"{name},{phone}\n")
    elif("search"):
        try:
            with open("Assignment-2/address_book.csv", 'r') as f:
                reader = csv.reader(f)
                header = next(reader)
                name = input("Enter name to search: ")
                for row in reader:
                    if(row[0] == name):
                        print(f"Name = {name}, Phone = {row[1]}")

        except FileNotFoundError as error:
            print(f"{error}: Address book does not exist!")
    else:
        print("Invalid operation!")
        

address_book_in("search")