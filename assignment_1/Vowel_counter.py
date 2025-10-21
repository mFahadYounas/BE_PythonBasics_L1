def vowel_counter(string: str):
    count = 0
    new_string = string.lower()
    new_list = {"a", "e", "i", "o", "u"}
    for c in new_string:
        if c in new_list:
            count += 1

    return count


print(vowel_counter("sfAn3kdjdfdj"))
