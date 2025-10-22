from typing import TypedDict


class SumAvgMaxOut(TypedDict):
    sum: int
    average: float
    max_in_list: int


def sum_avg_max(input_list: list[int]) -> SumAvgMaxOut:
    sum = 0
    for item in input_list:
        sum = sum + item
    average = sum / len(input_list)
    max_in_list = max(input_list)
    out: SumAvgMaxOut = {"sum": sum, "average": average, "max_in_list": max_in_list}
    return out


def reverse_list(input_list: list[int]) -> list[int]:
    left_point = 0
    right_point = len(input_list) - 1
    temp_for_swap = 0
    while left_point < right_point:
        temp_for_swap = input_list[left_point]
        input_list[left_point] = input_list[right_point]
        input_list[right_point] = temp_for_swap
        left_point += 1
        right_point -= 1
    return input_list
