import random

# -------------------------------------------
# Function to play the Guess the Number game
# -------------------------------------------
def guess_number():
    """
    Generate a random number between 1 and 100 and
    let the user guess it until correct.
    Provides feedback if the guess is too high or too low.
    """
    number = random.randint(1, 100)  # Random number to guess
    attempts = 0                       # Counter for attempts
    guess = None                       # Initialize user guess

    print("Welcome to the Guess the Number Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    # Loop until the user guesses the correct number
    while guess != number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1  # Increment attempt count

            if guess < number:
                print("Too low! Try again.")   # Hint if guess is lower
            elif guess > number:
                print("Too high! Try again.")  # Hint if guess is higher
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")  # Correct guess
        except ValueError:
            print("Please enter a valid number.")  # Handle non-integer input


# Main function
def main():
    """
    Main loop to run the game repeatedly until the user chooses to exit.
    """
    while True:
        guess_number()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! \n Exiting...")
            break  # Exit the loop and end the program


# Starter function
if __name__ == "__main__":
    main()
