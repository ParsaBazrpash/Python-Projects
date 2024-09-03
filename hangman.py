import random

def get_random_word():
    words = ['python', 'java', 'kotlin', 'javascript', 'hangman', 'software', 'engineering', 'programming']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    print("Welcome to Hangman!")
    word = get_random_word()
    guessed_letters = set()
    attempts = 6
    guessed_word = False

    while attempts > 0 and not guessed_word:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts remaining: {attempts}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            guessed_letters.add(guess)
        else:
            print(f"Oops! '{guess}' is not in the word.")
            guessed_letters.add(guess)
            attempts -= 1

        if all(letter in guessed_letters for letter in word):
            guessed_word = True

    if guessed_word:
        print(f"\nCongratulations! You guessed the word '{word}'.")
    else:
        print(f"\nGame Over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
