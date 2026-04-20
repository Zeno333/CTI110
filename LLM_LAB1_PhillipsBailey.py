# LLM_LAB1
# Number Guessing Game
# This program lets the user guess a random number between 1 and 20.
# It gives hints and counts the number of guesses.
# The user can also choose to play again.

import random


def play_game():
    """Runs one round of the number guessing game."""
    secret_number = random.randint(1, 20)
    guess_count = 0

    print("\nI am thinking of a number between 1 and 20.")

    while True:
        guess = input("Enter your guess: ")

        # Check if the user entered a valid whole number
        if not guess.isdigit():
            print("Please enter a valid whole number.")
            continue

        guess = int(guess)
        guess_count += 1

        # Check if guess is within the allowed range
        if guess < 1 or guess > 20:
            print("Your guess must be between 1 and 20.")
        elif guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print(f"Correct! You guessed the number in {guess_count} tries.")
            break


def main():
    """Main function to control the game loop."""
    print("Welcome to the Number Guessing Game!")

    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ").strip().lower()

        if again != "yes":
            print("Thanks for playing!")
            break


# Start the program
main()