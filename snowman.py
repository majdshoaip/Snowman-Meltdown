from game_logic import play_game

def main():
    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again not in ['yes', 'y']:
            print("Thanks for playing Snowman Meltdown! Goodbye!")
            break

if __name__ == "__main__":
    main()