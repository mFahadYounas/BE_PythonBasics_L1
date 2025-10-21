import re


def word_freq() -> dict:
    file_name = "assignment_2/assets/my_text.txt"
    freqs = {}
    text = ""
    try:
        with open(file_name) as f:
            text = f.read()
    except FileNotFoundError as error:
        raise (error)

    words = [word for word in re.split(r"\W+", text) if word]

    for word in words:
        if word not in freqs:
            freqs[word] = 1
        else:
            freqs[word] = freqs[word] + 1

    return freqs


print(word_freq())
