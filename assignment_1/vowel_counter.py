def vowel_counter(string: str) -> int:
    count = 0
    vowel_set = {"a", "e", "i", "o", "u"}
    lower_string = string.lower()
    vowel_count_gen = (1 for c in lower_string if c in vowel_set)
    count = sum(vowel_count_gen)
    return count
