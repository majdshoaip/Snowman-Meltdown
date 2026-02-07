import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    display_word = "".join([l + " " if l in guessed_letters else "_ " for l in secret_word])
    print("Word: ", display_word)

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You saved the snowman! 🎉")
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        elif guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
            guessed_letters.append(guess)
        else:
            print(f"Oops! '{guess}' is not there.")
            mistakes += 1
            guessed_letters.append(guess)
    else:
        display_game_state(mistakes, secret_word, guessed_letters)
        print("Game Over! The snowman has melted. ☃️🔥")
        print(f"The word was: {secret_word}")