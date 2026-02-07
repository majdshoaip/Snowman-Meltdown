import random
from ascii_art import STAGES


WORDS = ["python", "git", "github", "snowman", "meltdown", "programming"]


def get_random_word():

    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):

    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("\n--- Welcome to Snowman Meltdown! ---")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)


        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You saved the snowman! 🎉")
            break

        guess = input("Guess a letter: ").lower()


        if len(guess) != 1 or not guess.isalpha():
            print(">> Invalid input! Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print(f">> You already guessed '{guess}'. Try a different letter.")
        elif guess in secret_word:
            print(f">> Good job! '{guess}' is in the word.")
            guessed_letters.append(guess)
        else:
            print(f">> Oops! '{guess}' is not there.")
            mistakes += 1
            guessed_letters.append(guess)
    else:


        display_game_state(mistakes, secret_word, guessed_letters)
        print("Game Over! The snowman has melted. ☃️🔥")
        print(f"The word was: {secret_word}")