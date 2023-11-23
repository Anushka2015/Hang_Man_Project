import random
import logging
import image
import statistics
import hangman

logging.basicConfig(level=logging.INFO)

# ... (rest of your code)

def play_game(word, max_lives):
    # ... (existing code)
    # 
   if __name__ == "__main__":
    file_path = "words_train.txt"
    max_lives = 6
    num_games = 100  # Number of games to play for statistical analysis

    wins = 0
    losses = 0

    try:
        words = load_words(file_path)

        for _ in range(num_games):
            selected_word = random.choice(words)

            logging.info("Welcome to Hangman!")
            logging.info("Word to guess has %d letters", len(selected_word))

            play_game(selected_word, max_lives)

            if "_" not in selected_word:
                wins += 1
            else:
                losses += 1

        logging.info("Statistics after %d games:", num_games)
        logging.info("Wins: %d", wins)
        logging.info("Losses: %d", losses)
        logging.info("Win Rate: %.2f%%", (wins / num_games) * 100)

    except Exception as e:
        logging.error("An error occurred: %s", str(e))
