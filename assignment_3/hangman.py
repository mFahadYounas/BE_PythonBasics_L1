import random


class Hangman:
    words: list[str] = [
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

    @staticmethod
    def _select_word() -> str:
        index = random.randrange(0, len(Hangman.words))
        return Hangman.words[index]

    @staticmethod
    def _find_char(c: str, word: str) -> list[int]:
        return [i for i in range(len(word)) if word[i] == c]

    @staticmethod
    def game() -> int:
        selected_word = Hangman._select_word()
        len_selected_word = len(selected_word)
        hidden_word = ["_" for _ in selected_word]
        print(hidden_word)

        allowed_guesses = 5
        correct_guess = 0

        while correct_guess < len_selected_word and allowed_guesses > 0:
            guessed_char = input("Guess a letter: ")
            found_idx = Hangman._find_char(guessed_char, selected_word)

            if found_idx:
                for i in found_idx:
                    hidden_word[i] = guessed_char
                    correct_guess += 1
                print(hidden_word)
                continue

            allowed_guesses -= 1
            print(hidden_word)
            print(f"Guesses remaining = {allowed_guesses}")

        if correct_guess == len_selected_word:
            print("You Win!")
            return 1

        if allowed_guesses == 0:
            print(f"You Lose! Word was {selected_word}")

        return 1
