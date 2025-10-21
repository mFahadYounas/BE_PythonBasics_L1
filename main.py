from assignment_1.calculator import calculator
from assignment_1.list_operations import reverse_list, sum_avg_max
from assignment_1.temperature_converter import temp_converter
from assignment_1.vowel_counter import vowel_counter


def main():
    print(calculator(3, 0, "/"))
    print(sum_avg_max([1, 3, 66]))
    print(reverse_list([1, 2, 5, 12, 0, 12, 5]))
    print(temp_converter(1, "celsius"))
    print(vowel_counter("sfaaeiAn3oxkdjdfdj"))


if __name__ == "__main__":
    main()
