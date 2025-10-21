import random

words = [
    "serendipity",
    "ephemeral",
    "ubiquitous",
    "mellifluous",
    "cacophony",
    "luminous",
    "benevolent",
    "quintessential",
    "resplendent",
    "gregarious",
    "eloquence",
    "vicarious",
    "perseverance",
    "breathtaking",
    "nostalgia",
    "discombobulated",
    "incandescent",
    "flourish",
    "soliloquy",
    "magnanimous",
]

def select_word(words):
    index = random.randrange(0, len(words))
    return words[index]

def find_char(c, word):
    found_idx = []
    for i in range(len(word)):
        if word[i] == c:
            found_idx.append(i)
    return found_idx


def game():
    selected_word = select_word(words)
    len_selected_word = len(selected_word)
    hidden_word = '_' * len_selected_word
    print(hidden_word)
    hidden_word = list(hidden_word)

    allowed_guesses = 5
    correct_guess = 0

    while correct_guess < len_selected_word and allowed_guesses > 0:
        gc = input("Guess a letter: ")
        found_idx = find_char(gc, selected_word)
        if(found_idx):
            for i in found_idx:
                hidden_word[i] = gc
                correct_guess += 1
            print(hidden_word)
        else:
            allowed_guesses -= 1
            print(hidden_word)
            print(f"Guesses remaining = {allowed_guesses}")

    if(correct_guess == len_selected_word):
        print("You Win!")
        return
    if(allowed_guesses == 0):
        print("You Lose!")

game()