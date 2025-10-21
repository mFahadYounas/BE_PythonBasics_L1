from assignment_1.calculator import calculator
from assignment_1.list_operations import reverse_list, sum_avg_max
from assignment_1.temperature_converter import temp_converter
from assignment_1.vowel_counter import vowel_counter
from assignment_2.data_validation import data_type_verifier
from assignment_2.fibonacci_sequence import fib_seq
from assignment_2.file_handling import read_student_data
from assignment_2.file_handling import address_book_operations
from assignment_2.word_frequency import word_freq


def main():
    # Assignment - 1
    print(calculator(3, 0, "/"))
    print(sum_avg_max([1, 3, 66]))
    print(reverse_list([1, 2, 5, 12, 0, 12, 5]))
    print(temp_converter(1, "celsius"))
    print(vowel_counter("sfaaeiAn3oxkdjdfdj"))

    # Assignment - 2
    print(data_type_verifier("your@gmail.com", "email"))
    print(fib_seq(3))
    print(read_student_data("assignment_2/assets/student_data.csv"))
    address_book_operations("add")
    print(word_freq())


if __name__ == "__main__":
    main()
