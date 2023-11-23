#import required modules
import random
import logging
import image

logging.basicConfig(level=logging.INFO)
#Read words from given dictionary
def load_words(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            words = [line.strip() for line in lines]
            return words
    except FileNotFoundError:
        logging.error("File not found: %s", file_path)
        raise
#Generate "_" as per the length of words
def initialize_game(word):
    display = ["_" for _ in range(len(word))]
    return display
#Strategy to play game
def play_game(word, max_lives):
    lives = max_lives
    display = initialize_game(word)
    game_over = False

    while not game_over:
        guessed_letter = input("Guess a letter: ").lower()

        try:
            validate_input(guessed_letter)
        except ValueError as e:
            logging.warning("Invalid input: %s", str(e))
            continue

        update_display(word, guessed_letter, display)
        logging.info("Current state: %s", display)

        if guessed_letter not in word:
            lives -= 1
            logging.info("Incorrect guess. Lives remaining: %d", lives)

            if lives == 0:
                game_over = True
                logging.info("You Lose!! The word was: %s", word)

        if "_" not in display:
            game_over = True
            logging.info("You Win!!")

        logging.info(display_hangman(lives))
#check the letter given in right format
def validate_input(guessed_letter):
    if not guessed_letter.isalpha() or len(guessed_letter) != 1:
        raise ValueError("Invalid input. Please enter a single letter.")

def update_display(word, guessed_letter, display):
    for position in range(len(word)):
        letter = word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter

def display_hangman(lives):
    # Assuming image.hangman is a dictionary with hangman images for each life remaining
    return image.hangman[lives]

if __name__ == "__main__":
    file_path = "words_train.txt"
    max_lives = 6

    try:
        words = load_words(file_path)
        selected_word = random.choice(words)

        logging.info("Welcome to Hangman!")
        logging.info("Word to guess has %d letters", len(selected_word))

        play_game(selected_word, max_lives)

    except Exception as e:
        logging.error("An error occurred: %s", str(e))
