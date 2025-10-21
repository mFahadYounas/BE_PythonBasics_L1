def sum_avg_max(inlist):
    sum = 0
    for item in inlist:
        sum = sum + item
    average = sum / len(inlist)
    max1 = max(inlist)
    print(f"Sum = {sum}\nAverage = {average}\n Max = {max1}")
    return sum, average, max1


def reverse_list(input_list: list[int]):
    input_list.reverse()
    return input_list


print(reverse_list([1, 2, 5]))
