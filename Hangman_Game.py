import random

def hangman():
    # Predefined list of words
    words = ["PYTHON", "JAVA", "FIRST", "SECOND", "THIRD"]

    # Select a random word
    secret_word = random.choice(words)

    # Initialize game variables
    guessed_letters = []
    max_attempts = 6
    attempts_left = max_attempts
    word_progress = ["_"] * len(secret_word)

    # Game introduction
    print("*************************************************\n")
    print("               Welcome to Hangman!               \n")
    print("*************************************************\n")
    print(f"Guess the word. It has {len(secret_word)} letters.")
    print(" ".join(word_progress))
    print(f"You have {attempts_left} incorrect guesses allowed.\n")

    # Main game loop
    while attempts_left > 0 and "_" in word_progress:
        # Get user input
        guess = input("Guess a letter: ").upper()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (A-Z).")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        # Add to guessed letters
        guessed_letters.append(guess)

        # Check if guess is correct
        if guess in secret_word:
            print(f"Correct! '{guess}' is in the word.")
            # Update word progress for all occurrences of the guessed letter
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    word_progress[i] = guess
        else:
            attempts_left -= 1
            print(f"Sorry, '{guess}' is not in the word. Attempts left: {attempts_left}")

        # Display current status
        print("\n" + " ".join(word_progress))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}\n")

    # Game over message
    if "_" not in word_progress:
        print(f"Congratulations! You guessed the word: {secret_word}")
    else:
        print(f"Game over! The word was: {secret_word}")

if __name__ == "__main__":
    hangman()
