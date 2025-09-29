# Guess the Number Game (CLI)

A simple Python game where the computer picks a number between 1 and 100 and you try to guess it. The program tells you if your guess is too high or too low and counts your attempts.

## Features
- Random number between 1 and 100
- Feedback: too low / too high / correct
- Tracks number of attempts
- Option to play again

## Requirements
- Python 3.8+
- No external libraries required

## Run
```bash
python3 guess_number.py
```

## Usage
- Enter an integer guess when prompted
- Keep guessing until you get it right
- After a round, enter `yes` to play again or anything else to exit

## Example Session
```
Welcome to the Guess the Number Game!
I have chosen a number between 1 and 100. Can you guess it?
Enter your guess: 30
Too low! Try again.
Enter your guess: 70
Too high! Try again.
Enter your guess: 54
Correct! You guessed it in 3 attempts.
Do you want to play again? (yes/no): no
Thanks for playing! 
 Exiting...
```

## Project Structure
- `guess_number.py`: Game logic and CLI loop
