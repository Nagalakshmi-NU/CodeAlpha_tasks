import random

def hangman():
    # List of 5 predefined words
    words = ["apple", "banana", "cherry", "grape", "orange"]
    word = random.choice(words)  # Randomly choose a word
    guessed_letters = []  # To store correct and incorrect guesses
    attempts = 6  # Maximum wrong guesses allowed

    print("Welcome to Hangman!")
    print("_ " * len(word))  # Display underscores for each letter

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Correct guess
        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

        # Display the current word with guessed letters revealed
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word.strip())

        # Check if the player guessed all letters
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word that is {word}!")
            break
    else:
        print(f"Game over! The word was '{word}'.")

# Run the game
hangman()
