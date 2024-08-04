# Program: Hangman

# Imports
import random
from words import word_list
from arts import logo, stages

# Greet the User and display the logo
print(f"Welcome to Hangman!\n{logo}")

end_game: bool = False  # Variable to control the game loop
lives: int = 6  # Number of lives

# Choosing a random word from the word list
chosen_word: str = random.choice(word_list)
# Creating the display with underscores for each letter in the chosen word
guess_display: list = ['_' for char in chosen_word]

while not end_game:
    guess: str = input("\nGuess a letter: ").lower()  # Asking user to guess a letter
    if guess in guess_display:
        print(f"You have already guessed {guess}")

    # Checking if the guessed letter is in the chosen word
    for position in range(len(chosen_word)):
        letter: str = chosen_word[position]
        if letter == guess:
            guess_display[position] = letter

    # Display the current state of the word
    print(f"{' '.join(guess_display)}")

    # If the guessed letter is not in the chosen word
    if guess not in chosen_word:
        print(f"\nYou guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1  # Decrease the number of lives
        print(stages[lives])
        if lives == 0:
            end_game = True  # End the game if no lives are left
            print("\nYou Lose!")
            print(chosen_word)

    # If there are no more underscores in the display, the user has won
    if '_' not in guess_display:
        end_game = True
        print("\nYou Win!")
