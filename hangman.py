import random

# List of predefined words
words = ["apple", "mango", "grape", "peach", "lemon"]

# Select a random word
secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman!")

while wrong_guesses < max_wrong_guesses:

    # Display the word with hidden letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Remaining guesses:", max_wrong_guesses - wrong_guesses)

    # Check if the player has won
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word.")
        break

    # Take input from the user
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Game over
if wrong_guesses == max_wrong_guesses:
    print("\nGame Over!")
    print("The word was:", secret_word)
    
    
    
    
    