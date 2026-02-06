import random

WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():

    return WORDS[random.randint(0, len(WORDS) - 1)]

def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)


    guess = input("Guess a letter: ").lower()
    print("You guessed:", guess)

if __name__ == "__main__":
    play_game()